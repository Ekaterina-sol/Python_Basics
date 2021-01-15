f = open('text2.txt', encoding='utf-8')
user_text = f.readlines()
print(user_text)
print("Количество строк в файле: ", len(user_text))
f.close()
f = open('text2.txt', encoding='utf-8')
for i in range(len(user_text)):
    user_string = f.readline()
    user_string = user_string.split()
    print(f'Количество слов в строке {i+1}: {len(user_string)}')
    i += 1
f.close()