print("Learn Random Modules")
"""
print(dir(random))
'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'

randint-Fun = Take Interval (Start,Stop) ==> Return Integers
random-Fun = default interval (0,1) ==> Return Floating-point number

"""
import random

Random_Num = random.randint(1,10)
print(Random_Num)

Rand = round(random.random()*100)
print(Rand)

List = ["Nishanth", "Vasee", "Surya"]
C = random.choice(List)
print(f"This is Great Hacker {C}")
