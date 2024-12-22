# minecraft-server-web-page
Simple web page to display the status of the minecraft server

## Run Docker Compose
```
services:
  mcserver-web-page:
    image: zicstardust/mcserver-web-page:latest
    restart: unless-stopped
    environment:
      SERVER_NAME: "Server name"
      SERVER_URI_JAVA: "play.exemple.com"
      SERVER_URI_BEDROCK: "bedrock.exemple.com:3897"
      SERVER_MAP_URL: "https://dynmap.exemple.com"
      DISCORD_LINK: "https://discord.gg/exemple"
    #volumes:
    #  - <PATH PNG IMAGE>:/app/static/img/background_image.png #Opcional
    ports:
      - "8080:8080"
```