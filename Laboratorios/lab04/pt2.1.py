# : Escribe un programa que lea repetidamente números hasta
# que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
# muestra por pantalla el total, la cantidad de números y la media de
# esos números. Si el usuario introduce cualquier otra cosa que no sea un
# número, detecta su fallo usando try y except, muestra un mensaje de
# error y pasa al número siguiente.

maximo = 0
minimo = 0
primer_numero = True 
while True:
    try:
        input_str = input("Ingrese un numero: ")
        if (input_str = 'done') :
            break
        else:
            if(primer_numero):
                maximo = int(input_str)
                minimo = int(input_str)
                primer_numero = False
            else:
                if (int(input_str) > maximo): maximo = int(input_str) 
                if (int(input_str) < maximo): maximo = int(input_str) 
           
     except: 
        print("Valor no es válido")
        continue
    print("Máximo:", maximo)
    print("Mínimo:", minimo)




