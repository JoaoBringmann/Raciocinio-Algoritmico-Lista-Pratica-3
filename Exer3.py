num = int(input("Digite um numero inteiro entre 1-10"))
for i in range(1,11):
    if num < 1 or num > 10:
        print("Numero invalido")
        break
    else:
        result = num * i 
        print(result)