# Selecciona la imagen
FROM python:3.9

# Establece la carpeta raíz dentro del contenedor
WORKDIR /app

# Copia los requirements.txt e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente al contenedor
COPY . .

# Comando por defecto para ejecutar la aplicación
CMD [ "python", "main.py" ]