CREATE TABLE IF NOT EXISTS smart_support.processed_tickets ( 
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,   
    date TIMESTAMP NOT NULL,   
    content VARCHAR(255) NOT NULL,   
    user_email VARCHAR(255),  
    phone VARCHAR(255),   
    area VARCHAR(255),
    raw_ticket_id INT REFERENCES smart_support.raw_tickets(id),
    sentiment sentiment_type NOT NULL DEFAULT 'neutral',
    sentiment_score DECIMAL(5,4),
    processed_date TIMESTAMP NOT NULL
);