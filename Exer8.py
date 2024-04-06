num = int(input("Digite um numero positivo: "))
if num < 0:
    print("Numero invalido")
else:
    print("Divisores de", num, ":")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)