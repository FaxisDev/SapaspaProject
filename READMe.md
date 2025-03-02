# SAPASPA

Bienvenido a la plataforma de gestión de pago de agua para el pueblo de San Pablo Atlalzapan. Nuestra aplicación web facilita el proceso de pago de servicios de agua de manera eficiente y conveniente, mejorando la experiencia para los residentes de nuestra comunidad.

#Características Principales
1. Pago en Línea Seguro
Realiza tus pagos de agua de manera segura y conveniente desde la comodidad de tu hogar. Aceptamos múltiples métodos de pago para adaptarnos a tus preferencias.

#2. Historial de Pagos
Mantén un registro detallado de tus pagos anteriores. Accede fácilmente a tu historial para un seguimiento transparente de tus transacciones.

#3. Notificaciones Automáticas
Recibe notificaciones automáticas sobre fechas de vencimiento, cambios en tarifas y otros anuncios importantes relacionados con el suministro de agua en San Pablo Atlalzapan.
## Despliegue del Proyecto Django

A continuación se detallan los pasos para desplegar el proyecto Django.

### Requisitos Previos

- Python (versión recomendada)
- Virtualenv (opcional pero se recomienda)
- [Otras dependencias del sistema, si las hay]

### Pasos de Despliegue

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-proyecto.git
   cd tu-proyecto


# Instalar virtualenv si no lo tienes
pip3 install virtualenv

## Si no existe el archivo venv lo generamos con
python3 -m virtualenv venv

# Activar el entorno virtual (Linux/macOS)
source venv/bin/activate

# Activar el entorno virtual (Windows)
.\venv\Scripts\activate

# Instalar dependencias en el proyecto
pip3 install -r requirements.txt

# Desactivar el entorno virtual
deactivate

#Generar el archivo requirements.txt:
##Una vez que el entorno virtual esté activado, puedes utilizar el siguiente comando para guardar la lista de paquetes instalados en requirements.txt:

``` pip3 freeze > requirements.txt  ```

## Para Generar el archivo .dot para modelo relacional actual es
 ``` python3 manage.py graph_models -a -o my_models.dot  ```

#El resultado de codigo lo pegamos en el sitio:
https://dreampuf.github.io/GraphvizOnline/

#Generar Registros Aleatorios
## Para Contribuyentes:
``` python3 manage.py shell -c "from Contribuyentes.fake_registros import generate_fake_data; generate_fake_data()" ```

## Para Propiedades:
``` python3 manage.py shell -c "from Propiedades.fake_registros import generate_property_data; generate_property_data()" ```

