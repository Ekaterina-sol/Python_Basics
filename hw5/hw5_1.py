f = open('text1.txt', 'w+', encoding='utf-8')

while True:
    text_line = input("Введите строку. Для окончания ввода нажмите Enter: ")
    f.write(text_line+'\n')
    if text_line == '':
        break
print("Ввод данных завершен")
f.close()

f = open('text1.txt', encoding='utf-8')
content = f.readlines()
print(content)
f.close()