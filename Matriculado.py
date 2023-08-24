with open('./nomes.txt','r') as reader:
   arquivo = reader.readlines()

k = 0

nome = input("Nome completo: ")
for line in arquivo:
   line2 = line.lower()
   nome2 = nome.lower()
   if nome2 in line2:
      print("Você está matriculado!")
      k=k+1
if k == 0:
   print("Você não está matriculado!")