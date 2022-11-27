import random
import math

def wordle(lista):
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
        clue = ''.join(clue)
        return clue

    def cuvinteRamase(answer, clueAnswer, wordsLeft):
        cuvinte_ramase = []
        for cuv in wordsLeft:
            if procesDeGhicire(cuv, answer) == clueAnswer:
                cuvinte_ramase.append(cuv)
        return cuvinte_ramase

    def procesDeGhicireBot(answer, guess, I):
        clue = procesDeGhicire(answer, guess)
        if clue in I:
            I[clue] += 1
        else:
            I[clue] = 1
        return answer == guess

    word_list = []
    word_file = open("cuvinte.txt")
    for cuvant in word_file:
        word_list.append(cuvant.strip())
    word_file.close()
    cuvinte_ramase = lista

    cuvMax = ''

    EntropyMax = 0
    for cuv in word_list:
        I = {}
        for cuv2 in cuvinte_ramase:
            procesDeGhicireBot(cuv2, cuv, I)
        Entropy = 0
        for clue in I:
            p = I[clue] / len(cuvinte_ramase)
            Entropy += -p * math.log2(p)
        if Entropy > EntropyMax:
            cuvMax = cuv
            EntropyMax = Entropy
    if EntropyMax <= 1:
        print("Cuvantul optim e", cuvinte_ramase[0])
    else:
        print("Cuvantul optim e", cuvMax, EntropyMax)



    return lista

