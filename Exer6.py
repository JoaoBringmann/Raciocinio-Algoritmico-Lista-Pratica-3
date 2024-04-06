incluidos = 0
rejeitados = 0
lista = []
for i in range(0,10):
    num = int(input("Digite um Numero Inteiro"))
    if 10 <= num <= 20:
        incluidos += 1
    else:
        rejeitados += 1

print(f"{incluidos} numeros foram digitados entre 10 e 20 e {rejeitados} não foram")
    
