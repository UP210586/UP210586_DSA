import random
lista=[]
def randomlist(rL):    
    rL=[]
    for i in range(100):
        r=random.randint(101,500)
        if r not in rL:
            rL.append(r)
    print(rL)
    return(rL)
   
print(randomlist(lista))
