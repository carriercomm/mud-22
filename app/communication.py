from app import app
from flask import session
from flask.ext.socketio import SocketIO, emit

socketio = SocketIO(app)


@socketio.on("communication", namespace="/mud")
def communicate(message):
    print message
    if 'logged' in session:
        if message["data"].startswith("!"):
            print "Command!"
        else:
            message["name"] = session["name"]
            emit('communication', message, broadcast=True)
    elif message["data"].startswith("!register"):
        try:
            name = message["data"].split()[1]
        except IndexError:
            server_communication("Please include a username with your request: !register USERNAME")
            return
        session["logged"] = True
        session["name"] = name
    elif message["data"].startswith("!login"):
        try:
            name = message["data"].split()[1]
        except IndexError:
            server_communication("Please include a username with your request: !login USERNAME")
            return
        session["logged"] = True
        session["name"] = name
    else:
        server_communication("Please login or register with !login USERNAME or !register USERNAME")


def server_communication(msg, broadcast=False):
    emit('communication', {"name": "Server", "data": msg}, broadcast=broadcast)
