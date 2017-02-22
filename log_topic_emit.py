import pika
import sys
# python log_topic_emit.py "love"
# python log_topic_emit.py "artwebs.more"

if __name__ == '__main__':
    credentials = pika.PlainCredentials('artwebs','admin');
    connection = pika.BlockingConnection(pika.ConnectionParameters('artobj.dev' ,5672,'/',credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange='topic_logs',type='topic')
    routing_key = sys.argv[1] if len(sys.argv)>1 else 'anonymous.info'
    message = ' '.join(sys.argv[2:]) or 'Hello World!'
    channel.basic_publish(exchange='topic_logs',routing_key=routing_key,body=message)
    print " [x] Sent %r:%r"%(routing_key,message)
    connection.close()
