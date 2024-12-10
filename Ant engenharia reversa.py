import random

with open('código.txt', 'r') as arquivo:
    código = arquivo.read()

nomes = input("Digite o nome de todas as variáveis, instâncias de objeto etc. de seu código separadas por espaço: ")
nomes = nomes.split()
z = ""
nomes_alterados = []
for x in range(len(nomes)):
    for y in range(0,20):
        z = z + str(random.randint(1000,2000))
    z = "a" + z
    nomes_alterados.append(z)


pos = - 1
for code in nomes:
    pos = pos + 1
    código.replace(nomes[pos], nomes_alterados[pos])

with open("código.txt", "w") as arquivo:
    arquivo.write(código)
