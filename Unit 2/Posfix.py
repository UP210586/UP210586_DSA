def prioridad(c):
    if c in ["+", "-"]:
        return int(1)
    elif c in ["*", "/"]:
        return int(2)
    elif c in ["^"]:
        return int(3)
    elif c in ["(", ")"]:
        return int(0)


op = {"+", "-", "/", "*", "^"}
Q = ["A","+","(","B","*","C","-","(","D","/","E","^","F",")","*","G",")","*","H"]

S = []
P = []
Q.insert(0, "(")
Q.append(")")

for i in Q:
    if i != "(" and i != ")" and i not in op:
        P.append(i)
    elif i == "(":
        S.append(i)
    elif i in op:
        j=S[-1] 
        a = prioridad(i)
        b = prioridad(j)
        if b>=a:
            P.append(j)
            S.pop()
        S.append(i)    
    elif i == ")":
        j=S[-1]
        while j !="(":
            P.append(j)
            S.pop()
            j=S[-1]
        else:
            S.pop()
print(P)
            
