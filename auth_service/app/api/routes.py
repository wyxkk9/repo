from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.db import schemas, models
from app.db.database import get_db
from app.services.auth_service import register_user, authenticate_user
from app.utils.jwt_handler import decode_token
from app.utils.redis_handler import blacklist_token

router = APIRouter()

# 用户注册
@router.post("/register", response_model=schemas.UserCreate)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return register_user(db, user)

# 用户登录
@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    auth_tokens = authenticate_user(db, user.email, user.password)
    if not auth_tokens:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return auth_tokens

# 刷新令牌
@router.post("/refresh")
def refresh_token(refresh_token: str):
    try:
        payload = decode_token(refresh_token)
        access_token = create_access_token({"sub": payload["sub"]}, timedelta(minutes=15))
        return {"access_token": access_token, "token_type": "bearer"}
    except:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

# 更新用户信息
@router.put("/user/update")
def update_user(
    user_update: schemas.UserUpdate,
    db: Session = Depends(get_db),
    token: str = Depends(decode_token),
):
    email = token["sub"]
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user_update.email:
        user.email = user_update.email
    if user_update.password:
        user.hashed_password = pwd_context.hash(user_update.password)
    db.commit()
    return {"message": "User updated successfully"}

# 查看登录历史
@router.get("/user/history")
def get_login_history(
    db: Session = Depends(get_db), token: str = Depends(decode_token)
):
    email = token["sub"]
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    history = db.query(models.LoginHistory).filter(models.LoginHistory.user_id == user.id).all()
    return {"login_history": history}

# 用户登出
@router.post("/logout")
def logout(token: str = Depends(decode_token)):
    expiry = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")) * 60
    blacklist_token(token, expiry)  # 令牌过期时间为 15 分钟
    return {"message": "Logged out successfully"}


@router.get("/user/history")
def get_login_history(
    request: Request, db: Session = Depends(get_db), token: str = Depends(decode_token)
):
    email = token["sub"]
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    history = db.query(models.LoginHistory).filter(models.LoginHistory.user_id == user.id).all()
    return {"login_history": [h.to_dict() for h in history]}