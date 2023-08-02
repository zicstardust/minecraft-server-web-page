from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://web_page:web_page@localhost/minecraft_server_db")
connection = engine.connect()
