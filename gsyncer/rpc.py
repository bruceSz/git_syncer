import pika

__all__ = [
    'init',
    'destroy',
    'get_channel'
]

connection = None
channel = None

def init(conf):
    global connection
    global channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host = conf.rabbitmq_hostname))
    channel = connection.channel()
    channel.exchange_declare(exchange=conf.exchange_name,
                             type="topic")
    
def destroy():
    global connection
    global channel
    
    connection.close()
    connection = None
    channel = None

