import pygame

#Inicialización de Pygame
pygame.init()

#Dimensiones de la ventana del juego
WIDTH, HEIGHT = 700, 500

#Configuración de la ventana del juego
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")#Título de la ventana


#Configuración del juego
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 10 #El juego termina cuando uno se los jugadores llegue a 10


#Clase para manejar la paleta
class Paddle:
    #Atributos de la paleta
    COLOR = WHITE
    VEL = 4 #Velocidad de la paleta

    def __init__(self, x, y, width, height):
        #Inicialización de la paleta
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        #Dibuja la paleta en la ventana del juego
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))


    def move(self, up=True):
        #Mueve la paleta hacia arriba o abajo según la tecla presionada
        if up:
            self.y -= self.VEL

        else:
            self.y += self.VEL

    def reset(self):
        #Reinicia la posición original de la paleta
        self.x = self.original_x
        self.y = self.original_y


#Clase para manejar la pelota
class Ball:
    #Atributos de la pelota
    MAX_VEL = 5 #Velocidad de la pelota
    COLOR = WHITE

    def __init__(self, x, y, radius):
        #Inicialización de la pelota
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL #
        self.y_vel = 0

    def draw(self, win):
        #Dibuja la pelota en la ventana del juego
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    #Mueve la pelota en la dirección establecida por sus velocidades
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    #Reinicia la posición original de la pelota y sus velocidades
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


#Función para dibujar elementos en la ventana del juego
def draw(win, paddles, ball, left_score, right_score):
    win.fill(BLACK)

    #Dibuja las puntuaciones en la pantalla
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))
    

    #Dibuja las paletas y la pelota en la pantalla
    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue

        ball.draw(win)
        pygame.draw.rect(win, WHITE,(WIDTH//2 - 5, i, 10, HEIGHT//20))


    pygame.display.update()

#Función para manejar colisiones 
def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


#Función para manejar el movimiento de las paletas
def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)

#Función principal del juego
def main():

    #Configuración inicial
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH // 2, HEIGHT// 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    #Bucle principal del juego
    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, left_score,right_score)

        #Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)


        #Actualización de puntuaciones y finalización del juego
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()
        
        won = False
        if left_score >= WINNING_SCORE:
           won = True
           win_text = "El jugador de la Izquierda Ganó!!!!"

        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "El jugador de la Derecha Ganó!!!!"

        if won:
            #Muestra el mensaje de victoria, reinicia el juego y las puntuaciones
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(text,(WIDTH//2 -text.get_width()//2, HEIGHT//2 -text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0



    pygame.quit()


#Inicio del juego si se ejecuta este archivo
if __name__ == '__main__':
    main()
