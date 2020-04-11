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

    wp = w.copy()
    xp = x.copy()

    wp.append(t)
    xp.append(-1)

    w_prim = add_vectors(wp, (multiply_vector(xp,((d-y)*alfa))))

    return w_prim

        
class Perceptron:
    # def __init__(self, k: int, group: str):
    #     self.weights = [randint(-10,10) for x in range(0,k)]
    #     self.t = randint(-10,10)
    #     self.group = group

    def __init__(self, w: list, t: float, group: str):
        self.weights = w.copy()
        self.t = t
        self.group = group
    
    def training(self, trainSet: list, trueRes: str, alfa: float):

        # net = calculate_net(self.weights, trainSet)
        net = calculate_net(multiply_vector(self.weights, (1.0/vector_length(self.weights))),multiply_vector(trainSet, (1.0/vector_length(trainSet))))

        res = 0
        if net > self.t:
            res = 1

        # print(f"{self.group}: {res}")
        # print(f"TrueRes: {trueRes} Perceptron: {self.group} res: {res}")

        
        i=0

        while (res == 0 and trueRes == self.group) or (res == 1 and trueRes != self.group):
                        
            # uczenie
            # print(f"UCZENIE {i}")
            # i+=1

            d = 1
            y = 0
            if res == 1:
                d = 0
                y = 1

            # wprim = delta_rule(self.weights, d, y, alfa, trainSet, self.t)
            wprim = delta_rule(multiply_vector(self.weights, (1.0/vector_length(self.weights))), d, y, alfa, multiply_vector(trainSet, (1.0/vector_length(trainSet))), self.t)          
            
            self.t = float(wprim[-1])
            self.weights = wprim[:-1]

            

            # net = calculate_net(self.weights, trainSet)
            net = calculate_net(multiply_vector(self.weights, (1.0/vector_length(self.weights))),multiply_vector(trainSet, (1.0/vector_length(trainSet))))

            res = 0
            if net > self.t:
                res = 1
            

    def testing(self, testSet: list) -> int:
        net = calculate_net(multiply_vector(self.weights, (1.0/vector_length(self.weights))),multiply_vector(testSet, (1.0/vector_length(testSet))))
        # net = calculate_net(self.weights,testSet)

        res = 0
        if net > self.t:
            res = 1

        # return net
        return res