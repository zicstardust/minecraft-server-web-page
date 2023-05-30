from mcstatus import JavaServer

server = JavaServer.lookup("localhost:25565")


def get_server_status():
    players = 0
    latency = 9999
    try:
        status = server.status()
        online = True
        players = status.players.online
        latency = status.latency
    except:
        online = False

    players_color = "green" if players > 0 else "red"
    latency_color = "green" if latency < 100 else "red"
    online_color = "green" if online else "red"
    online_text = "online" if online else "offline"

    server_status = [
        ["status", online_text, online_color],
        ["players", players, players_color],
        ["latency", latency, latency_color],
    ]

    return server_status
