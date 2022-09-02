# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

print('X Y Z\t¬(X ⋁ Y ⋁ Z)\t¬X ⋀ ¬Y ⋀ ¬Z\t==')
for X in [False,True]:
    for Y in [False, True]:
        for Z in [False, True]:
            # Красиво все печатаем
            print(f'{int(X)} {int(Y)} {int(Z)}\t\t  '\
                  f'{int(not(X or Y or Z))}\t\t\t\t  '\
                  f'{int(not(X) and not(Y) and not(Z))}\t\t\t '\
                  f'{int(not(X or Y or Z) == (not(X) and not(Y) and not(Z)))}')
