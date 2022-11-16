# Python je keysensitive "Python" != "python"

# 5 + 5 = sčítání
# 6 - 4 = odčítání
# 8 * 9 = násobení
# 8 / 8 = dělení
# 7 // 2 = celočíselné dělení
# 7 % 2 = zbytek po dělení
# 8 ** 2 = mocnina
# 32 ** (1/5) = odmocnina


promenna = "Tohle je hodnota proměnné"
Promenna = "Tohle je hodnota proměnné"
# znovu promenna != Promenna
# proměnné v pythonu mají dinamický datový typ

x, y, z = 1, 2, 3
# definice více proměnných najednou

str()
int()
float()
bool()

print(type(promenna))  # zjištění datového typu proměnné = datový typ
print(isinstance(promenna, int))  # zjištění daového typu proměnné = true/false

i = 2.5
int(i)  # vrátí 2
round(i, 0)  # vrátí 3

bool()  # True | False

float = 1  # proměnná nesmí být pojmenována klíčovými slovy, nebo názvi funkcí

velikost = 1  # definování
velikost == 1  # porovnávání
velikost < 2
velikost > 1  # (1, 00)
velikost >= 1  # <1, 00)


print(
    "Ahoj " +
    "světe!"
)

print(
    """
    výceřádkový
    výpis
    """
)

"""
dá se využít
i jako výceřádková
poznámka
"""

vstup = input("Co je:")
print(vstup)

print("zadej něco")
vstup = input("->")

print("zadal jsi:" + vstup)
print("zadal jsi:", vstup, ":-)", sep="#")

print("#" * 10)

bod, x, y = "A", 100, 200
print("bod " + bod + " se nachází na souřadnicých [" + str(x) + " , " + str(y) + "]")
print("bod {} se nachází na souřadnicých [{}, {}]".format(bod, x, y))
print("bod {0} se nachází na souřadnicých [{2}, {1}]".format(bod, y, x))
print("bod {a} se nachází na souřadnicých [{b} , {c}]".format(
                                                            a=bod,
                                                            b=x,
                                                            c=y
                                                        ))
print(f"bod {bod} se nachází na souřadnicých [{x}, {y}]")

if bod == "A":
    pass
elif bod == "B":
    pass
else:
    pass

#################################
# ----------  cykli ----------- #
#################################

for i in range(10):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1  # nebo i = i + 1


samohlasky = 0
souhlasky = 0
cisla = 0
ostatni_znaky = 0

vstup = input("->")
for znak in vstup:
    if znak in "aeiouy":
        samohlasky += 1
    elif znak in "qwrtzpsdfghjklxcvbnm":
        souhlasky += 1
    elif znak in "0123456789":
        cisla += 1
    else:
        ostatni_znaky += 1
print(f"Slovo {vstup} má {souhlasky} souhlásek")
print(f"Slovo {vstup} má {samohlasky} samohlásek")
print(f"Slovo {vstup} má {cisla} čísel")
print(f"Slovo {vstup} má {ostatni_znaky} ostatních znaků")

