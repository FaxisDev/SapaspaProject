from faker import Faker
from Contribuyentes.models import Contribuyente
from .models import Propiedad, TipoPropiedad
from django.db import transaction

fake = Faker('es_MX')  # Usamos el locale de México para generar datos latinos

# Función para generar propiedades aleatorias
def generate_property_data():
    # Obtener los contribuyentes que no tienen propiedad asociada
    contribuyentes_sin_propiedad = Contribuyente.objects.filter(propiedad__isnull=True)

    # Si no hay contribuyentes sin propiedad, retornar
    if not contribuyentes_sin_propiedad:
        print("No hay contribuyentes sin propiedad.")
        return

    # Obtener tipos de propiedad disponibles
    tipo_propiedad = TipoPropiedad.objects.all()

    # Crear propiedades para los contribuyentes sin propiedad
    for contribuyente in contribuyentes_sin_propiedad:
        # Generar datos ficticios para la propiedad
        propiedad = Propiedad(
            numero_interior=fake.unique.random_number(digits=2) if fake.boolean() else None,
            numero_exterior=fake.random_number(digits=3),
            calle=fake.street_name(),
            entre_calles=f"{fake.street_name()} & {fake.street_name()}",
            colonia=fake.random_element(["San Pablo Atlazalpan", "Jazmin", "Cantorías", "Candelaria", "El Recodo", "El Carcamo", "Lomas de San Pablo", "San Jose", "La Michoacana"]),
            ciudad="Chalco",
            estado="Estado de México",
            codigo_postal=56620,
            referencias=fake.sentence(),
            tipo_propiedad=fake.random_element(tipo_propiedad),
            contribuyente=contribuyente
        )

        # Guardar la propiedad
        propiedad.save()

        print(f"Propiedad {propiedad.id} asociada a Contribuyente {contribuyente.id}.")

# Llamar la función
if __name__ == "__main__":
    with transaction.atomic():  # Usar transacción para asegurar que todo se guarda correctamente
        generate_property_data()
