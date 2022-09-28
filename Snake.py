import pygame
import sys
import random
from playsound import playsound

pygame.init()

# Sonidos:
sonido_giros = True
sonido_manzana = True
sonido_muerte = True
volumen_giros = 0.5

tamaño_bloque = 40
tamaño_cuadrícula = 15  #Debe ser impar

velocidad = 10

anchura = tamaño_bloque * tamaño_cuadrícula
altura = anchura

puntos = 0

blanco = (255,255,255)
negro = (0,0,0)
gris = (125,125,125)
rojo = (255,0,0)
verde = (0,255,0)
verde_oscuro = (0,125,0)

tamaño_manzana = 16
posicion_manzana = [random.randint(0, tamaño_cuadrícula - 1), random.randint(0, tamaño_cuadrícula - 1)]

posicion_cabeza_serpiente = [(tamaño_cuadrícula - 1)/2, (tamaño_cuadrícula - 1)/2]
posicion_cuerpo_serpiente = []
posicion_cuerpo_serpiente.append([posicion_cabeza_serpiente[0], posicion_cabeza_serpiente[1]])

direccion = "quieto"

screen = pygame.display.set_mode((anchura, altura))

fila = []

for i in range(tamaño_cuadrícula):
	fila.append(0)

mapa = []

for i in range(tamaño_cuadrícula):
	mapa.append(fila)

game_over = False

clock = pygame.time.Clock()

while not game_over:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and direccion != "abajo":
				if direccion != "arriba" and sonido_giros == True:
					pygame.mixer.music.load("giro_1.wav")
					pygame.mixer.music.set_volume(volumen_giros)
					pygame.mixer.music.play()
				direccion = "arriba"
			elif event.key == pygame.K_DOWN and direccion != "arriba":
				if direccion != "abajo" and sonido_giros == True:
					pygame.mixer.music.load("giro_2.wav")
					pygame.mixer.music.set_volume(volumen_giros)
					pygame.mixer.music.play()
				direccion = "abajo"
			elif event.key == pygame.K_RIGHT and direccion != "izquierda":
				if direccion != "derecha" and sonido_giros == True:
					pygame.mixer.music.load("giro_3.wav")
					pygame.mixer.music.set_volume(volumen_giros)
					pygame.mixer.music.play()
				direccion = "derecha"
			elif event.key == pygame.K_LEFT and direccion != "derecha":
				if direccion != "izquierda" and sonido_giros == True:
					pygame.mixer.music.load("giro_4.wav")
					pygame.mixer.music.set_volume(volumen_giros)
					pygame.mixer.music.play()
				direccion = "izquierda"

	if direccion == "quieto":
		pass
	elif direccion == "arriba":
		posicion_cabeza_serpiente[1] -= 1
	elif direccion == "abajo":
		posicion_cabeza_serpiente[1] +=1
	elif direccion == "derecha":
		posicion_cabeza_serpiente[0] += 1
	elif direccion == "izquierda":
		posicion_cabeza_serpiente[0] -=1

	if posicion_cabeza_serpiente[0] < 0 or posicion_cabeza_serpiente[0] > tamaño_cuadrícula - 1 or posicion_cabeza_serpiente[1] < 0 or posicion_cabeza_serpiente[1] > tamaño_cuadrícula - 1:
			game_over = True

	posicion_cuerpo_serpiente.append([posicion_cabeza_serpiente[0], posicion_cabeza_serpiente[1]])
	if posicion_manzana == posicion_cabeza_serpiente:
		while posicion_cuerpo_serpiente.count(posicion_manzana) != 0:
			posicion_manzana = [random.randint(0, tamaño_cuadrícula - 1), random.randint(0, tamaño_cuadrícula - 1)]
		puntos += 1
		if sonido_manzana == True:
			pygame.mixer.music.load("comer_manzana.wav")
			pygame.mixer.music.play()
	else:
		posicion_cuerpo_serpiente.pop(0)

	if posicion_cuerpo_serpiente.count(posicion_cabeza_serpiente) != 1:
		game_over = True

	screen.fill(negro)
	for y in range(tamaño_cuadrícula):
		for x in range(tamaño_cuadrícula):
			pygame.draw.rect(screen, gris, ((tamaño_bloque * x) + 2, (tamaño_bloque * y) + 2, 36, 36))

	pygame.draw.circle(screen, rojo, (posicion_manzana[0] * 40 + 20, posicion_manzana[1] * 40 + 20), tamaño_manzana)

	for element in posicion_cuerpo_serpiente:
		pygame.draw.rect(screen, verde, ((tamaño_bloque * element[0]) + 2, (tamaño_bloque * element[1]) + 2, 36, 36))

	clock.tick(velocidad)

	pygame.display.update()
if sonido_muerte == True:
	playsound("rock.wav")
print("Puntos: " + str(puntos))