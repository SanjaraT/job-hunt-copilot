import psycopg2
import psycopg2.extras
from contextlib import contextmanager
from app.config import DATABASE_URL

@contextmanager
def get_connection():
    conn = psycopg2.connect(DATABASE_URL)

    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users(
id SERIAL PRIMARY KEY,
email TEXT UNIQUE NOT NULL,
hashed_password TEXT NOT NULL,
resume_text TEXT,
created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE F NOT EXISTS jobs (
id SERIAL PRIMARY KEY,
source TEXT NOT NULL,
title TEXT NOT NULL,
company TEXT,
url TEXT UNIQUE NOT NULL,
description TEXT,
posted_at TEXT,
scraped_at TIMESTAMPTZ DEFAULT noW()
);

CREATE IF NOT EXISTS matches(
id SERIAL PRIMARY KEY,
user_id INTEGER NOT NULL RFERENCES users(id) ON DELETE CASCADE,
job_id INTEGER NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
relevance_score INTEGER,
rational TEXT,
created_at TIMESTAMPTZ DEFAULT now(),
UNIQUE(user_id, job_id)
);

CREATE TABLE IF NOT EXISTS applications(
id SERIAL PRIMARY KEY,
user_id INTEGER NOT NULL REFERENCES user(id) ON DELETE CASCADE,
job_id INTEGER NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
status TEXT DEFAULT 'saved',
applied_at timestamptz,
note TEXT,
UNIQUE (user_id, job_ID)
);


CREATE INDEX IF NOT EXISTS idx_matches_user_id ON matches(user_id;
CREATE INDEX IF NOT EXISTS idx_applications_user_id ON applications(user_id);
"""
def init_schema():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(SCHEMA_SQL)
