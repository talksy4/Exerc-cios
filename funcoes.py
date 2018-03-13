"""Escreva uma função para imprimir “n” linhas, de acordo com o esquema a seguir:
  *
  ** """
def imprime_linhas(n):
  for i in range (1,n+1):
    for j in range (1,i+1):
      print ("*", end=" ")
    print ()

#programa principal
n = int(input("Digite o numero a ser impresso: "))
print(imprime_linhas(n))

"""Escreva uma função que receba um tempo em “segundos” e converta para “hora, minuto e segundo”. Também escreva um programa para testar essa função."""
def conver_temp(s):
  h=3600//s
  m=s//60
  s==s
  return (h,m,s)

#progrma princiapl
s=int(input("Segundos para conversao em horas, minutos e segundos(?):"))
print (conver_temp(s))

"""Escreva uma função para inverter um número inteiro. Exemplo: 326  623. Também
escreva um programa para testar essa função."""

def inverter(n):
  n=str(n)
  n=n[::-1]
  return n

#progrma principal
n=int(input("número:"))
print (inverter(n))
  
  
"""Escreva uma função que receba uma data (dia, mês e ano) e gere a string: “dia de mês por extenso e ano”."""
def data(dia, mes, ano):
	meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	meses= meses[mes-1]
	return meses
	
#progrma principal
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
print("Data: dia", dia, "de", data(dia,mes,ano), ano)

  
"""5. Escreva uma função para receber um valor inteiro e retornar a quantidade de cédulas de:
100, 50, 20, 10, 5, 2 e 1."""
def qtd_cel(v):
  n1=v//100
  n2=v%100//50
  n3=v%50//20
  n4=v%100%50%20//10
  n5=v%100%50%20%10//5
  n6=v%100%50%20%10%5//2
  m1=v%100%50%20%10%5%2//1
  notas=[n1,n2,n3,n4,n5,n6,m1] 
  return notas

#pp
v=int(input("valor:"))
print (qtd_cel(v))


"""6. Crie funções para receberem uma lista de números, calcular e retornarem:
a. Maior valor;
b. Menor valor;
c. Média dos números;
d. Valor mais próximo da média;
e. Quantidade números vizinhos iguais."""

def 

  