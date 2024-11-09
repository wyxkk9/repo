def filter_strings(filter_func, string_array):
    return list(filter(filter_func, string_array))

# definition
filter_condition = lambda s: s.strip() and not s.startswith('a') and len(s) >= 5

# test
string_array = [
    "apple",
    "banana",
    "hello",
    "   ",
    "world",
    "a quick brown fox",
    "goodbye",
    "hi"
]

# try
filtered_array = filter_strings(filter_condition, string_array)

# out
print(filtered_array)
