import pika, json

params = pika.URLParameters('amqps://nhusqpli:UFpbN0AEgSSAA5voYK7g1g2t0tTVzqMt@gull.rmq.cloudamqp.com/nhusqpli')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)