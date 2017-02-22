import pika
import sys

//python log_emit.py

if __name__ == '__main__':
    credentials = pika.PlainCredentials('artwebs','admin');
    connection = pika.BlockingConnection(pika.ConnectionParameters('artobj.dev' ,5672,'/',credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange="logs",type="fanout")
    message = ' '.join(sys.argv[1:]) or "info:Hello World"
    channel.basic_publish(exchange="logs",routing_key="",body=message)
    print " [x] Sent %r" %(message,)
    connection.close()
