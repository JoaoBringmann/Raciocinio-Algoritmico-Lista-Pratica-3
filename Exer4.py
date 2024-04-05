sair = 0
total = 0
num = 0
while sair == 0:
 idade = int(input("Digite uma idade ou Digite 0 para sair"))
 if idade == 0:
  print("Encerrando")
  sair = 1
  break
 else:
  total += idade
  num += 1
  result = total/num
print(result)