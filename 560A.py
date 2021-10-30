# Question
# https://codeforces.com/contest/560/problem/A

number = int(raw_input())
notas = map(int, raw_input().split())
notas.sort()
# initialization
maximo = 1000000
rest = 0
soma = 1
flag = True
i = number - 1
while(soma < maximo and flag): #while loop with condition
  rest = soma #initializing
  while(i >= 0): #second while
    rest = rest % notas[i]
    if(rest == 0):
      break #break case
    i=i-1
  else:
    if(rest != 0): #if rest!=0 flag = 0
      flag = False
    i = number - 1
  soma=soma+1

if(soma == maximo): #if equal print -1
  print -1
else:
  print soma - 1
