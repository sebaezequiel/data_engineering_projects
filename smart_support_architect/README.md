# Smart Support Architect

This pipeline consists in:
- Creating a database and tables to generate fake tickets
- Using Hugging Face to classify sentiment value to the content of those tickets
- Train an ML Model with this sentiment
  

## Tech Stack
- Python 3.10+
- PostgreSQL
- Hugging Face Transformers
- Scikit-learn
- Faker


## Project Structure

```text
.
├── data/
├── db/
│   ├── 01_create_schema.sql
│   ├── 02_create_types.sql
│   ├── 03_create_tables.sql
│   ├── 04_create_sentiment.sql
│   ├── 05_create_processed_tickets.sql
│   └── 06_create_views.sql
├── env/
├── jobs/
│   ├── db_connection.py
│   ├── generate_tickets.py
│   ├── init_db.py
│   ├── ticket_analysis.py
│   └── train_model.py
├── models/
│   └── sentiment_model.pkl
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

    
# .env

- Change .env.example with .env
- Add your own password


# Execution order:

1. Create the db manually

```bash
psql -U postgres
CREATE DATABASE engineering_solutions;
```

2. init_db.py (This will create schema, types and tables in PostgreSQL)
3. generate_tickets.py (This will generate 100 tickets by default in raw_tickets)
4. ticket_analysis.py (Analyze sentiment with Hugging Face and fill processed_tickets)
5. train_model.py (Train the Scikit-learn model and saves sentiment_model.pkl in models/)


# Testing the model:

```python
import joblib
modelo = joblib.load('models/sentiment_model.pkl')
resultado = modelo.predict(["spanish text"])
print(resultado)
```

  
# Future Improvements

- Add a visual diagram of the pipeline flow
- Create a shell script to run all commands automatically
- Implement error handling and exception management
- Add a YAML file with configuration