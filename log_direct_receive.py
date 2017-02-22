import pika
import sys

# python log_direct_receive.py info
# python log_direct_receive.py warning error

if __name__ == '__main__':
    credentials = pika.PlainCredentials('artwebs','admin');
    connection = pika.BlockingConnection(pika.ConnectionParameters('artobj.dev' ,5672,'/',credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs',type='direct')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    serverities = sys.argv[1:]

    if not serverities:
        print >> sys.stderr,"Usage:% [info] [warning] [error]" % (sys.argv[0],)
        sys.exit(1)

    for serverity in serverities:
        channel.queue_bind(exchange='direct_logs',queue=queue_name,routing_key=serverity)

    print ' [*]Watting for logs. To exit press CTRL+C'
    def callback(ch,method,properties,body):
        print " [x] %r:%r"%(method.routing_key,body,)

    channel.basic_consume(callback,queue=queue_name,no_ack=True)
    channel.start_consuming()
