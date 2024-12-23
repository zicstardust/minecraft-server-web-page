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
      SERVER_URI_BEDROCK: "bedrock.exemple.com:19132"
      SERVER_MAP_URL: "https://dynmap.exemple.com"
      DISCORD_LINK: "https://discord.gg/exemple"
      # BACKGROUND_IMAGE_URL: "https://exemple.com/image" #Opcional
    ports:
      - "8080:8080"
```