import random
Etapas = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#Paso 1.
#4Bueno estamos ordanenando ahora. dejara de tener sentido los apuntes jeje.....................
fin_del_juego = False
word_list = ["oso hormiguero", "babuino", "camello", "jirafa", "mula", "burro", "vaca", "rinoceronte"]
palabra_elegida = random.choice(word_list)
palabra_longitud = len(palabra_elegida)
#TODO-1 - Elija aleatoriamente una palabra de la lista de palabras y asígnela a una variable llamada palabra_elegida.
#TODO-2 - Pide al usuario que adivine una letra y asigne su respuesta a una variable llamada adivinar. Hacer conjetura en minúsculas.
# adivinar = input("Adivina la letra").lower()
#TODO-3 - Comprobar si la letra que el usuario adivinó (adivinar) es una de las letras de la palabra_elegida.
# for palabra in palabra_elegida:
 #   if palabra == adivinar:
     #   print("correcto!") 
   # else:
       # print("error!")
#Código de prueba - uniendo paso 1 (3 pasos) y paso 2(3)
#4.......................................................................
vidas = 6
#TODO-1: - Crear una Lista vacía llamada display.
#Para cada letra en la palabra_elegida, agregue un "_" a 'mostrar'.
#Entonces, si la palabra_elegida era "manzana", la pantalla debería ser ["_", "_", "_", "_", "_"] con 5 "_" representando cada letra para adivinar.
#display = []
#for letra in palabra_elegida:
#    display += "_"
#print(display)
#por lo general estaria bien este modo, si es que no habria pasos extras
# por eso usaremos range pues más adelante queremos saber posiciones, solo por si acaso. 
#4 ......................................................................
display = []
for _ in range(palabra_longitud):
    display += "_"
#print(display)
#fin_del_juego = False
while not fin_del_juego:
    adivinar = input("Adivina la letra\n").lower()

#TODO-2: - Pasa por cada posición en la palabra_elegida;
#Si la letra en esa posición coincide con 'adivinar', revele esa letra en la pantalla en esa posición.
#p.ej. Si el usuario adivinó "p" y la palabra elegida fue "manzana", la pantalla debería ser ["_", "p", "p", "_", "_"].
#4....................................................................... 
    #hemos elegido esta forma porque necesitamos las posiciones de las letras se cumplan
    #recordemos que esto es un bucle con limite. empieza por 0 1 2 .. limite
    #obviamente se repetira hasta que la condicion se verdadera
    for posicion in range(palabra_longitud):
        letra = palabra_elegida[posicion]
        #print(f"Posición actual: {posición}\n Letra actual: {letra}\n Letra adivinada: {adivinar}")
        if letra == adivinar:
            display[posicion] = letra 
    if adivinar not in palabra_elegida:
        vidas -= 1
        if vidas == 0:
            fin_del_juego = True
            print("Pierdes, amigo mio ")  #editanto cambio para mi bash y github
            print(f'Pssst, la solución es {palabra_elegida}.')

    #con este if. vemos que la letra reemplazara a la posicion que pertenezca dentro de la lista display
    #Une todos los elementos de la lista y conviértelos en un String. (join=unirse
    #4.................................................................................. 
    print(f"{' '.join(display)}")

    if "_" not in display:
        fin_del_juego = True 
        print("Tú ganas.")

#TODO-3: - Imprima 'display' y debería ver la letra adivinada en la posición correcta y todas las demás letras reemplazadas con "_".
#Sugerencia: no se preocupe por hacer que el usuario adivine la siguiente letra. Abordaremos eso en el paso 3.
#4....................................................................................
    print(Etapas[vidas])