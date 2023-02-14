op = {"+", "-", "/", "*"}
P = [5, 6, 2, "+", "*", 12, 4, "/", "-"]
P.append(")")
Pila = []
C = 0

for i in P:
      if i !=")":
            if i not in op:
                  Pila.append(i)
            else:
                  B = Pila.pop()
                  A = Pila.pop()
                  if i == "+":
                        C = A+B
                  elif i == "-":
                        C = A-B
                  elif i == "*":
                        C = A*B
                  else:
                        C = A/B

                  Pila.append(C)
      else:
            print(C)