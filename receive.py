import pika
import logging

if __name__ == '__main__':
    credentials = pika.PlainCredentials('artwebs', 'admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters('artobj.dev' ,5672,'/',credentials))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    print '[*] Waitting for messages. To exit press CTRL+C'
    def callback(ch,method,properties,body):
        print " [x] Received %r" % (body,)

    channel.basic_consume(callback,queue="hello",no_ack=True)
    channel.start_consuming()
