def translate(text):
    words = {"привет":"Hello", "мир":"world", "как":"how", "дела":"are you"}
    result = text
    for ru, en in words.items():
        result = result.replace(ru, en)
    return result