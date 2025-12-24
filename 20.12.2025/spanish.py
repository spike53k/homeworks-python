def translate(text):
    words = {"привет":"Hola", "мир":"mundo", "как":"como", "дела":"estas"}
    result = text
    for ru, es in words.items():
        result = result.replace(ru, es)
    return result