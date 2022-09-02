# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

wod_s = input("Введите номер дня недели [1..7]: ")
if not wod_s.isdigit():
    print("Ошибка. Введено не натуральное число!")
    exit(-1)
wod_i = int(wod_s)
if not (1 <= wod_i <= 7):
    print("Ошибка. Введен неверный номер дня недели")
    exit(-1)
if wod_i > 5:
    print("Это выходной!")
else:
    print("Это будний день")