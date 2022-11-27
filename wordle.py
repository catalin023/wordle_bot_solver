import random
import bot_wordle

def procesDeGhicire(answer, guess):
    d = {}
    for litera in answer:
        if litera in d:
            d[litera] += 1
        else:
            d[litera] = 1
    position = 0
    clue = ["0", "0", "0", "0", "0"]
    for litera in guess:
        if litera == answer[position]:
            clue[position] = "1"
            d[litera] -= 1
        position += 1
    position = 0
    for litera in guess:
        if litera in answer and d[litera] and clue[position]!="1":
            clue[position] = '2'
            d[litera] -= 1
        position += 1
    return clue

def cuvinteRamase(answer, clueAnswer, wordsLeft):
    cuvinte_ramase = []
    for cuv in wordsLeft:
        if procesDeGhicire(cuv, answer) == clueAnswer:
            cuvinte_ramase.append(cuv)
    return cuvinte_ramase

word_list = []
word_file = open("cuvinte.txt")
for cuvant in word_file:
    word_list.append(cuvant.strip())
word_file.close()
lista = word_list

#alegerea cuvantului
raspuns = random.choice(word_list)
print(raspuns)
num_de_incercari = 0
clue = ["0", "0", "0", "0", "0"]

while clue != ["1", "1", "1", "1", "1"]:
    if num_de_incercari == 0:
        print("Cuvantul optim e TAREI 6.413805505806508")
    else:
        bot_wordle.wordle(lista)
    ghicit = input("Introdu un cuvant\n")
    ghicit = ghicit.upper()
    if ghicit in word_list:
        num_de_incercari += 1
        clue = procesDeGhicire(raspuns, ghicit)
        print(clue)
        lista = cuvinteRamase(ghicit, clue, lista)
    else:
        print("Cuvantul nu este in lista")


print("Felicitari! Ai ghicit cuvantul in ", num_de_incercari, "incercari")
