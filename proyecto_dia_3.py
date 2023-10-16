#text = str(input("Ingrese un texto para procesar:"))
text = """Bueno, el tercer día no ha dejado nada que desear. Hemos visto muchas cosas y de las buenas, 
y ha llegado la hora de juntar todo lo python aprendido y ponerlo en práctica, creando un programa 
perfectamente funcional desde cero python."""

text_upper = text.upper()

letters = []

for i in range(3):
    l = str(input("Ingrese 3 letras:"))
    letters.append(l.upper())

# 1 
print("\n     Primero: ¿cuántas veces aparece cada una de las letras que eligió?")
print("Las letras elegidas por el usuario: " + str(letters))

print(f"La letra {letters[0]} aparece {text_upper.count(letters[0])} vez/veces.")
print(f"La letra {letters[1]} aparece {text_upper.count(letters[1])} vez/veces.")
print(f"La letra {letters[2]} aparece {text_upper.count(letters[2])} vez/veces.")

# 2
print("\n     Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto")
text_split = text.split()
print(f"El texto contiene {len(text_split)} palabras.")

# 3
print("\n     Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última.")
print(f"La primer letra del texto es {text[0]}")

if text[-1] == ".":
    print(f"La última letra del texto es {text[-2]}")
else:
    print(f"La última letra del texto es {text[-1]}")

# 4
print("""\n     Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de 
las palabras.""")
text_reverse = text_split
text_reverse.reverse()

print(" ".join(text_reverse))

# 5
print("""\n     Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del 
texto.""")
if (text_upper.count("PYTHON".upper())) > 0:
    print('La palabra "Python" se encuentra en el texto.')
else:
    print('La palabra "Python" NO se encuentra en el texto.')