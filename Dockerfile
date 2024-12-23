FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements-prod.txt

EXPOSE 8080

CMD [ "waitress-serve", "--port=8080", "--call", "app:production" ]