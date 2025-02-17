import eventlet
import socketio
from eventlet import wsgi
from loguru import logger

from classes.player import Player

# Заставляем работать пути к статике
static_files = {'/': 'static/index.html', '/static': './static'}
sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')
app = socketio.WSGIApp(sio, static_files=static_files)

players = {}


# Обрабатываем подключение пользователя
@sio.event
def connect(sid, environ):
    logger.info(f"Пользователь {sid} подключился")
    players[sid] = Player()


@sio.on('next')
def next_event(sid, data):
    player = players.get(sid)
    if not player:
        return

    riddle = player.get_next_riddle()
    if riddle:
        sio.emit('riddle', riddle, to=sid)
    else:
        sio.emit('over', data, to=sid)
        sio.emit('score', data={'value': 0}, to=sid)
        player.reset_game()


# Обрабатываем отправку ответа
@sio.on('answer')
def receive_answer(sid, data):
    player = players.get(sid)
    if not player or not data:
        return

    answer = data.get('text', '').strip()
    result = player.check_answer(answer)

    sio.emit('result', data=result, to=sid)
    sio.emit('score', data=player.get_score(), to=sid)


# Обрабатываем отключение пользователя
@sio.event
def disconnect(sid):
    players.pop(sid)
    logger.info(f"Пользователь {sid} отключился")


if __name__ == '__main__':
    wsgi.server(eventlet.listen(("127.0.0.1", 8000)), app)
