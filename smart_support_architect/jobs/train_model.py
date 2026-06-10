from db_connection import get_connection
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib
import os

conn = get_connection()

query = "SELECT content, sentiment FROM smart_support.processed_tickets"
df = pd.read_sql(query, conn)

df['content_clean'] = df['content'].apply(lambda x: re.sub(r'[^a-záéíóúüñ\s]', '', x.lower()))

X = df['content_clean']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clasificador', MultinomialNB())
])

modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
print(classification_report(y_test,y_pred))

base_path = os.path.dirname(__file__)
models_path = os.path.join(base_path, "..", "models")
sentiment_model_path = os.path.join(models_path, "sentiment_model.pkl")
joblib.dump(modelo, sentiment_model_path)

