# AppPython - prueba

El siguiente documento este compuesto de dos partes

* Instrucciones de juego
* Explicación del código

## Instrucciones de juego

Al iniciar el juego debes oprimir una tecla para comenzar su uso

*##* Uso del control demando

Se debe desplazar mediante el uso de teclas derecha e izquierda según el movimiento que se desee realizar.

Para disparar a los asteroides se debe usar la barra espaciadora.

* Objetivo del juego

El juego consiste en disparar a los meteoritos para poder destruirlos o lograr esquivarlos con el fin de no colisionar contra ellas y perder la partida
Cada vez que pierdas se reiniciara el juego

## Desarrollo del código

1. Se crea una pantalla utilizando los parámetros de altura, ancho, y colores
2. Como vamos a darle moviiiento a objetos sobre la pantalla debemos crear el dinamismo de los objetos por medio de variables de iniciación, marco y limite de la pantalla, titulo y tiempo de la duración
3. Se crean las clases:

* Clase jugador, meteoritos, disparos laser, explosiones:

Donde definimos las propiedades de cada objeto como imagen que se va mostrar, orientación de coordenadas en la pantalla, velocidad de movimiento
Se desarrolla la función que se le asignara a cada clase dependiendo de las sentencias a usar, por medio de bucles usando las condiciones if y else damos alternativas de jugabilidad y desenlace según la decisión del usuario.

* Bloque de texto

Se define mediante la sentencia de visualización de pantalla, por medio de método pintura ponemos el texto de inicio y de final de la aplicación el cual mediante una condición de recorrido junto con while decide que comando ejecutar según el resultado de la partida

* Lista de meteoritos

El listado se usa para poder conseguir la alternación de manera aleatoria con la cual se van a mostrar los objetos meteoritos alternando su tamaño y su dirección posteriormente
Por medio de una variable agregamos el fondo de pantalla

* Agregación de sonidos

Por medio de la librería pygame cargamos los sonidos los cuales se asignarán a los eventos según sea necesario
El archivo de música de fondo se mantiene repetitivo por medio del método loop
Se define el reloj con 60nsegundos con lo cual se genera una condición infinita a no ser que se cumpla la condicionante que lleva el juego a un cierre
Evento de disparo el cual se asigna a una acción con el comando de barra espaciadora

* Evento asteroide colisión

Mediante un ciclo for evaluamos si un objeto se une a otro para poder ejecutar la acción de colisión con el cual se abre un nuevo evento área cerrar la partida y salir del ciclo while

* Cierre

Para cerrar la pantalla se utiliza el método de blit llevando la pantalla a 0 y generando la activación de la sentencia quit, donde finalmente se cierra el código.
