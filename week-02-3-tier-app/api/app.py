import os

import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )


def init_db():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS notes (id SERIAL PRIMARY KEY, text TEXT NOT NULL)")


@app.get("/health")
def health():
    try:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT 1")
        return jsonify(status="ok"), 200
    except Exception:
        return jsonify(status="db unreachable"), 503


@app.get("/notes")
def list_notes():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, text FROM notes ORDER BY id")
        rows = cur.fetchall()
    return jsonify([{"id": r[0], "text": r[1]} for r in rows])


@app.post("/notes")
def add_note():
    text = (request.get_json(silent=True) or {}).get("text")
    if not text:
        return jsonify(error="'text' is required"), 400
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO notes (text) VALUES (%s) RETURNING id", (text,))
        new_id = cur.fetchone()[0]
    return jsonify(id=new_id, text=text), 201


init_db()
