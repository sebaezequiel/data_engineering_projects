from transformers import pipeline
from db_connection import get_connection
import datetime as dt

conn = get_connection()
cursor = conn.cursor()
cursor.execute("""
    SELECT * FROM smart_support.raw_tickets
    WHERE status IN ('pendiente', 'error');
""")
tickets = cursor.fetchall()
print("Ready to proces tickets")

classifier = pipeline(
    task="sentiment-analysis",
    model="finiteautomata/beto-sentiment-analysis"
)
mapeo = {
    'NEG' : 'negativo',
    'POS': 'positivo',
    'NEU': 'neutral'
}

for i in tickets:
    date = i[1]
    content = i[2]
    user_email = i[3]
    phone = i[4]
    area = i[5]
    raw_ticket_id = i[0]
    resultado = classifier(content)
    print(resultado)
    sentiment = mapeo[resultado[0]['label']]
    sentiment_score = resultado[0]['score']
    processed_date = dt.datetime.now()
    cursor.execute("""
        INSERT INTO smart_support.processed_tickets(date, content, user_email, phone, area, raw_ticket_id, sentiment, sentiment_score, processed_date)           
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (date, content, user_email, phone, area, raw_ticket_id, sentiment, sentiment_score, processed_date))
    cursor.execute("""
        UPDATE smart_support.raw_tickets
        SET status = 'procesado'
        WHERE id = %s
    """, (raw_ticket_id,))

conn.commit()
conn.close()
print("tickets processed successfully")

