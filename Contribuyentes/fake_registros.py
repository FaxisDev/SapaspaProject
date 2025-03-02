from faker import Faker
from .models import Contribuyente   # Cambia 'myapp' por el nombre de tu aplicación
from django.contrib.auth.models import User

fake = Faker('es_MX')

def generate_fake_data():
    for _ in range(300):  # Número de registros a insertar
        folio_unico = fake.unique.random_number(digits=10)  # Genera un número único
        curp = fake.unique.bothify(text='??######???##')  # Genera un CURP falso
        nombre = fake.first_name()
        apellido_paterno = fake.last_name()
        apellido_materno = fake.last_name()
        telefono = fake.phone_number()
        correo_electronico = f"{nombre.lower()}_{folio_unico}@gmail.com"
        
        # Obtén un usuario de la base de datos, asumiendo que ya existen usuarios
        user = User.objects.first()  # Cambia esto si quieres seleccionar un usuario específico

        # Crea el objeto Contribuyente en la base de datos
        Contribuyente.objects.create(
            folio_unico=str(folio_unico),
            curp=curp,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            telefono=telefono,
            correo_electronico=correo_electronico,
            estatus="activo",
            id_user=user,
        )

if __name__ == "__main__":
    generate_fake_data()
