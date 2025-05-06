import random

# Opciones válidas
options = ['r', 'p', 's']
score = {'Usuario': 0, 'Computadora': 0, 'Empates': 0}

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return 'Empates'
    elif (usuario == 'r' and computadora == 's') or \
         (usuario == 'p' and computadora == 'r') or \
         (usuario == 's' and computadora == 'p'):
        return 'Usuario'
    else:
        return 'Computadora'

print("¡Bienvenido a Piedra, Papel o Tijeras!")
print("Usá 'r' para Piedra, 'p' para Papel, 's' para Tijeras y 'e' para salir.")

while True:
    user_input = input("Tu elección: ").lower()
    
    if user_input == 'e':
        print("Gracias por jugar. Marcador final:")
        print(f"Usuario: {score['Usuario']}, Computadora: {score['Computadora']}, Empates: {score['Empates']}")
        break

    if user_input not in options:
        print("Entrada no válida. Por favor ingresá 'r', 'p', 's' o 'e'.")
        continue

    computadora = random.choice(options)
    print(f"Computadora eligió: {computadora}")

    resultado = determinar_ganador(user_input, computadora)
    score[resultado] += 1

    if resultado == 'Empates':
        print("¡Es un empate!")
    else:
        print(f"¡{resultado} gana esta ronda!")

    print(f"Marcador - Usuario: {score['Usuario']} | Computadora: {score['Computadora']} | Empates: {score['Empates']}")
    print("-" * 40)
