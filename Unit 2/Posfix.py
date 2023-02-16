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
Q = ["5", "*", "(", "6", "+", "2", ")", "-", "12", "/", "4"]
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
        for j in reversed(S):
            a = prioridad(i)
            b = prioridad(j)
            print(a, b)
