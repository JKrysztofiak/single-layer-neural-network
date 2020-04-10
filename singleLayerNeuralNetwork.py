import os

#TODO: Wczytanie pliku i konwersja na 26-elementowy wektor proporcji liter 
path = 'data'

for root, subdirs, files in os.walk(path):
    for file in files:
        if '.txt' in file:
            tmpPath = os.path.join(root,file)

            with open(tmpPath, 'r') as f:
                text = f.read()

            letters = {}

            for l in text:
                if ord(l) in range(ord('A'),ord('Z')+1) or ord(l) in range(ord('a'),ord('z')+1):
                    if l.lower() in letters:
                        letters[l.lower()]+=1
                    else:
                        letters[l.lower()] = 1
                


#TODO: Trenowanie perceptronu n do rozpoznawania tylko n-języka 