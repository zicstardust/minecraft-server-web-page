FROM python:3.13-slim

ENV SERVER_NAME="Server name"
ENV SERVER_URI_JAVA="play.exemple.com"
ENV SERVER_URI_BEDROCK="bedrock.exemple.com:3897"
ENV SERVER_MAP_URL="https://dynmap.exemple.com"
ENV DISCORD_LINK="https://discord.gg/exemple"
ENV BACKGROUND_IMAGE_URL="None"

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements-prod.txt

EXPOSE 8080

CMD [ "waitress-serve", "--port=8080", "--call", "app:production" ]