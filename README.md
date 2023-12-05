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

Este juego de la Serpiente (Snake) ha sido implementado en Python utilizando las librerías Tkinter y Pygame. La idea principal del juego es controlar una serpiente para que recoja comida y crezca, evitando chocar consigo misma o con las paredes del juego. Adicionalmente se le agregaron caracteristicas como que cambie de color la comida o de forma. 

## Funcionalidades y Características

### Visión General
- **Inicio del Juego:** El juego comienza con una ventana de menú que permite al jugador iniciar el juego, acceder a las instrucciones o salir.
- **Controles:** El jugador puede mover la serpiente hacia arriba, abajo, izquierda o derecha usando las teclas de dirección.
- **Puntuación:** La serpiente obtiene puntos cada vez que come comida.
- **Fin del Juego:** Si la serpiente choca consigo misma o con las paredes, se muestra una pantalla de fin de juego.
- **Reintentar:** Después del fin del juego, los jugadores pueden volver a intentar el juego.
- **Instrucciones:** Se proporciona orientación sobre cómo jugar el juego.

### Componentes Clave
- **Serpiente (Snake):** Compuesta por una serie de cuadrados que representan partes del cuerpo. Cada vez que come comida, su longitud aumenta.
- **Comida (Food):** Se coloca aleatoriamente en el lienzo del juego y cambia su apariencia cada vez que es consumida.
- **Lienzo (Canvas):** Área donde se desarrolla el juego, mostrando la serpiente, comida y mensajes de fin de juego.
- **Botones de Interfaz:** Botones para iniciar el juego, acceder a instrucciones o salir del juego.
# Clases Relevantes

### Clase Snake

La clase `Snake` representa la serpiente en el juego y gestiona su movimiento y aspecto visual. Sus aspectos más importantes son:

- **Constructor (`__init__`):** Inicializa la serpiente con un tamaño predefinido y crea cuadrados en el lienzo que representan su cuerpo.
- **Métodos:**
  - `__init__(self)`: Crea una serpiente con un tamaño inicial y coordenadas predefinidas.
  - Otros métodos que manejan la actualización de las coordenadas y la apariencia de la serpiente.

### Clase Food

La clase `Food` se encarga de generar la comida de forma aleatoria en el juego. Sus puntos importantes son:

- **Constructor (`__init__`):** Genera comida en ubicaciones aleatorias con formas y colores aleatorios.
- **Métodos:**
  - `__init__(self)`: Inicializa la comida con una forma y color aleatorios.
  - `change_appearance(self)`: Cambia la apariencia de la comida de manera aleatoria.

## Funciones Relevantes

### `start_game()`

La función `start_game()` es esencial para comenzar el juego. Realiza las siguientes acciones:

- Oculta el menú de inicio.
- Crea la ventana del juego.
- Inicializa la serpiente y la comida.
- Inicia el ciclo principal del juego llamando a la función `next_turn()`.

### `next_turn()`

Esta función controla cada turno del juego. Sus puntos claves son:

- Mueve la serpiente en la dirección adecuada.
- Verifica si la serpiente come la comida y actualiza la puntuación.
- Maneja la generación de nueva comida y su apariencia.
- Verifica colisiones y termina el juego si la serpiente choca.

### `game_over()` y `restart_game()`

Estas funciones gestionan el fin del juego y la posibilidad de reiniciar. Sus aspectos claves incluyen:

- `game_over()`: Muestra la pantalla de fin de juego y opciones para volver a intentarlo o salir.
- `restart_game()`: Reinicia el juego restableciendo la puntuación y los elementos del juego.

### `change_direction(new_direction)`

Controla el cambio de dirección de la serpiente según las teclas presionadas por el jugador.

## Utilidad de estas Clases y Funciones

