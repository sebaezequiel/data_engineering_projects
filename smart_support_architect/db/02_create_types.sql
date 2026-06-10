DO $$ BEGIN
    CREATE TYPE ticket_status AS ENUM ('pendiente', 'procesado', 'error');
EXCEPTION
    WHEN duplicate_object THEN NULL;
END $$;