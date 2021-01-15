import math
with open('text6.txt', encoding='utf-8') as f:
    subject_dict = {}
    subjects = []
    quanitites = []
    new_quantities = []
    subject_list = f.read().split('\n')
    print(subject_list)
    for subject in subject_list:
        subject = subject.split(":")
        subjects.append(subject[0])
        quanitites.append(subject[1])
    for quant in quanitites:
        quant = quant.split(" ")
        number = 0
        subj_quant = []
        for number in quant:
            i = number.rfind('(')
            number = number[:i]
            if number != "":
                subj_quant.append(number)
        sum = 0
        for el in subj_quant:
            el = int(el)
            sum = sum + el
        new_quantities.append(sum)
    subject_dict = dict(zip(subjects, new_quantities))
    print(subject_dict)
f.close()