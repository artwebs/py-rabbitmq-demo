import pika
import sys

# python log_direct_emit.py 
# python log_direct_emit.py warning
# python log_direct_emit.py error

if __name__ == '__main__':
    credentials = pika.PlainCredentials('artwebs','admin');
    connection = pika.BlockingConnection(pika.ConnectionParameters('artobj.dev' ,5672,'/',credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs',type='direct')
    severity = sys.argv[1] if len(sys.argv) >1 else 'info'
    message = ' '.join(sys.argv[2:]) or 'Hello World'
    channel.basic_publish(exchange='direct_logs',routing_key=severity,body=message)
    print " [x] Sent %r:%r" %(severity,message)
    connection.close()