Estas clases y funciones son cruciales para el funcionamiento y la lógica del juego de la serpiente. La clase `Snake` maneja el movimiento y el cuerpo de la serpiente, mientras que la clase `Food` gestiona la generación y apariencia de la comida. Las funciones como `start_game()` y `next_turn()` controlan la lógica del juego, incluyendo la detección de colisiones y el fin del juego.
## Cómo Jugar
1. Al iniciar el juego, se muestra un menú.
2. Utiliza las teclas de dirección para mover la serpiente y recolectar la comida.
3. Evita que la serpiente choque consigo misma o con las paredes.
4. Gana puntos por cada pieza de comida recolectada.
5. Intenta nuevamente si pierdes el juego.

## Controles
- Flecha Arriba: Mover la serpiente hacia arriba.
- Flecha Abajo: Mover la serpiente hacia abajo.
- Flecha Izquierda: Mover la serpiente hacia la izquierda.
- Flecha Derecha: Mover la serpiente hacia la derecha.



-`Space Invaders:`

Este código implementa un juego de Space Invaders simple utilizando Pygame, con funciones para controlar eventos, manejar colisiones, reproducir sonidos y mostrar pantallas de inicio y Game Over. Se importan las siguientes bibliotecas para la ejecución del código: math, random, pygame, y sys. Ahora bien, podemos ver que de forma gráfica, el juego detalla menús y controles para casos como  pausar el juego, salir del juego, reiniciar el juego y mostrar la pantalla de Game Over.

Una vez iniciado el juego, cuando un enemigo llega a la parte inferior de la pantalla, se muestra la pantalla de Game Over con opciones para volver a jugar o salir. Además, para iniciar la parte gráfica del juego implementamos funciones para implementar y cargar imágenes del background, el jugador, los enemigos y las balas. Donde se define la posición inicial del jugador, los enemigos y las balas, el título y el icono de la ventana del juego. La parte más importante del código corresponde a la función principal del juego, donde se ejecuta el código en conjunto. El juego se inicia con la función game_intro(),  utilizamos botones del teclado para controlar el movimiento del jugador y la pausa del juego, la función principal del juego es la operación de los enemigos mientras se mueven en la pantalla, y se detectan colisiones con las balas.

La función que inicia el juego es `game_intro()`, esta se encarga de controlar la pantalla de inicio del juego y presentar opciones para comenzar o salir. Cabe destacar que la función `game_loop()` es la función principal que maneja el bucle del juego. Controla eventos, el movimiento del jugador, la lógica de los enemigos, las colisiones y la actualización constante de la pantalla.
La función `fire_bullet(x, y)` gestiona el disparo de balas desde la posición del jugador. Este aspecto es crucial para la mecánica del juego.

Función `isCollision(enemyX, enemyY, bulletX, bulletY)` determina si ha ocurrido una colisión entre una bala y un enemigo. Esta función afecta directamente al puntaje y al reinicio de la posición de los enemigos.
La función `show_score(x, y)` muestra la puntuación actual en la pantalla, y la unica forma de reiniciar el score es con la función `restart_game()` se utiliza para reiniciar las variables del juego cuando es necesario, como después de que el jugador pierde. La función `pause_game()` permite pausar el juego de forma segura, manteniendo el puntaje actual del usuario; y la función `draw_game_over_screen()` muestra la pantalla de Game Over y proporciona opciones para volver a jugar o salir.

-`Flappy Bird:`

La funcionalidad del juegoFlappy Bird essimple pero desafiante en el que controlas a un pájaro y tu objetivo es volar a través de un entorno lleno de tuberías verdes sin chocar contra ellas. Se controla la altura del ave con el espaciado del teclado, cada toque hace que el pájaro vuele hacia arriba un poco

Las funciones importantes del código son las siguientes:

`1. bird(y)`

Parámetro y: La posición vertical del pájaro en la pantalla.
Acción: Dibuja el pájaro en la posición (bird_x, y) en la pantalla.

`3. pipes(x, gap)`
   
Parámetros:
x: La posición horizontal de los tubos en la pantalla.
gap: La brecha entre los tubos.
•	Acción: Dibuja los tubos en la posición (x, gap - pipe_height) y (x, gap + pipe_gap) en la pantalla.

