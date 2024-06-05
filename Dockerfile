FROM python:3.10-slim

WORKDIR /app

COPY .env .

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 8080

CMD ["streamlit", "run", "main.py"]