# Talana Kombat

Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte .

## Instalación

1. Clona este repositorio en tu local:

   ```shell
   git clone https://github.com/JoelHe97/talana_kombat.git
   ```

2. Navega hasta el directorio del proyecto:

   ```shell
   cd talana_kombat
   ```

3. Crea un entorno virtual para el proyecto:

   ```shell
   python -m venv env
   ```

4. Activa el entorno virtual:

   - En Windows:

     ```shell
     env\Scripts\activate
     ```

   - En macOS y Linux:

     ```shell
     source env/bin/activate
     ```

5. Instala las dependencias requeridas:

   ```shell
   pip install -r requirements.txt
   ```

## Requisitos

- Python 3.10.7
- Colorama 0.4.6: Librería para imprimir texto con colores en la consola de Python.
- MyPy 1.3.0: Herramienta para realizar comprobaciones estáticas de tipado en código Python.

## Comprobación de Tipos

Este proyecto utiliza MyPy para realizar comprobaciones estáticas de tipos en el código Python. Para ejecutar MyPy, sigue estos pasos:

1. Asegúrate de que el entorno virtual esté activado.

2. Ejecuta el comando MyPy en la raíz del proyecto:

   ```shell
   mypy main.py
   ```

   Esto realizará comprobaciones estáticas de tipos en todo el código Python del proyecto y mostrará cualquier error o advertencia relacionada con el tipado.

### Ejecutar con Docker

1. Asegúrate de tener Docker instalado y corriendo en tu máquina.

2. Desde el directorio raíz del proyecto, ejecuta el siguiente comando para construir la imagen de Docker:

   ```shell
   docker build -t talana_kombat .
   ```

3. Una vez construida la imagen, ejecuta el siguiente comando para iniciar un contenedor basado en la imagen:

   ```shell
   docker run talana_kombat
   ```

## Uso

1. Ejecuta el script:

   ```shell
   python main.py
   ```