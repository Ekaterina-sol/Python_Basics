translation = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
russian_translation = []
with open ('text4.txt', encoding='utf-8') as f:
    words = f.read().split('\n')
    for line in words:
        line = line.split(" — ")
        print(line)
        if line[0] in translation:
            word = translation[line[0]]
            russian_translation.append(word +' — '+ line[1])
    print(russian_translation)
f.close()
with open('file_4_ru.txt', 'w', encoding='utf-8') as ru_f:
    for word in russian_translation:
        ru_f.write(word + '\n')
ru_f.close()