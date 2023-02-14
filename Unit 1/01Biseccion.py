
def a(x1, x2):
    es = .001
    er = abs(x1-x2)
    while (er>es):
        xn = ((x1 + x2) / 2)
        if (x1*xn < 0):
            x2 = xn
        else:
            x1 = xn
        return xn

print('El valor de xn = ', a(4., 7.))