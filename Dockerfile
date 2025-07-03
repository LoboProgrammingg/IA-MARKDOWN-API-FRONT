FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o script wait-for-it.sh
COPY wait-for-it.sh .

# Torna o script executável DENTRO do contêiner
RUN chmod +x wait-for-it.sh

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "/app/wait-for-it.sh db 5432 -- python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]