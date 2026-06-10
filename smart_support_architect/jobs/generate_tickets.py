from db_connection import get_connection
import random
from faker import Faker

NUM_TICKETS = 100
print(f"{NUM_TICKETS} tickets to process")

tickets = [
    ("Técnico", "Llevan 5 días sin resolver mi problema con la API. Hice un ticket antes, lo cerraron como resuelto y sigue sin funcionar. Esto es una falta de respeto."),
    ("Técnico", "El sistema sigue agregando caracteres especiales en los reportes sin que yo los escriba. Ya reporté esto tres veces y nadie da una solución concreta."),
    ("Técnico", "La API no está funcionando correctamente desde ayer. Adjunto logs del error para que puedan revisarlo."),
    ("Técnico", "Hay un error en producción, entiendo que el equipo está ocupado, solo aviso para que se pueda solucionar lo antes posible. Gracias."),
    ("Facturación", "Me cobraron dos veces el mismo servicio este mes. Exijo una devolución inmediata. Si no se resuelve hoy llamo a mi banco."),
    ("Facturación", "La factura de este mes tiene un monto incorrecto, es el tercer mes consecutivo que pasa esto. Estoy harto de tener que llamar siempre."),
    ("Facturación", "Quisiera solicitar una factura rectificativa por el mes de abril. El monto facturado no coincide con el plan contratado."),
    ("Facturación", "Necesito actualizar los datos de facturación de mi cuenta. ¿Podrían indicarme cómo hacerlo?"),
    ("Ventas", "Me vendieron un plan diciéndome que incluía soporte 24hs y resulta que no es así. Me siento estafado, quiero hablar con un supervisor."),
    ("Ventas", "Contraté el plan premium hace una semana y todavía no me activaron todas las funcionalidades prometidas. Nadie me da respuestas claras."),
    ("Ventas", "Quisiera información sobre los planes disponibles para empresas. Somos un equipo de 10 personas y estamos evaluando opciones."),
    ("Ventas", "Estoy muy conforme con el servicio hasta ahora. Me gustaría conocer qué opciones hay para hacer un upgrade de mi plan actual.")
]

conn = get_connection()
cursor = conn.cursor()
fake = Faker()

for i in range(NUM_TICKETS):
    ticket = random.choice(tickets)
    area = ticket[0]
    contenido = ticket[1]
    fecha = fake.date()
    email = fake.email()
    telefono = fake.phone_number()
    cursor.execute("""
        INSERT INTO smart_support.raw_tickets(date, content, user_email, phone, area)
        VALUES (%s, %s, %s, %s, %s)
    """, (fecha, contenido, email, telefono, area))

conn.commit()
conn.close()
print(f"{NUM_TICKETS} tickets inserted successfully")
