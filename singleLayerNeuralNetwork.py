import os
import Perceptron
import string


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
p2 = Perceptron.Perceptron(26,"Italian")
p3 = Perceptron.Perceptron(26,"German")

dirs = []

for root, subdirs, files in os.walk(path):
    for file in files:
        if '.txt' in file:
            dirs.append(os.path.join(root,file))

order = [0,5,17,18,8,23,9,21,11,3,22,12,13,2,4,14,15,1,16,7,19,6,20,10]

for x in order:
    print(dirs[x])
    group = ""
    if "English" in dirs[x]:
        group = "English"
    if "Italian" in dirs[x]:
        group = "Italian"
    if "German" in dirs[x]:
        group = "German"
            
    with open(dirs[x], 'r') as f:
        text = f.read()

    letters = countLetters(text)

    # print(f"Group: {group}")
    # print(f"Results: ")
    
    print("TRAIN")
    p1.training(letters,group, 4.25)
    p2.training(letters,group, 1)
    p3.training(letters,group, 3.75)
    # print("TEST")
    # print(p1.testing(letters))
    # print(p2.testing(letters))
    # print(p3.testing(letters))


    

    
print("TESSSSSSSSSSSSSTING")


for root, subdirs, files in os.walk(path):
    group = root[5:]
    for file in files:
        if '.txt' in file:
            tmpPath = os.path.join(root,file)

            with open(tmpPath, 'r') as f:
                text = f.read()

            letters = countLetters(text)

            print(f"Group: {group}")
            print(f"Results: ")
    
            # print("TRAIN")
            # p1.training(letters,group, 23.4)
            # p2.training(letters,group, 23.4)
            # p3.training(letters,group, 23.4)
            print("TEST")
            print(p1.testing(letters))
            print(p2.testing(letters))
            print(p3.testing(letters))


while True:
    inp = input("TEXT: ")

    if inp.lower() == "exit":
        break

    let = countLetters(inp)

    print(p1.testing(let))
    print(p2.testing(let))
    print(p3.testing(let))

