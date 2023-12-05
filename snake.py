# ************************************
# Python Snake
# ************************************

# Importar los módulos necesarios
from tkinter import *
import random
import tkinter

# Definir las variables globales necesarias
# Definir la ventana global
window = Tk()
canvas = None
label = None
start_button = None
instructions_button = None
exit_button = None
snake = None
food = None
direction = 'down'
score = 0

# Dimensiones del juego
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# Clase Snake para definir la serpiente
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Inicializar las coordenadas de la serpiente
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Crear los cuadrados que representan la serpiente
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Clase Food para definir la comida
class Food:
    def __init__(self):
        self.shape = random.choice(['oval', 'rectangle'])  # Forma inicial aleatoria
        self.color = FOOD_COLOR  # Color inicial

        # Generar coordenadas aleatorias para la comida
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Dibujar la comida en el canvas
        if self.shape == 'oval':
            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.color, tag="food")
        else:
            canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.color, tag="food")

    # Cambiar la apariencia de la comida
    def change_appearance(self):
        self.shape = random.choice(['oval', 'rectangle'])  # Cambio aleatorio de forma
        self.color = random.choice(['#FFA500', '#FF00FF', '#00FFFF'])  # Cambio aleatorio de color

        # Actualizar la apariencia de la comida en el canvas
        canvas.delete("food")

        x, y = self.coordinates
        if self.shape == 'oval':
            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.color, tag="food")
        else:
            canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.color, tag="food")

# Función para iniciar el juego
def start_game():
    global snake, food
    hide_menu()
    snake = Snake()
    food = Food()
    window.after(SPEED, next_turn)  # Llamar a next_turn después de iniciar el juego

# Función para el próximo turno en el juego
def next_turn():
    global snake, food, direction, canvas, score

    x, y = snake.coordinates[0]

    # Mover la serpiente en la dirección correspondiente
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Insertar las nuevas coordenadas al principio de la serpiente
    snake.coordinates.insert(0, (x, y))
    
    # Crear un nuevo cuadrado para la cabeza de la serpiente en las nuevas coordenadas
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    # Insertar el nuevo cuadrado al principio de la lista de cuadrados de la serpiente
    snake.squares.insert(0, square)

    # Verificar si la serpiente come la comida
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))

        # Cambiar la apariencia de la comida existente
        food.change_appearance()

        # Actualizar la posición de la comida
        food.coordinates = [random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE,
                            random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE]

        # Actualizar la apariencia de la comida en el canvas
        canvas.delete("food")
        if food.shape == 'oval':
            canvas.create_oval(food.coordinates[0], food.coordinates[1],
                               food.coordinates[0] + SPACE_SIZE, food.coordinates[1] + SPACE_SIZE,
                               fill=food.color, tag="food")
        else:
            canvas.create_rectangle(food.coordinates[0], food.coordinates[1],
                                    food.coordinates[0] + SPACE_SIZE, food.coordinates[1] + SPACE_SIZE,
                                    fill=food.color, tag="food")
    else:
        # Si la serpiente no come la comida, eliminar el último cuadrado de la serpiente
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Verificar colisiones
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn)

# Función para cambiar la dirección de la serpiente
def change_direction(new_direction):
    global direction
    direction = new_direction

# Función para verificar colisiones
def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Verificar colisión con las paredes
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    # Verificar colisión con el cuerpo de la serpiente
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Función para mostrar el fin del juego
def game_over():
    global canvas, snake, food, score

    # Mostrar texto de fin del juego en el canvas
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text="FIN DEL JUEGO!", fill="pink", tag="gameover")

    # Crear botón "Reintentar" y colocarlo en el canvas
    retry_button = Button(window, text="Reintentar", font=('consolas', 20), command=restart_game)
    retry_button.pack()
    canvas.create_window(canvas.winfo_width() / 2, canvas.winfo_height() / 1.5, window=retry_button)

# Función para reiniciar el juego
def restart_game():
    global canvas, snake, food, score, direction, window
    
    score = 0
    direction = 'down'
    label.config(text="Score: {}".format(score))

    if canvas is not None:
        canvas.delete("all")  # Eliminar todo el contenido del canvas

    create_game_window()  # Re-crear el canvas y empaquetarlo nuevamente
    
    # Restablecer la posición de la ventana
    window.update_idletasks()  # Actualizar la ventana para obtener el tamaño correcto
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    window.geometry('+{}+{}'.format(int(x_coordinate), int(y_coordinate)))

    # Inicializar una nueva serpiente y comida
    snake = Snake()
    food = Food()
    window.after(SPEED, next_turn)  # Comenzar el juego nuevamente

# Función para cerrar el juego
def exit_game():
    window.destroy()

# Función para ocultar el menú
def hide_menu():
    label.pack_forget()
    start_button.pack_forget()
    instructions_button.pack_forget()
    exit_button.pack_forget()

# Función para crear el canvas del juego
def create_game_window():
    global canvas
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

# Función para mostrar las instrucciones
def show_instructions():
    hide_menu()
    instructions_text = """
    Instrucciones:
    - Utiliza las teclas de flecha (arriba, abajo, izquierda, derecha) para mover la serpiente.
    - El objetivo es comer la comida roja para crecer y obtener puntos.
    - Evita chocar contra las paredes o contra tu propia cola, esto terminará el juego.
    - Haz clic en 'Start Game' para comenzar o 'Exit' para salir del juego.
    Presiona 'Volver al Menú' para regresar al menú principal.
    """
    instruction_label = Label(window, text=instructions_text, font=('consolas', 14), justify=LEFT)
    instruction_label.pack(pady=20)
    back_to_menu_button = Button(window, text="Volver al Menú", font=('consolas', 16), command=display_main_menu)
    back_to_menu_button.pack(pady=10)

# Función para mostrar el menú principal
def display_main_menu():
    # Eliminar los widgets actuales del menú
    for widget in window.winfo_children():
        widget.pack_forget()
    create_buttons_and_labels()

# Función para crear los botones y etiquetas del menú principal
def create_buttons_and_labels():
    global label, start_button, instructions_button, exit_button
    label = Label(window, text="Snake Game", font=('consolas', 24))
    label.pack(pady=20)
    start_button = Button(window, text="Start Game", font=('consolas', 16), command=restart_game)
    start_button.pack(pady=10)
    instructions_button = Button(window, text="Instructions", font=('consolas', 16), command=show_instructions)
    instructions_button.pack(pady=10)
    exit_button = Button(window, text="Exit", font=('consolas', 16), command=exit_game)
    exit_button.pack(pady=10)

# Función principal para inicializar el juego
def initialize_game():
    global window
    window.title("Snake Game")
    window.resizable(False, False)
    create_buttons_and_labels()  # Crear botones y etiquetas del menú principal
    
    # Vinculación de las teclas de flecha para controlar la dirección de la serpiente
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))

    # Centrar la ventana en la pantalla
    window.update_idletasks()  # Actualizar la ventana para obtener el tamaño correcto
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    window.geometry('+{}+{}'.format(int(x_coordinate), int(y_coordinate)))

    window.mainloop()  # Iniciar el bucle principal de la interfaz

initialize_game()  # Llamar a la función principal para iniciar el juego
