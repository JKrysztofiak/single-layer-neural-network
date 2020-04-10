import os
import Perceptron
import string



#TODO: Wczytanie pliku i konwersja na 26-elementowy wektor proporcji liter 

def countLetters(text: str) -> list:
    
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    for l in text:
        if l.lower() in letter_count:
            letter_count[l.lower()]+=1

    letters = [] 
    for key in sorted(letter_count):
        letters.append(letter_count[key])

    return letters



path = 'data'

p1 = Perceptron.Perceptron(26,"English")


for root, subdirs, files in os.walk(path):
    group = root[5:]
    for file in files:
        if '.txt' in file:
            tmpPath = os.path.join(root,file)

            with open(tmpPath, 'r') as f:
                text = f.read()

            letters = countLetters(text)
    
            p1.training(letters,group, 0.25)



#TODO: Trenowanie perceptronu n do rozpoznawania tylko n-języka 