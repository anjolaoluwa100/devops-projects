# ---------- Stage 1: build ----------
FROM python:3.12-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Stage 2: runtime ----------
FROM python:3.12-alpine
WORKDIR /app
RUN addgroup -S app && adduser -S app -G app
COPY --from=builder /install /usr/local
COPY app.py .
USER app
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--preload", "app:app"]
