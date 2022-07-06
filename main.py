import heapq
l = [int(l) for l in input("Введіть елементи списку:").split(",")]
if len(l) >= 6:
    print("Ваш список: ", l)
    print("5 найменших елементів вашого списку: ", heapq.nsmallest(5, l))
else:
    print("Список має містити більше п'яти елементів!")
