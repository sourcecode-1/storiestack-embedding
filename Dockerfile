FROM python:3.10-slim

# 1. Install dependencies
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy your code
COPY . .

# 3. Expose the port that Flask uses
ENV PORT=7840
EXPOSE 7840

# 4. Run your app
CMD ["gunicorn", "--bind", "0.0.0.0:7840", "app:app", "--workers", "1", "--threads", "1"]