`4. show_score(score, x, y)`
   
Parámetros:
score: El puntaje actual del jugador.
x: La posición horizontal donde se muestra el puntaje.
y: La posición vertical donde se muestra el puntaje.
•	Acción: Muestra el puntaje en la pantalla en la posición (x, y).

`5. game_over_text()`
   
Acción: Muestra el texto "Game Over" en el centro de la pantalla.


`6. final_score_text(score)`
   
 Parámetro score: El puntaje final del jugador.
 
Acción: Muestra el puntaje final del jugador en la pantalla.



`7. start_menu()`

Acción: Muestra el menú de inicio que indica al jugador que presione la barra espaciadora para comenzar y "P" para pausar.

`8. again_exit_menu()`

Acción: Muestra el menú que aparece cuando el juego termina, indicando al jugador que presione "A" para jugar de nuevo o "Q" para salir.

`9. pause_menu()`

Acción: Muestra el menú de pausa que aparece cuando el juego está pausado, indicando al jugador que presione "P" para reanudar.






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

Demostración de la interfaz gráfica de los juegos ejecutados


-`Pinpong:`

![Captura de pantalla 2023-12-05 132052](https://github.com/dylaREX1028/Proyecto02/assets/130623878/71902db1-f404-4e77-ba7d-478d2c8a0af6)

![Captura de pantalla 2023-12-05 132109](https://github.com/dylaREX1028/Proyecto02/assets/130623878/831addc3-c3eb-412b-ba97-db8fc585e41c)

![Captura de pantalla 2023-12-05 132046](https://github.com/dylaREX1028/Proyecto02/assets/130623878/a75af034-e044-44e1-ba18-478a08fd4975)



-`Snake:`

![Captura de pantalla 2023-12-05 114325](https://github.com/dylaREX1028/Proyecto02/assets/130623878/589bceab-7b3f-475c-83f1-3ba10217e70b)

![Captura de pantalla 2023-12-05 115937](https://github.com/dylaREX1028/Proyecto02/assets/130623878/3a206cc6-450a-48a7-a6e6-356dc2108e16)

![Captura de pantalla 2023-12-05 114615](https://github.com/dylaREX1028/Proyecto02/assets/130623878/60a0ad4e-3f25-43ac-ac80-dc0ac7532296)

![Captura de pantalla 2023-12-05 114624](https://github.com/dylaREX1028/Proyecto02/assets/130623878/914e2cc8-90a2-4844-87c3-87c9eee876e4)


-`Space Invaders:`

![WhatsApp Image 2023-12-05 at 11 15 08 AM](https://github.com/dylaREX1028/Proyecto02/assets/143848068/a5877903-1430-424e-8d87-9b3bd271b2eb)

![WhatsApp Image 2023-12-05 at 11 15 09 AM](https://github.com/dylaREX1028/Proyecto02/assets/143848068/a10d46e5-f2e5-4773-a5ad-68c6a130f119)

![WhatsApp Image 2023-12-05 at 11 15 09 AM (1)](https://github.com/dylaREX1028/Proyecto02/assets/143848068/02592fcd-8c29-47f3-93e0-2561cb8011f9)



-`Flappy Bird:`

![Captura de pantalla 2023-12-05 111736](https://github.com/dylaREX1028/Proyecto02/assets/130623878/a1050b12-73c5-4989-b902-ab38491c4e9f)

![Captura de pantalla 2023-12-05 112547](https://github.com/dylaREX1028/Proyecto02/assets/130623878/4ae7ba1b-fa59-41e1-9656-fd28ec12f2ae)

![Captura de pantalla 2023-12-05 112124](https://github.com/dylaREX1028/Proyecto02/assets/130623878/c4049ecf-46aa-4d62-8521-2868d77c75f4)

![Captura de pantalla 2023-12-05 112133](https://github.com/dylaREX1028/Proyecto02/assets/130623878/d04d74fb-55d4-48b4-8ac5-95cb1d63de54)
