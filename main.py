import random
import math

def getRandom():
    return random.uniform(0.0,1.0)

class Point:
    def __init__(self):
        self.first = getRandom()
        self.last = getRandom()
    
    def isInCircle(self):
        squaredFirst = self.first*self.first
        squaredLast = self.last*self.last
        d = math.sqrt(squaredFirst + squaredLast)
        return d<1
        
    
def estimate_pi():
    list = []
    total_count = 1000000
    for i in range(0,total_count):
        list.append(Point())
    in_circle_count = 0
    for p in list:
        if p.isInCircle(): in_circle_count +=1
    
    print(4 * in_circle_count / total_count)
    

estimate_pi()
