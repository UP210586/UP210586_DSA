secret_number = 777
print(
"""
+====================+
| Welcome to my game |
+====================+
""")
i=1
x=int(input("¿Cuál crees que sea el número? "))
while x != secret_number:
    i+=1
    if x<secret_number:
        print("Subele")
        x=int(input("Intenta de nuevo "))
    else:
        print("Bajale")
        x=int(input("Intenta de nuevo "))


print("Bingo")
print("Lo lograste en ",i," intentos.")