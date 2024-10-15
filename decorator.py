import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # start
        result = func(*args, **kwargs)  
        end_time = time.time()  # end
        print(f"function '{func.__name__}' worktime: {end_time - start_time:.4f} s")
        return result
    return wrapper

# sum 
@time_decorator
def calculate_sum(a, b):
    result = a + b
    print(f"sum: {result}")
    return result

# from input.txt read and write to output.txt 
@time_decorator
def read_and_write_sum():
    try:
        with open('input.txt', 'r') as infile:
            a, b = map(int, infile.read().split())
        
        result = a + b
        
        with open('output.txt', 'a') as outfile:
            outfile.write(f"sum: {result}\n")
        
        print(f"have write output.txt: {result}")
    except Exception as e:
        print(f"erro: {e}")

# test
if __name__ == "__main__":
    # test calculate_sum 
    calculate_sum(5, 10)

    # create input.txt and write
    with open('input.txt', 'w') as infile:
        infile.write("3 7")

    # test read_and_write_sum 
    read_and_write_sum()
