file = open('nomes.txt', 'r')
lines = file.readlines()
file.close()

k = 0
i = 0

n = int(input("Pressione: \n 1 - Para consultar aluno matriculado \n 2 - Cadastrar novo aluno \n \n"))

if n == 1:
  
   nome = input("\nInsira nome completo: ")
   nome = nome.lower()

   for min in lines:
      min = min.lower()
      i= i +1
      if nome in min:
         print("\n", min, "foi o",i,"° matriculado na turma 1 do curso de Pontapé Inicial Desenvolvedor Python!\n")
         k=k+1
   if k == 0:
      print("\n",nome,"não está matriculado na turma 1 do curso de Pontapé Inicial Desenvolvedor Python!\n")

if n == 2:
   novo = input("Insira o nome completo do novo aluno: ")
   lines.insert(len(lines)+1,"\n" + novo)

   file = open('nomes.txt', 'w')
   file.writelines(lines)
   file.close()
