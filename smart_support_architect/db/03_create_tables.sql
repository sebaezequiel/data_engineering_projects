CREATE TABLE IF NOT EXISTS smart_support.raw_tickets ( 
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,   
    date TIMESTAMP NOT NULL,   
    content VARCHAR(255) NOT NULL,   
    user_email VARCHAR(255),  
    phone VARCHAR(255),   
    area VARCHAR(255),   
    status ticket_status NOT NULL DEFAULT 'pendiente'  
);