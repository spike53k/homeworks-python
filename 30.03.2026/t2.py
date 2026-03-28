with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

total_lines = len(lines)

total_words = 0
for line in lines:
    words = line.split()
    word_count = len(words)
    total_words += word_count

longest_line = ""
for line in lines:
    if len(line) > len(longest_line):
        longest_line = line

longest_line_length = len(longest_line.strip())

print(f"Количество строк: {total_lines}")
print(f"Количество слов: {total_words}")
print(f"Самая длинная строка: {longest_line_length} символов")