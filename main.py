# antecessor e sucessor 05
# antecessor e sucessor de outra maneira
"""
nu=int(input('digite um número'))
print('o antecessor é {} e o seu sucessor é {}'.format((nu-1),(nu+1)))"""


num=int(input('digite um número para ver seu antessessor e sucessor:'))
sub= num -1
som= num +1
print('O antecessor de {} é {}\nE o sucessor de {} é {}'.format(num, sub, num, som))

#  algoritmo 06

o=int(input('digite um número para saber seu dobro, triplo e raiz quadrada:'))
x= o*2
x1 = o*3
x2 = o**(1/2)
print('dobro de {} é {};\nO triplo de {} é {};\nA raiz quadrada de {} é {:.3f};'.format(o, x, o, x1, o, x2))

#média aritmética 07

nota1 = float(input('primeira nota do aluno:  '))
nota2 = float(input('segunda nota do aluno:   '))
média = (nota1+nota2)/2
print('a média do aluno é {}'.format(média))






# conversor de medidas 08

h = float(input('digite um número para converter em milímetros e centímetros:'))
h2 = h*100
h3 = h*1000
print('O valor em centímetros  de {} é {:.2};\nO valor de {} em milímetros é {:.2f};'.format(h, h2, h, h3))

# tabuada 09
J=int(input('digite um número inteiro para ver a sua tabuada:'))

s2 = J*2, J*3 , J*4, J*5, J*6, J*7, J*8, J*9

print('tabuada:\n',J,'= {}' .format(s2))

#carteira 10

v = float(input("Quantos reais você possuí em sua carteira?"))
r=v/5.35

print("você pode comprar U${}".format(r
                  ))
# Parede 11
print("informe a altura de suas paredes")

parede1=float(input("altura da sua parede"))
parede2=float(input("largura da parede"))
parede3=float(input("comprimento da parede"))

r2= parede1 * parede2 * parede3

print("você gastara {} litros de tinta para pintar.".format(r2))



#promoção 012

preço_inicial = float(input("qual o preço do produto que deseja comprar?"))
desconto = preço_inicial * 0.05
novo_valor = preço_inicial - desconto

print('Você recebeu um desconto de 5%!\n '
      'preço original:     R${}\ndesconto:       R${}\npreço total:      R${}'
      .format(preço_inicial, desconto, novo_valor))


#salário 013

seu_salario = float(input('Quanto você recebe?'))
aumento = seu_salario *  1.15
print('você ganhou um aumento de 15%, agora você recebe {} mês'.format(aumento))
