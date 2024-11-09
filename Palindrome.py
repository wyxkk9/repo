def is_palindrome(s):
    # Удалить пробелы и преобразовать строку в нижний регистр
    s = s.replace(" ", "").lower()
    # Проверьте, равна ли строка своей обратной
    return s == s[::-1]

# test
test_string = "A man a plan a canal Panama"
if is_palindrome(test_string):
    print(f'"{test_string}" Да')
else:
    print(f'"{test_string}" Нет ')
