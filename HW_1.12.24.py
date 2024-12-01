from tkinter.scrolledtext import example

example = 'Urban'
half_index = len(example) // 3
print(example[0])
print(example[-1])
print(example[half_index + 1:])
print(example[::-1])
print(example[1::2])