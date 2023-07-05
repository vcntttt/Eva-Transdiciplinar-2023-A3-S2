
# Eva-Transdiciplinar-2023-A3-S2
**Alumnos** : Joaquín Cantero, Franco Oyarzo, Javier Poblete, Vicente Rivera

**Carrera** : Ingeniería Civil Informática

**Asignatura** : Programación 1 - Física

## Descripción
El objetivo de este proyecto es calcular el trabajo que se realiza en un objeto (en nuestro caso usaremos un cuadrado), mediante los 2 métodos que se nos solicitaron a través de un programa de python, buscando realizar los cálculos de las formulas de la manera mas eficaz y rápida posible, dando resultados numéricos exactos y representaciones graficas al instante.

## Evento físico a simular
Nuestro proyecto busca demostrar como es el movimiento que realiza un objeto cuando se le transfiere energía mecánica (Trabajo).

## Origen
El grupo decidió encontrar una forma sencilla y rápida de hacer los cálculos relacionados con el trabajo y la energía. Se quiere crear una aplicación que diera resultados precisos, rápidos y claros, que además mostrará una simulación de cómo se verían las diferentes fuerzas y movimientos que se realizan.
### Trabajo
El concepto de trabajo ha sido modificado a lo largo de la historia, pero la formulación matemática y cuantitativa del trabajo, se atribuye a los científicos Galileo Galilei y Evangelista Torricelli en el siglo XVII en la comunidad científica. Estos investigadores comenzaron a investigar las leyes del movimiento y la conexión que existe entre la fuerza y el desplazamiento de los objetos.
### Energía
El concepto de energía también ha ido evolucionando con el tiempo, como bien sabemos uno de los hitos mas importantes para la física fue el desarrollo de la **ley de conservación de la energía**, que fue formulada por el físico alemán **Julius Robert Von Mayer(1814 - 1878)** en el año 1842.
> " La energía no se crea ni se destruye, solo se puede transformar de una forma a otra"

Posteriormente fue desarrollada de manera independiente por el físico ingles **James Prescott Joule(1818 - 1889)**, conocido por sus investigaciones y trabajos en electricidad, termodinámica y energía, paso a realizar experimentos que relacionan el trabajo mecánico con el calor, lo que provoco la idea de que la energía mecánica y la creación de la unidad de medida **Joules**.
## Matemática Empleada
El trabajo y energía, están relacionados entre si, como se menciono anteriormente ya que se establece que el trabajo realizado sobre un objeto va a ser igual al cambio en su energía cinética, por lo tanto, tenemos varias formulas para calcular tanto el trabajo como la energía cinética.

-**Trabajo**: El trabajo se define como la cantidad de energía que se transmite de un objeto o sistema debido a la aplicación de fuerza a lo largo de una distancia. El trabajo se calcula mediante las fórmulas:

$$
W = F \cdot D \cdot \cos(\theta)
$$

$$
W = \Delta E_c
$$

$$
\Delta E_c = E_{cf} - E_{ci}
$$

Donde:
- $W$ = Trabajo realizado.
- $F$ = Magnitud de la fuerza aplicada.
- $D$ = Distancia sobre la cual se le aplica la fuerza.
- $\theta$ = Angulo formado entre la dirección de la fuerza y la dirección del desplazamiento.

He de aclarar que cada formula se usara dependiendo de los datos que tengamos a nuestra disposición y en caso de no tener ningún dato de la formula original del trabajo lo podemos calcular a través de la **Energía Cinética**.
- **Energía Cinética**: Es una energía que esta asociada con el movimiento de un objeto, debido a su masa y velocidad. Cuanta mas velocidad tenga el objeto o cuanto mayor sea la masa, mayor será la energía cinética de este, la formula es: 

$$
E_c = \frac12m \cdot v^2
$$

Donde:
- $E_c$ = Energía cinética
- $m$ = Masa del objeto
-  $v$ = velocidad del objeto 

Si recordamos, el trabajo se define como la variación de la energía cinética por lo tanto también se puede calcular de la siguiente manera:

$$
W = \Delta E_c
$$

$$
\Delta E_C = E_cf - E_ci
$$

Donde: 
- $W$ = Trabajo
- $\Delta E_C$ = Variación de la energía cinética
- $E_ci$ = Energía cinética inicial
- $E_cF$ = Energía cinética final

## Como se resuelve
Para poder resolver ejercicios de trabajo y energía debemos realizar una serie de pasos:
    

-   Identificar la información proporcionada: Antes de resolver algún ejercicio debemos leer bien el enunciado e identificar la información relevante para resolver el ejercicio.
    
-   Determinar lo que se pide calcular: Una vez tengamos la información relevante, necesitamos identificar qué es lo que se necesita calcular, para así saber las fórmulas que vamos a necesitar.
    
-   Aplicar las fórmulas adecuadas: Cuando tengamos los datos y sabemos lo que debemos calcular, debemos identificar las fórmulas que necesitamos para llegar al resultado que buscamos.
    
-   Realizar los cálculos: Finalmente debemos reemplazar los valores que identificamos en las fórmulas y realizar los cálculos necesarios para obtener el resultado.
    

