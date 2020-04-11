import os
import Perceptron
import string
import random
from random import randint
import tkinter as tk


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

def testLayer(data: list) -> str:
    res = {}

    for perc in perceptrons:
        res[perc.group] = perc.testing(data)

    result = perceptrons[0].group
    max = res[perceptrons[0].group]
    for key in res:
        if res[key] > max:
            result = key
            max = res[key]

    return result


def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")

    letters = countLetters(inputValue)

    label.config(text=testLayer(letters))




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
weights = [randint(-10,10) for x in range(0,26)]
t = randint(-5,5)
for g in groups:
    # perceptrons.append(Perceptron.Perceptron(26,g))
    perceptrons.append(Perceptron.Perceptron(weights, t, g))

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
        per.training(letters, group, 0.6)

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


root=tk.Tk(className="Language Classificator")

root.geometry("500x500")

textBox=tk.Text(root, height=2, width=10)
textBox.pack(fill=tk.BOTH, expand=1)

buttonCommit=tk.Button(root, height=1, width=10, text="TEST", 
                    command=lambda: retrieve_input())
buttonCommit.pack(side=tk.BOTTOM)
label = tk.Label(root, text="")
label.pack()


tk.mainloop()