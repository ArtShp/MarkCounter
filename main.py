def count(a, b):
    tekyshaya_list = a
    kolonka_list = b

    mark_list = [[], [], [], [], [], [], [], [], [], [], []]
    chast_povtor = 0
    itog_mark_list = kolonka_list

    for i in tekyshaya_list:
        mark_list[i].append(i)

    for i in range(len(mark_list)):
        mark_list[i] = len(mark_list[i])

    for i in range(len(mark_list) - 1, -1, -1):
        if mark_list[i] == max(mark_list):
            chast_povtor = i
            break

    print(f'Часто повторяющаяся: {chast_povtor}')
    itog_mark_list.append(chast_povtor)

    itog_mark = sum(itog_mark_list) / len(itog_mark_list)
    print(f'Оценка: {itog_mark}')
    if (itog_mark * 10) % 10 == 5:
        itog_mark = round(itog_mark) + 1
        print(f'Итоговая оценка: {itog_mark}')
    else:
        itog_mark = round(itog_mark)
        print(f'Итоговая оценка: {itog_mark}')
    return itog_mark

tekyshaya_list = []
kolonka_list = []
q1 = count(tekyshaya_list, kolonka_list)
