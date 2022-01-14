/* --------------------------------------------- */ 
/* AUTOMATICALLY IMPORT SCHEMAS DURING DB LAUNCH */
/* --------------------------------------------- */ 

/* Extension For Password Encryption And Randomized UUID Gen*/
CREATE EXTENSION IF NOT EXISTS pgcrypto;

/* Schema For tbl_users */
CREATE TABLE IF NOT EXISTS shortened_urls (
  id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
  original_url VARCHAR(255) NOT NULL,
  short_link VARCHAR(10) NOT NULL,
  short_link_create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(short_link)
);

CREATE UNIQUE INDEX ix_shortened_urls_short_link ON shortened_urls (short_link);
