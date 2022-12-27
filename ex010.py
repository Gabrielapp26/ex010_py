#Desafio 09
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento 
print("Digite o seu atual salário para saber quanto vai ser o seu salário com aumento")
sa = int(input("Salário atual: "))
sca = sa + (sa * 15 / 100)
print("Com o aumento de 15% o seu salário agora é de {} reais".format(sca))