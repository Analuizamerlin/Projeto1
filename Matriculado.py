with open('./nomes.txt','r') as reader:
   arquivo = reader.readlines()

k = 0
i = 0

n = int(input("Pressione: \n 1 - Para consultar aluno matriculado \n 2 - Cadastrar novo aluno \n \n"))

if n == 1:
  
   nome = input("\nInsira nome completo: ")
   nome = nome.lower()

   for line in arquivo:
      line = line.lower()
      i= i +1
      if nome in line:
         print("\n", line, "foi o",i,"° matriculado na turma 1 do curso de Pontapé Inicial Desenvolvedor Python!\n")
         k=k+1
   if k == 0:
      print("\n",nome,"não está matriculado na turma 1 do curso de Pontapé Inicial Desenvolvedor Python!\n")

if n == 2:
   with open('./nomes.txt','a') as arquivo:
      arquivo.write = input("Insira nome completo do novo aluno: ")
      arquivo.close()
      with open('./nomes.txt','r') as reader:
         arquivo = reader.readlines()

      for line in arquivo:
         print(line)
      
      

      
