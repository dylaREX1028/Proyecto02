# Proyecto02-Consola de Juego
- Universidad de Costa Rica
- Facultad de Ingeniería
- Escuela de Ingeniería Eléctrica
- IE-0117 - Programación Bajo Plataformas Abiertas
- II ciclo 2023
- Proyecto Final: Consola de juegos
- Participantes:
  - Dilana Rodríguez Jiménez (Carne C06660)
  - Kryssia Martínez Martínez (Carne B84636)
  - Randy Cascante Espinoza (Carné C11718)
  - Kristel Hidalgo Mata (Carne C23887)
  
- Profesora: Carolina Trejos
- Fecha: 5 de Diciembre del 2023


## Descripción del proyecto
El presente proyecto consiste en el desarrollo de una consola de 4 juegos en leguaje de programación python. Al ejecutar el código de cualquier juego se despliega una interfaz gráfica en donde se puede interactura con el juego. Algunos de ellos tiene un menú  para empezar a jugar y salir del programa, lo juegos disponibles son Pin-pong, Snake, FlappyBird y Space invaders. 

### Teoría y funcionamiento

-`Pinpong:`

El juego desarrollado de Ping-Pong se implementó con la biblioteca de Pygame. Y la finalidad del juego es que dos jugadores compiten controlando paletas para golpear una pelota.  El jugador de la izquierda se mueve con las teclas W y S para trasladarse hacia arriba o abajo, mientras que el jugador de la derecha se traslada con las flechas de arriba y abajo. Se gana el juego cuando un de los jugadores lleguen a la puntuación de 10 y cada punto se obtiene cuando a su contrincante no pueda golpear la pelota y esta se vaya fuera de la pantalla. Después de cada punto obtenido la pelota se reinicia en el centro de la pantalla.

1. De clases se está se están manejado las siguientes:
   
Como `Paddle`: Representa las paletas de los jugadores. Puede dibujarse, moverse y reiniciarse a su posición original. Y `Ball`: Representa la pelota. Puede dibujarse, moverse y reiniciarse a su posición original.

2. Respecto a las funciones Principales serían:

`draw:` Dibuja en la ventana del juego las paletas, la pelota y las puntuaciones de los jugadores. `handle_collision:` Maneja las colisiones de la pelota con las paletas y los bordes de la ventana. `handle_paddle_movement:` Controla el movimiento de las paletas según las teclas presionadas por los jugadores. `main:` Función principal del juego. Configura los elementos iniciales, maneja el bucle principal del juego, detecta eventos, actualiza el movimiento de paletas y pelota, gestiona colisiones, controla las puntuaciones y muestra un mensaje de victoria cuando un jugador alcanza la puntuación definida para ganar.

-`Snake:`


-`Space Invaders:`

Este código implementa un juego de Space Invaders simple utilizando Pygame, con funciones para controlar eventos, manejar colisiones, reproducir sonidos y mostrar pantallas de inicio y Game Over. Se importan las siguientes bibliotecas para la ejecución del código: math, random, pygame, y sys. Ahora bien, podemos ver que de forma gráfica, el juego detalla menús y controles para casos como  pausar el juego, salir del juego, reiniciar el juego y mostrar la pantalla de Game Over.

Una vez iniciado el juego, cuando un enemigo llega a la parte inferior de la pantalla, se muestra la pantalla de Game Over con opciones para volver a jugar o salir. Además, para iniciar la parte gráfica del juego implementamos funciones para implementar y cargar imágenes del background, el jugador, los enemigos y las balas. Donde se define la posición inicial del jugador, los enemigos y las balas, el título y el icono de la ventana del juego. La parte más importante del código corresponde a la función principal del juego, donde se ejecuta el código en conjunto. El juego se inicia con la función game_intro(),  utilizamos botones del teclado para controlar el movimiento del jugador y la pausa del juego, la función principal del juego es la operación de los enemigos mientras se mueven en la pantalla, y se detectan colisiones con las balas.

La función que inicia el juego es `game_intro()`, esta se encarga de controlar la pantalla de inicio del juego y presentar opciones para comenzar o salir. Cabe destacar que la función `game_loop()` es la función principal que maneja el bucle del juego. Controla eventos, el movimiento del jugador, la lógica de los enemigos, las colisiones y la actualización constante de la pantalla.
La función `fire_bullet(x, y)` gestiona el disparo de balas desde la posición del jugador. Este aspecto es crucial para la mecánica del juego.

Función `isCollision(enemyX, enemyY, bulletX, bulletY)` determina si ha ocurrido una colisión entre una bala y un enemigo. Esta función afecta directamente al puntaje y al reinicio de la posición de los enemigos.
La función `show_score(x, y)` muestra la puntuación actual en la pantalla, y la unica forma de reiniciar el score es con la función `restart_game()` se utiliza para reiniciar las variables del juego cuando es necesario, como después de que el jugador pierde. La función `pause_game()` permite pausar el juego de forma segura, manteniendo el puntaje actual del usuario; y la función `draw_game_over_screen()` muestra la pantalla de Game Over y proporciona opciones para volver a jugar o salir.

-`Flappy Bird:`







### Objetivos
 - Proporcionar una experiencia de entretenimiento atractiva a través de juegos interactivos en el menú de jugos, con el fin de mejorar la agilidad mental y los reflejos de los participantes.
 - Facilitar la oportunidad de aprendizaje y desarrollo de habilidades en el campo de la programación y diseño de juegos, dado a que es un compo bastante amplio.
 - Promover una experiencia saludable a través de los juegos interactivos, con el propósito de contribuir a la mejora de la salud mental de las personas al proporcionar una vía efectiva para reducir el estrés, y fomentar la distracción positiva 


### Limitaciones

En el presente proyecto se pretendía generar un menú para unir los 4 juegos, pero no fue posible generarlo. Dado que al realizar el menú solo se imprimián las interfaz gráficas de los juegos pero se ejecutaban. Por lo que se optó por generar un menú por cada juego, siendo posible 3 de los 4 juegos desarrollados.


## Dependencias e instalación
Para ejecutar el siguiente programa es necesario primeramente descargar los documentos que se encuentran en la carpetas sin importar el sistema operativo que esté utilizando. 

Ahora, si está utilizando `Linux`, hay que instalar python3 y las dependecias necesarias para correr los programas. Solo necesita copiar y pegar estas dependencias en su terminal y darle enter para que estas se instalen.

```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip install pygame 
pip install mixer
pip install tk

```



Si fuera el caso que esté utilizando `Windows` se recomienda instalar `Visual Studio Code` y descaragr la biblioteca de Python, además de instalar las dependencias que de igual manera funciona los programas. Para instalar las dependencias de necesario copiar y pegar los siguiente en el la terminal del editor de texto.

```bash
python.exe -m pip install --upgrade pip
pip install tk
pip install pygame 
Pip install mixer
pip install tk

```


## Pasos para ejecucion

Para ejecutar en `Linux` los 4 juegos es necesario que copie y pegue estos comando uno a uno para poder juagar cada juego en la terminal.

```bash

python3 Proyecto.py
python3 frescuradecodigo.py
python3 ping_pong_4.py
python3 snake.py

```

## Ejemplos de cómo funciona

Kryssia




