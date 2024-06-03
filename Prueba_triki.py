import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
size = (500, 550)  # Aumentamos la altura para dar espacio al mensaje y al botón
pantalla = pygame.display.set_mode(size)
pygame.display.set_caption("X&O Arena")

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
azul = (0, 0, 255)
gris_claro = (200, 200, 200)

# Fuentes
fuente = pygame.font.Font(None, 74)
fuente_titulo = pygame.font.Font(None, 50)
fuente_boton = pygame.font.Font(None, 36)

# Configurar el tablero
tablero = [["" for _ in range(3)] for _ in range(3)]
jugador = "X"
ganador = None

# Dibujar la cuadrícula
def dibujar_cuadricula():
    pantalla.fill(blanco)
    titulo_texto = fuente_titulo.render("X&O Arena", True, negro)
    pantalla.blit(titulo_texto, (150, 20))
    for fila in range(1, 3):
        pygame.draw.line(pantalla, negro, (100, 100 * fila + 100), (400, 100 * fila + 100), 3)
        pygame.draw.line(pantalla, negro, (100 * fila + 100, 100), (100 * fila + 100, 400), 3)

# Dibujar las X y O en el tablero
def dibujar_marcas():
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == "X":
                pygame.draw.line(pantalla, rojo, (columna * 100 + 120, fila * 100 + 120), (columna * 100 + 180, fila * 100 + 180), 5)
                pygame.draw.line(pantalla, rojo, (columna * 100 + 180, fila * 100 + 120), (columna * 100 + 120, fila * 100 + 180), 5)
            elif tablero[fila][columna] == "O":
                pygame.draw.circle(pantalla, azul, (columna * 100 + 150, fila * 100 + 150), 40, 5)

# Verificar si hay un ganador
def verificar_ganador():
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] != "":
            return tablero[fila][0]
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != "":
            return tablero[0][columna]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
        return tablero[0][2]
    return None

# Verificar si hay empate
def verificar_empate():
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == "":
                return False
    return True

# Dibujar el botón de volver a jugar
def dibujar_boton_volver_a_jugar():
    pygame.draw.rect(pantalla, gris_claro, (150, 500, 200, 40))
    texto_boton = fuente_boton.render("Volver a jugar", True, negro)
    pantalla.blit(texto_boton, (160, 505))

# Reiniciar el juego
def reiniciar_juego():
    global tablero, jugador, ganador
    tablero = [["" for _ in range(3)] for _ in range(3)]
    jugador = "X"
    ganador = None

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if ganador or verificar_empate():
                if 150 <= x <= 350 and 505 <= y <= 555:  # Comprobar si se hizo clic en el botón de volver a jugar
                    reiniciar_juego()
            else:
                if 100 < x < 400 and 100 < y < 400:  # Asegurarse de que el clic esté dentro del tablero
                    fila, columna = (y - 100) // 100, (x - 100) // 100
                    if tablero[fila][columna] == "":
                        tablero[fila][columna] = jugador
                        jugador = "O" if jugador == "X" else "X"

    dibujar_cuadricula()
    dibujar_marcas()
    ganador = verificar_ganador()
    empate = verificar_empate()

    if ganador:
        texto_ganador = fuente.render(f"¡{ganador} ha ganado!", True, negro)
        pantalla.blit(texto_ganador, (90, 425))  # Ajustamos la posición del mensaje de ganador
        dibujar_boton_volver_a_jugar()
    elif empate:
        texto_empate = fuente.render("¡Empate!", True, negro)
        pantalla.blit(texto_empate, (140, 425))  # Ajustamos la posición del mensaje de empate
        dibujar_boton_volver_a_jugar()

    pygame.display.flip()

pygame.quit()
sys.exit()
