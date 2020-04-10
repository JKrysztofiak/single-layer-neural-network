from random import randint
import math

def vector_length(v: list) -> float:
    value = 0
    for x in v:
        value+=pow(x,2)
    return math.sqrt(value)

def multiply_vector(v: list, m: float) -> list:
    res = []
    for value in v:
        res.append(float(value)*m)
    return res

def add_vectors(v1: list,v2: list) -> list:
    res = []
    for i in range(0,len(v1)):
        res.append(float(v1[i])+float(v2[i]))

    return res


def calculate_net(w: list, p: list) -> float:
    res = 0
    for i in range(0,len(w)):
        res += float(p[i])*float(w[i])

    return res


def delta_rule(w: list, d: int, y: int, alfa: float, x: list, t: float) -> list:
    
    w.append(t)
    x.append(-1)

    w_prim = add_vectors(w, (multiply_vector(x,((d-y)*alfa))))

    return w_prim

        
class Perceptron:
    def __init__(self, k: int, group: str):
        self.weights = [randint(-5,5) for x in range(0,k)]
        self.t = randint(-5,5)
        self.group = group

    
    def training(self, trainSet: list, trueRes: str, alfa: float):
        net = calculate_net(self.weights, trainSet)

        res = 0
        if net > self.t:
            res = 1

        # print(f"{self.group}: {res}")
        # print(f"TrueRes: {trueRes} Perceptron: {self.group} res: {res}")

        if res == 0 and trueRes == self.group:
            #uczenie
            wprim = delta_rule(self.weights, 1, 0, alfa, trainSet, self.t)
            self.t = float(wprim[-1])
            self.weights = wprim[:-1]
            return
            
        
        if res == 1 and trueRes != self.group:
            #uczenie
            wprim = delta_rule(self.weights, 0, 1, alfa, trainSet, self.t)
            self.t = float(wprim[-1])
            self.weights = wprim[:-1]
            return


    def testing(self, testSet: list) -> int:
        net = calculate_net(multiply_vector(self.weights, (1.0/vector_length(self.weights))),multiply_vector(testSet, (1.0/vector_length(testSet))))
        return net
        
        
