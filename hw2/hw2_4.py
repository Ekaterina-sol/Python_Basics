user_text = input("Введите текст: ")

user_string = user_text.split(' ')

for num, word in enumerate(user_string, 1):
    if len(word) > 10:
        word = word[:10]
    print(str(num) + " " + str(word))
