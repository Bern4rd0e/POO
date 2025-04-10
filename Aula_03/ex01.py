# x = 1

# while x <= 10:
#     print(x, end = " ")
#     x += 1

# for x in range(1, 11):
#     print(x, end = " ")

# def funcao_recursiva(num, x):
#     print(num)
#     if num <= x:
#         return funcao_recursiva(num + 1, x)

# funcao_recursiva(0, 10)



def funcao_recursiva_2(lista, i=0):
    if i == len(lista):
        return 0
    else:
        if lista[i] >= i:
            print(i)
            return funcao_recursiva_2(lista, i + 1)

funcao_recursiva_2([10, 20, 10])