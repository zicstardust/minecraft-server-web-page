FROM python:3.13

ENV SERVER_NAME='Server name'
ENV SERVER_URI_JAVA="127.0.0.1:25565"
ENV SERVER_URI_BEDROCK="127.0.0.1:19132"
ENV SERVER_MAP_URL="http://127.0.0.1:9980"
ENV DISCORD_LINK="https://discord.gg/blabla"

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python", "app.py" ]