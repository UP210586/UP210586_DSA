import math

def prioridad(c):
    if c in ["+", "-"]:
        return int(1)
    elif c in ["*", "/"]:
        return int(2)
    elif c in ["sen", "cos", "tan", "arctan", "arccos", "arcsen", "log", "ln", "alog", "aln", "√"]:
        return int(3)
    elif c in ["^"]:
        return int(4)
    elif c in ["(", ")"]:
        return int(0)
def posfix(Q):
    op = {"+", "-", "/", "*", "^", "sen", "cos", "tan",
          "arctan", "arccos", "arcsen", "log", "ln", "alog", "aln","√"}
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
            j = S[-1]
            a = prioridad(i)
            b = prioridad(j)
            if b >= a:  # type:ignore
                P.append(j)
                S.pop()
            S.append(i)
        elif i == ")":
            j = S[-1]
            while j != "(":
                P.append(j)
                S.pop()
                j = S[-1]
            else:
                S.pop()
    return P
def Calculadora(P):
    op = {"+", "-", "/", "*", "^"}
    fnt = {"sen", "cos", "tan", "arctan", "arccos",
          "arcsen"}
    fnl = {"log", "ln", "alog", "aln","√"}
    P.append(")")
    Pila = []
    C = 0
    for i in P:
        if i != ")":
            if i not in op and i not in fnt and i not in fnl:
                Pila.append(float(i))
            elif i in op:
                B = Pila.pop()
                A = Pila.pop()
                if i == "+":
                    C = A+B
                elif i == "-":
                    C = A-B
                elif i == "*":
                    C = A*B
                elif i == "/":
                    C = A/B
                elif i == "^":
                    C = A**B
                Pila.append(C)
            elif i in fnt:
                A = Pila.pop()
                R=math.radians(A)
                if i == "sen":
                    C = math.sin(R)
                elif i == "cos":
                    C = math.cos(R) ##no copies
                elif i == "tan":
                    C = math.tan(R)
                elif i == "arctan":
                    C = math.atan(R)
                elif i == "arccos":
                    C = math.acos(R)
                elif i == "arcsen":
                    C = math.asin(R)
                Pila.append(C)
            elif i in fnl:
                A= Pila.pop()
                if i == "√":
                    C = math.sqrt(A)
                elif i == "log":
                    C = math.log10(A)
                elif i == "ln":
                    C = math.log(A)
                elif i == "aln":
                    C = math.e**(A)
                elif i == "alog":
                    C = 10**(A)
                Pila.append(C)
                    

    return float(C)

array = input("Ingresa la operación (separa por espacios cada término): ")
c = array.split()
print("El término en posfix es: ", posfix(c))
print("El resultado es: ", Calculadora((posfix(c))))
