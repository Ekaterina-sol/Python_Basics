def int_func(user_text):
    word = user_text.title()
    return word

user_text = input("Введите слово или предложение из маленьких латинских букв: ")
print(int_func(user_text))


