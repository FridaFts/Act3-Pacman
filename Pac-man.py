# Roberto Carlo Mata Pineda
# A00829002
# Frida Fuentes
# A00827
# Reflexión
#
# Fecha - 6 - Mayo - 2021

# Se hacen los import de todas las librerias
from random import choice
from turtle import *
from freegames import floor, vector

# Almacena la cantidad de puntos acumulados por Pac-man
state = {'score': 0}

# Hace invisible a Turtle, ademas crea 2 objetos de clase Turtle
path = Turtle(visible=False)
writer = Turtle(visible=False)

# Dirección la cual esta Pac-man
aim = vector(5, 0)

# Crea Pac-man en posicion -40,-80 
pacman = vector(-40, -80)

# Lista de listas de posición y dirección de cada fantasma
# CAMBIO PARA HACERLOS MAS RAPIDOS A LOS FANTASMAS
ghosts = [
    [vector(-180, 160), vector(13, 0)],
    [vector(-180, -160), vector(13, 10)],
    [vector(100, 160), vector(0, -13)],
    [vector(100, -160), vector(-13, 0)],
]

# Lista del tablero 20 columnas x 20 renglones
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Dibuuja un cuadrado con su esq inf izq en (x,y)
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

# 
def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Retorna verdadero si el punto esta una tile válido
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

# Si la celda es 0 regresa ya que es pared
    if tiles[index] == 0:
        return False

    index = offset(point + 19)
    
# Si la celda es 0 regresa ya que es pared
    if tiles[index] == 0:
        return False
    
#Retorna true
    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

#Recorre toda lista de (titles)
    for index in range(len(tiles)):
        #Extrae el valor que existe en posiciín index
        tile = tiles[index]

#Si el valor es mayor que 0
        if tile > 0:
            #Calcula x,y en donde se dibuja el square
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            #Dibuja la galleta sobre el square, en el centro
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    #colores = ['red', 'gray', 'blue', 'yellow']
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    # Limpia la ventana
    clear()

    #Si es una posición valida ejecuta en esa dirección
    # la posición del pacman
    if valid(pacman + aim):
        pacman.move(aim)

    # Retoma la posición de pacman en el tablero
    index = offset(pacman)

    # 1 - camino
    if tiles[index] == 1:
        # a esa posición le asigna 2
        tiles[index] = 2
        # Se incrementa el valor de score
        state['score'] += 1
        # Calcula posición x,y del pacman
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        # Dibuja el square - sin galleta
        square(x, y)

    up()
    # Se va a la posición del pacman
    goto(pacman.x + 10, pacman.y + 10)
    # 1ra vez que se dibuja el pacman
    dot(20, 'yellow')
#k=0
    for point, course in ghosts:
        # Valida si el fantasma poin se puede mover en course
        if valid(point + course):
            point.move(course)
            
        else: #Si el fantasma no se puede mover en esa dirección...
            # CAMBIO PARA HACERLOS MAS RAPIDOS A LOS FANTASMAS
            options = [
                vector(13, 0),
                vector(-13, 0),
                vector(0, 13),
                vector(0, -13),
            ]
            
            #plan guarda la nueva dirección del fantasma
            #HACER FANTASMAS MÁS INTELIGENTES
            plan = choice(options)
            course.x = plan.x 
            course.y = plan.y 
        # Levanta
        up()
        # Mueve la posición del fantasma
        goto(point.x + 10, point.y + 10)
        # Dibuja el fantasma
        dot(20, 'red')
        #dot(20, colores[k])
        #k = k + 1
       

    update()

    # recorre lista de fantasmas para ver si
    # coinciden las posiciónes
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            writer.goto(-120,10)
            writer.write('GAME OVER' , font=('Arial',30,'normal'))
            return

    ontimer(move, 100)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Tamaño de ventana ancho 420,420,
# 370 / 0 ,0 indica posición de la esq sup izq de la ventana
setup(420, 420, 370, 0)
# Esconde a Turtle (Flecha)
hideturtle()
# Oculta toda forma de dibujar se puede poner (True)
tracer(False)
# Mueve la turtle writer a posición 160,160
writer.goto(160, 160)
writer.color('white')
#valor = state['score']
writer.write(state['score'])
# Activa los eventos del teclado
listen()
# En caso de que el usuario oprima tecla manda llamar función change
# LLama a la función change con argumentos indicados
# Que indican la nueva dirección de pacman
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
# LLama a world - dibuja el tablero
world()
# LLama la función move()
move()
# Entra en un loop infinito para atender todo los eventos
done()