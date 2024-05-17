nota = 85
#if nota >= 90:
   # print("Ótimo desempenho!")
#elif nota >= 70:
    #print("Bom desempenho.")
#else:
    #print("Melhorar na próxima.")


#nome = input('digite seu nome')
#idade = input('digite sua idade')
#curso = input('digite seu curso')
#numero = int(input('digite um numero'))


#print('é divisivel')

# ERCÍCIOS: 

# 1

# Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.
 
numero = int(input('digite um numero'))
if numero < 0:
    print('é negativo')
elif numero > 0:
    print('é positivo')
else:
    print(' é 0')





# 2

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.
idade =int(input('digite sua idade'))
if idade >=16:
    print('é pode votar')
else:

    print(' não pode votar')








# 3

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
n = 10
if n % 2 ==0:
    print('é par')
else:
    print('é impar')







# 4

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno
n1 = int(input(''))
n2 = int(input(''))
n3 = int(input(''))

if n1 == n2 == n3:
    print('equilatero')
elif n1 != n2 != n3: 
    print('isósceles')





# **Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.**


# 5

# Determine se um número é múltiplo de 5 e 7.




# 6

# Verifique se um número é positivo e maior que 10

n=10 
if n > 0 and n > 10:
     print('verdadeiro')
else:
     print('não é verdadeiro')






# 7

# Verifique se um número é divisível por 3 ou 5.
number = 15
if number % 5 or number % 3 ==0: 
    print('verdadeiro')
    




