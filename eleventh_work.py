space = int(input("Введите число: "))
for i in range(1,space+1):
    print(" " * space + "#" * i * 2)
    space -= 1
