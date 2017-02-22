import pika
import time

if __name__ == '__main__':
    credentials = pika.PlainCredentials('artwebs','admin');
    connection = pika.BlockingConnection(pika.ConnectionParameters('artobj.dev' ,5672,'/',credentials))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue',durable=True)
    print ' [*] Waitting for messages.To exit press CTRL+C'

    def callback(ch,method,properties,body):
        print " [x] Received %r"%(body,)
        time.sleep(body.count('.'))
        print " [x] done"
        ch.basic_ack(delivery_tag=method.delivery_tag)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,queue='task_queue')
    channel.start_consuming()
