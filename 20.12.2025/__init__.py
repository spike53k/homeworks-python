def translate(text, l):
    if l == "english":
        import translator.english
        return translator.english.translate(text)
    elif l == "spanish":
        import translator.spanish
        return translator.spanish.translate(text)
    else:
        return "такого языка нет"