- Verificar el resultado: Ya para finalizar, si aún tenemos dudas podemos verificar el resultado reemplazando datos en ecuaciones previas a la que te llevó al resultado.

## Aplicaciones
Se utilizan para calcular la energía cinética y potencial, así como para determinar la cantidad de trabajo realizado por las fuerzas en diferentes situaciones. Esto es útil para analizar el rendimiento de máquinas, calcular la velocidad de un objeto en movimiento o estudiar la caída de objetos en campos gravitacionales. Por ejemplo se utilizan para calcular la energía requerida en procesos industriales, rendimiento de máquinas y motores, así como para determinar los esfuerzos y deformaciones en estructuras bajo cargas, además son fundamentales para el diseño y análisis de sistemas y estructuras. Y así se pueden seguir nombrando numerosas aplicaciones que tienen la energía y el trabajo en distintas áreas.
## Programación
 ### Descripción de las herramientas utilizadas:
Se utilizó el lenguaje de programación **“Python”**. 

- Python es un lenguaje de programación de alto nivel, interpretado y utilizado en una amplia variedad de aplicaciones, se caracteriza por su sintaxis clara y legible, lo que facilita su aprendizaje y comprensión.
   
- **Tkinter**: Es un módulo incorporado en Python que se utiliza para crear aplicaciones de escritorio con interfaces gráficas. Proporciona varios controles y widgets (ventanas) que se pueden utilizar para diseñar la interfaz de usuario.

- **ttkbootstrap**: Es una biblioteca de temas para Tkinter que proporciona una apariencia mejorada a los elementos de la GUI (interfaz gráfica del usuario). Se utiliza para establecer el tema de la ventana principal.

- **PIL (Python Imaging Library)**: Es una biblioteca de procesamiento de imágenes en Python. Se utiliza aquí para capturar una captura de pantalla de la ventana de la aplicación.

- link explicativo del codigo: [Explicacion del Codigo](https://youtu.be/ungINfVGpe8) y [Explicacion del Codigo Parte 2](https://youtu.be/73fdcocVn3Y)
## Guía de Instalación
Primero que nada, nos tenemos que asegurar de tener [Python 3.11](https://www.python.org/downloads/), [Git](https://git-scm.com/downloads) y algún editor de código, de preferencia, [Visual Studio Code](https://code.visualstudio.com/download). Tenemos que ejecutar un par de comandos, para esto podemos usar la consola predeterminada de nuestro sistema, o en cambio, podemos utilizar la terminal integrada de Visual Studio Code, nosotros recomendamos esta ultima opción.

1.Clonar el repositorio utilizando el comando:

    git clone  https://github.com/vcntttt/Eva-Transdiciplinar-2023-A3-S2.git
 
2.Instalar las dependencias utilizadas en este proyecto con el comando, recuerde tener la consola en la que va a ejecutar el comando dentro del repositorio clonado (en caso de estar utilizando la terminal integrada de **vscode**, la consola se posiciona directamente en la carpeta)  :

    pip install -r requirements.txt
 
3. Ejecutar 😎.
4. Se adjuntara un link explicando la guia de instalacion a continuacion:
   [Guia de Instalacion](https://www.youtube.com/watch?v=qD4JyWkhpxs)
5. Se adjuntara un link al video tutorial de uso a continuación:
   [Uso de Aplicacion y Modelo Fisico](https://www.youtube.com/watch?v=zvMCDFs9r94)

## Conclusiones
El proyecto demuestra una sólida investigación y entendimiento de los conceptos físicos de trabajo y energía. Se investigaron y aplicaron fórmulas matemáticas para el cálculo del trabajo, considerando la magnitud de la fuerza aplicada, la distancia recorrida y el ángulo entre la dirección de la fuerza y el desplazamiento. Además, se utilizó la fórmula de la energía cinética, que está relacionada directamente con el trabajo realizado sobre un objeto.
Lo que a su vez condujo hacia la integración de la programación en Python que permitió automatizar los cálculos y la simulación del movimiento del objeto. Se investigaron y emplearon las bibliotecas tkinter, ttk bootstrap y PIL para desarrollar una interfaz gráfica de usuario intuitiva y atractiva, lo que entregó una capacidad para crear una interfaz visual mejorada que contribuyó a la experiencia del usuario y facilitó la interacción con el programa.
Queremos destacar que el proyecto también abordó la instalación y gestión de las dependencias, lo cual es fundamental para la correcta ejecución del código. Se proporcionó en base al conocimiento y experiencia del equipo una guía de instalación detallada, asegurando que todas las bibliotecas necesarias estuvieran disponibles y correctamente configuradas.
En conclusión el proyecto fue atenuante y desafiante, pero evidenció un aprendizaje sólido en cuanto a la comprensión de los conceptos físicos, la aplicación de fórmulas matemáticas y la integración de la programación en Python, que sin duda sin nuestros conocimientos previos a este último, nos hubiera complicado mucho más su desarrollo, evidenciando lo mucho que se ha aprendido a través de estos meses de clases.
