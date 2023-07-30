# Proyecto_Final_curso_python
### Hi there 👋 William Elí
<h2>Curso de Python Básico a Intermedio</h2>
<h3>
      <b>Nombre del Proyecto: Obtención de Precios y Gráfico de Barras.</b>
</h3>
<h3>Descripcion:</h3>
<p>Este proyecto tiene como objetivo obtener los precios de tres artículos diferentes desde sus respectivas páginas web y generar un gráfico de barras para visualizar y comparar los precios de manera más clara. Para lograr esto, se utiliza Python junto con las bibliotecas `requests`, `BeautifulSoup` y `matplotlib`.
</p>
 <h3>Funcionalidad</h3>
 <p>El proyecto consta de dos partes principales:</p>
 <p>1.- Obtención de Precios desde Páginas Web</p>
 <p>- Se accede a las páginas web de los tres artículos mediante las URLs proporcionadas en las variables `url`, `url1` y `url2`.</p>
 <p>- Utilizando la biblioteca `requests`, se realiza una solicitud HTTP a cada página y se guarda el contenido HTML en las variables `page`, `page1` y `page2`.</p>
 <p> - Luego, con la ayuda de `BeautifulSoup`, se analiza el código HTML y se extraen las partes que contengan las etiquetas `<span>` con el atributo `class="andes-money-amount__fraction"`.</p>
 <p> - Estas partes se convierten en strings para poder ser procesadas más fácilmente.</p>
   <p>2.- Generación del Gráfico de Barras</p>
   <p>- Se crean objetos `BeautifulSoup` a partir de los strings que contienen las partes relevantes del código HTML (almacenadas en las variables `chango`, `chango1` y `chango2`).</p>
   <p>- Utilizando `BeautifulSoup`, se busca la etiqueta `<span>` que contiene el precio en cada objeto.</p>
   <p>- Se obtiene el texto que se encuentra dentro de la etiqueta `<span>`, el cual corresponde al precio del artículo.</p>
   <p>- Se eliminan las comas de los precios (para representar los miles) y se convierten a números enteros utilizando `int()`.</p>
     <p>- Finalmente, los precios y nombres de los artículos se almacenan en listas (`precios` y `articulos`, respectivamente), y se grafican en un gráfico de barras utilizando `matplotlib`.</p>
    
