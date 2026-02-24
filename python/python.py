import random

n1=input("digite o nome de quem sera sorteado: ")
n2 = input ("digite outro nome: ")
n3 = input("digite mais outro nome:")
n4 = input("digite mais um: ")
lista = [n1, n2, n3, n4]
num = str(random.choice(lista))
print ("a pessoa sorteada foi: ", num,)