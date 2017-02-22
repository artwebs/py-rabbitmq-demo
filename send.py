import pika
if __name__ == '__main__':
    parameters = pika.URLParameters('amqp://artwebs:admin@artobj.dev:5672/%2F')
    connection = pika.BlockingConnection(parameters)
    # credentials = pika.PlainCredentials('artwebs', 'admin')
    # connection = pika.BlockingConnection(pika.ConnectionParameters('artobj.dev' ,5672,'/',credentials))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
    routing_key='hello',
    body='Hello World')
    print "[x] Sent 'Hello World'"
    connection.close()
