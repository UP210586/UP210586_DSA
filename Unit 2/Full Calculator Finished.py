import tkinter as tk
import math

calculation = ""

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

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def posfix(Q):
    op = {"+", "-", "/", "*", "^", "sen", "cos", "tan",
          "arctan", "arccos", "arcsen", "log", "ln", "alog", "aln","√"}
    S = []
    P = []
    if Q[0]== "-":
        Q.insert(0,0)
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
    fnt = {"sen", "cos", "tan", "arctan", "arccos","arcsen"}
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
                if i == "sen":
                    R=math.radians(A)
                    C = math.sin(R)
                elif i == "cos":
                    R=math.radians(A)
                    C = math.cos(R)
                elif i == "tan":
                    R=math.radians(A)
                    C = math.tan(R)
                elif i == "arctan":
                    C = math.degrees(math.atan(A))
                elif i == "arccos":
                    C = math.degrees(math.acos(A))
                elif i == "arcsen":
                    C = math.degrees(math.asin(A))
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

def evaluate_calculation(calcu):
    c = calcu.split()
    print("El término en posfix es: ",posfix(c))
    result = Calculadora(posfix(c))
    print("El resultado es: ", result)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, result)#type:ignore
    

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("370x400")

text_result = tk.Text(root, height=2, width=20, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=7, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=7, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=7, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=7, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=7, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=7, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=7, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=7, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=7, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=7, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation(" + "), width=7, font=("Arial", 14))
btn_plus.grid(row=3, column=4)
btn_minus = tk.Button(root, text=" - ", command=lambda: add_to_calculation(" - "), width=7, font=("Arial", 14))
btn_minus.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation(" / "), width=7, font=("Arial", 14))
btn_div.grid(row=5, column=4)
btn_mult = tk.Button(root, text="*", command=lambda: add_to_calculation(" * "), width=7, font=("Arial", 14))
btn_mult.grid(row=6, column=4)
btn_ele = tk.Button(root, text="^", command=lambda: add_to_calculation(" ^ "), width=7, font=("Arial", 14))
btn_ele.grid(row=7, column=4)
btn_roo = tk.Button(root, text="√", command=lambda: add_to_calculation(" √ "), width=7, font=("Arial", 14))
btn_roo.grid(row=8, column=4)
btn_roo = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=7, font=("Arial", 14))
btn_roo.grid(row=8, column=3)
btn_ipar = tk.Button(root, text="(", command=lambda: add_to_calculation(" ( "), width=7, font=("Arial", 14))
btn_ipar.grid(row=5, column=1)
btn_fpar = tk.Button(root, text=")", command=lambda: add_to_calculation(" ) "), width=7, font=("Arial", 14))
btn_fpar.grid(row=5, column=3)
btn_sen = tk.Button(root, text="sen", command=lambda: add_to_calculation(" sen "), width=7, font=("Arial", 14))
btn_sen.grid(row=6, column=1)
btn_cos = tk.Button(root, text="cos", command=lambda: add_to_calculation(" cos "), width=7, font=("Arial", 14))
btn_cos.grid(row=6, column=2)
btn_tan = tk.Button(root, text="tan", command=lambda: add_to_calculation(" tan "), width=7, font=("Arial", 14))
btn_tan.grid(row=6, column=3)
btn_atan = tk.Button(root, text="arcsen", command=lambda: add_to_calculation(" arcsen "), width=7, font=("Arial", 14))
btn_atan.grid(row=7, column=1)
btn_acos = tk.Button(root, text="arccos", command=lambda: add_to_calculation(" arccos "), width=7, font=("Arial", 14))
btn_acos.grid(row=7, column=2)
btn_asen = tk.Button(root, text="arctan", command=lambda: add_to_calculation(" arctan "), width=7, font=("Arial", 14))
btn_asen.grid(row=7, column=3)
btn_asen = tk.Button(root, text="log", command=lambda: add_to_calculation(" log "), width=7, font=("Arial", 14))
btn_asen.grid(row=8, column=1)
btn_asen = tk.Button(root, text="ln", command=lambda: add_to_calculation(" ln "), width=7, font=("Arial", 14))
btn_asen.grid(row=8, column=2)
btn_asen = tk.Button(root, text="alog", command=lambda: add_to_calculation(" alog "), width=7, font=("Arial", 14))
btn_asen.grid(row=9, column=1)
btn_asen = tk.Button(root, text="aln", command=lambda: add_to_calculation(" aln "), width=7, font=("Arial", 14))
btn_asen.grid(row=9, column=2)
btn_res = tk.Button(root, text="=", command=lambda: evaluate_calculation(calculation), width=15, font=("Arial", 14))
btn_res.grid(row=9, column=3, columnspan=2, rowspan=1)
btn_clear = tk.Button(root, text="C", command=lambda: clear_field(), width=7, font=("Arial", 14), )
btn_clear.grid(row=2    , column=4)

root.mainloop()