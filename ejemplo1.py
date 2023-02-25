#Represa Hifroituango

#Entradas
levelWater = float(input("Digite el nivel del agua: "))

#Procesos 
if levelWater>=0 and levelWater <= 250:
    print(f"El sensor marca: {levelWater}, muy bajo...")
elif levelWater > 250 and levelWater <=400:
    print(f"El sensor marca: {levelWater}, Aceptable")
else:
     print(f"El sensor marca: peligrooooooo")

