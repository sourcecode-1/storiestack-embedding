FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# No need to EXPOSE — HF handles port
# CMD sh -c "gunicorn -b 0.0.0.0:${PORT} app:app --workers 1 --threads 1"
ENV PORT=7860
CMD gunicorn -b 0.0.0.0:$PORT app:app --workers 1 --threads 1

