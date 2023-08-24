with open('./nomes.txt','r') as reader:
   arquivo = reader.readlines()

k = 0
i = 0

nome = input("Nome completo: ")
nome = nome.lower()

for line in arquivo:
   line = line.lower()
   i= i +1
   if nome in line:
      print("Você foi o",i,"° matriculado na turma 1 do curso de Pontapé Inicial Desenvolvedor Python!")
      k=k+1

if k == 0:
   print("Você não está matriculado na turma 1 do curso de Pontapé Inicial Desenvolvedor Python!")