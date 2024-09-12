# file_io.py

# Read from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:", content)

from collections import Counter

def word_frequency(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower().split()
#将文本转换小写并分词
        word_count = Counter(text)
        for word, freq in word_count.items():
            print(f"{word}: {freq}")
#计算词频并打印

word_frequency('example.txt')