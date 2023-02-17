from time import time

def time_random():
    return time() - float(str(time()).split('.')[0])

def gen_random_range(min,max):
    return int(time_random() * (max - min)+ min)

#Driver Code.
print(gen_random_range(10,6783))
