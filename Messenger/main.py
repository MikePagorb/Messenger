import time

db = [
    {
        'time' : time.time(),
        'name' : 'Jack',
        'text' : 'Hello everyone',
    },
    {
        'time': time.time(),
        'name': 'Jack',
        'text': 'Hello everyone',
    },
]

def send_message(name, text):
    message = {
        'time': time.time(),
        'name': name,
        'text' : text,
    }
    db.append(message)

def get_messages(after):
    """messages from db after given time stamp"""
    result = []
    for messsage in db:
        if messsage['time'] > after:
            result.append(messsage)
    return result

print(db)
t1 = db[-1]['time']
print(get_messages(t1))

time.sleep(0.01)
send_message('123','123')
send_message('123','456')
print(get_messages(t1))

t2 = db[-1]['time']
print(get_messages(t2))

time.sleep(0.01)
send_message('123','789')
print(get_messages(t2))

# send message == положить message в db
# get messages == достать из db сообщения,
# которые не подгружены на клиенте