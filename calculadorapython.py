#nome da calculadora
print('BEM-VINDO A CALCULADORA DO ARGO')

#dados
n = input('Digite seu nome: ')
print('Muito Obrigado por usar a minha calculadora, {}.'.format(n))

#variaveis
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

#resultado das contas
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
rd = n1 % n2

#resultado
print('A soma dos valores {} e {}, é igual a {}'.format(n1, n2, s))
print('A diferença dos valores {} e {} é {}'.format(n1, n2, su))
print('A multiplicação dos valores {} e {} é {}'.format(n1, n2, m))
print('A divisão dos valores {} e {} é {}'.format(n1, n2, d))
print('A divisão inteira dos valores {} e {} é {}'.format(n1, n2, di))
print('A potência de {} elevado a {} é {}'.format(n1, n2, p))
print('O resto da divisão dos valores {} e {} é {}'.format(n1, n2, rd))

#agradecimentos
print('Bons Estudos, {}.'.format(n))

