import os
import Perceptron
import string
import random


def countLetters(text: str) -> list:
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    allLetters = 0
    for l in text:
        if l.lower() in letter_count:
            letter_count[l.lower()]+=1
            allLetters +=1 

    letters = [] 
    for key in sorted(letter_count):
        letters.append(letter_count[key]/allLetters)

    return letters





path = 'data'

dirs = []
groups = []

for root, subdirs, files in os.walk(path):
    if root[5:] not in groups and root[5:]!="":
        groups.append(root[5:])
    for file in files:
        if '.txt' in file:
            dirs.append(os.path.join(root,file))

perceptrons = []
for g in groups:
    perceptrons.append(Perceptron.Perceptron(26,g))

random.shuffle(dirs)

for file in dirs:
    group = ""
    for g in groups:
        if g in file:
            group = g

    print(file, "is group: "+group)
            
    with open(file, 'r') as f:
        text = f.read()

    letters = countLetters(text)

    for per in perceptrons:
        per.training(letters, group, 0.5)

    for per in perceptrons:
        print(f"{per.group}: ",per.testing(letters))

   

print("###############@@@@@@@@@@@@@@@@@@@@@@##################@@@@@@@@@@@@@@@@@###########")

for root, subdirs, files in os.walk(path):
    group = root[5:]
    for file in files:
        if '.txt' in file:
            tmpPath = os.path.join(root,file)

            with open(tmpPath, 'r') as f:
                text = f.read()

            letters = countLetters(text)

            print("TO TEST: ",group)
            for p in perceptrons:
                print(p.group,": ", p.testing(letters))

            
            # res = {}
            # res[p1.group] = p1.testing(letters)
            # res[p2.group] = p2.testing(letters)
            # res[p3.group] = p3.testing(letters)

            # result = p1.group
            # max = res[p1.group]
            # for key in res:
            #     if res[key] > max:
            #         result = key
            #         max = res[key]

            # print("ODP: ",result)
            # print("###")




# while True:
#     inp = input("TEXT: ")

#     if inp.lower() == "exit":
#         break

#     let = countLetters(inp)

#     print(p1.testing(let))
#     print(p2.testing(let))
#     print(p3.testing(let))

