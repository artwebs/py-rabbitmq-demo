import pika
import uuid

class FibonacciRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials('artwebs','admin');
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('artobj.dev' ,5672,'/',credentials))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_respone,no_ack=True,queue=self.callback_queue)
    def on_respone(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.respone = body

    def call(self,n):
        self.respone = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',routing_key='rpc_queue',properties=pika.BasicProperties(reply_to=self.callback_queue,correlation_id=self.corr_id,),body=str(n))
        while self.respone is None:
            self.connection.process_data_events()
        return int(self.respone)

if __name__ == '__main__':
    fibonacci_rpc = FibonacciRpcClient()
    respone = fibonacci_rpc.call(30)
    print " [.] Got %r"%(respone,)
