import random
from diccionario import diccionario
import string

def palabra_valida(diccionario):
        palabra = random.choice(diccionario)
        while "-" in palabra or ' ' in palabra:
                palabra = random.choice(diccionario)
        return palabra.upper()

def dificultad():
    mode = (input("Que dificultad quieres jugar? (vidas): Dificil (3) Medio (7) Facil (10): ").lower())
    if mode == "dificil":
        lives = 3
    elif mode == "medio":
        lives = 7
    elif mode == "facil":
        lives = 10
    return lives

def ahorcado():
    lives = dificultad()
    palabra =  palabra_valida(diccionario)
    letraspalabra = set(palabra)
    abecedario = set(string.ascii_uppercase)
    letrasutilizadas = set()


    while len(letraspalabra) > 0 and lives > 0:
        print ("Tienes ",  lives, 'vidas restantes y las siguientes letras han sido utilizadas: ', ' '.join(letrasutilizadas))
        word_list = [letter if letter in letrasutilizadas else '-' for letter in palabra]
        print("Palabra actual:" , ' '.join(word_list))
        
        letrausuario = input("Adivina la siguiente letra: ").upper()

        if letrausuario in abecedario - letrasutilizadas:
             letrasutilizadas.add(letrausuario)
             if letrausuario in letraspalabra:
                letraspalabra.remove(letrausuario)
                print('')
             else:
                  lives = lives - 1
                  print(f"La letra {letrausuario} no esta dentro de la palabra. Tienes una vida menos")
        elif letrausuario in letrasutilizadas:
                print("Ya utilizaste esa letra")
        else:   
             print("No es una letra valida")


    if lives == 0:
        print(f"Ya no tienes vidas :(, La palabra era:{palabra}")
    else:
        print(f"Felicidades adivinaste la palabra {palabra}")

ahorcado()


