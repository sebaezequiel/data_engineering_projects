DO $$ BEGIN
    CREATE TYPE sentiment_type AS ENUM ('positivo', 'negativo', 'neutral');
EXCEPTION
    WHEN duplicate_object THEN NULL;
END $$;