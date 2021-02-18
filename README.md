# "Enunciado"

El archivo input.json contiene configuraciones para una orquestador de contenedores (Marathon).

Dentro del mismo se encuentra la definición de N aplicaciones con información respecto al runtime (con que imagen de Docker corre, cuanta RAM/CPU tiene reservada, que puertos reserva/expone, cuantas instancias ocupa, etc.)

---

## Se pide:

- obtener todas las aplicaciones que hayan cambiado su configuración en las ultimas 24 horas.

- la salida del programa tiene que tener el nombre de cada aplicación y su fecha de modificación.

#### BONUS: Debe verse primero la última que se modifico.
#### BONUS: Que hayan cambiado su configuración en las ultimas X horas.
#### BONUS: Encontrar aquellas aplicaciones que contengan los mismos containerPort definidos y armar un reporte.

#### BONUS ESPECIAL: Encontrar diferencias de versiones entre el input.json e input2.json y determinar la version mas nueva de cada componente con diferencias. El formato de tag de las imagenes se compone de la siguiente manera:

  registry/componente:version-fecha-hora

Las diferencias pueden ser de version (dentro del tag) o fecha.
---

Hint: En este repl se puede importar ```json``` :)