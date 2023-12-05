import math
import random
import pygame
from pygame import mixer
import sys

# Inicializar pygame
pygame.init()

# Crear la pantalla
screen_width, screen_height = 800, 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Fondo
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

# Sonido
mixer.music.load("background.wav")
mixer.music.play(-1)

# Título e Icono
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Jugador
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 380
playerX_change = 0

# Enemigo
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img = pygame.image.load('enemy.png')
    enemy_img = pygame.transform.scale(enemy_img, (64, 64))
    enemyImg.append(enemy_img)
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bala
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (32, 32))
bulletX = 0
bulletY = 380
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Puntuación
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Función para mostrar la puntuación
def show_score(x, y):
    score = font.render("Puntuación : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Función para mostrar el texto de Game Over
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Función para verificar la colisión entre enemigo y bala
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Función para mostrar botones
def draw_button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = (x + (w / 2), y + (h / 2))
    screen.blit(text_surf, text_rect)

# Función para manejar el renderizado de texto
def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()

# Función para reiniciar el juego
def restart_game():
    global score_value, playerX, playerY, bullet_state
    score_value = 0
    playerX = 370
    playerY = 380
    bullet_state = "ready"
    for i in range(num_of_enemies):
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(50, 150)

# Función para dibujar al jugador
def player(x, y):
    screen.blit(playerImg, (x, y))

# Función para dibujar a un enemigo
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Función para disparar una bala
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Función para pausar el juego
def pause_game():
    mixer.music.pause()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    mixer.music.unpause()
                    paused = False

# Función para salir del juego
def quit_game():
    pygame.quit()
    sys.exit()

# Función para manejar los estados del juego
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(background, (0, 0))
        large_text = pygame.font.Font('freesansbold.ttf', 80)
        text_surf, text_rect = text_objects("Space Invaders", large_text)
        text_rect.center = ((screen_width / 2), (screen_height / 2 - 100))
        screen.blit(text_surf, text_rect)

        draw_button("Iniciar Juego", 300, 300, 200, 50, (0, 255, 0), (0, 200, 0), game_loop)
        draw_button("Salir", 300, 400, 200, 50, (255, 0, 0), (200, 0, 0), quit_game)

        pygame.display.update()

# Función para manejar el bucle principal del juego
def game_loop():
    global score_value, playerX, playerY, playerX_change, bulletX, bulletY, bullet_state
    global enemyX, enemyY, enemyX_change, enemyY_change

    running = True
    game_active = True

    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletSound = mixer.Sound("laser.wav")
                        bulletSound.play()
                        bulletX = playerX
                        bullet_state = "fire"
                if event.key == pygame.K_p:
                    pause_game()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Movimiento del jugador
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Movimiento del enemigo
        for i in range(num_of_enemies):
            if enemyY[i] > 340:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                draw_game_over_screen()
                game_active = False
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # Colisión
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 380
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            # Movimiento de la bala
            if bulletY <= 0:
                bulletY = 380
                bullet_state = "ready"
            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletY -= bulletY_change

            # Dibujar enemigo
            enemy(enemyX[i], enemyY[i], i)

        # Dibujar jugador
        player(playerX, playerY)
        show_score(textX, textY)

        pygame.display.update()

        if not game_active:
            break

    pygame.quit()
    sys.exit()

# Función para dibujar la pantalla de Game Over
def draw_game_over_screen():
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))
        game_over_text()


        draw_button("Volver", 300, 300, 200, 50, (0, 255, 0), (0, 200, 0), game_intro)
        draw_button("Salir", 300, 400, 200, 50, (255, 0, 0), (200, 0, 0), quit_game)

        pygame.display.update()

# Iniciar el juego
game_intro()
