#!/usr/bin/env python
import os
import pika

host = os.environ['BROKER_HOST']
rabbituser = os.environ['RABBIT_USER']
rabbitpass = os.environ['RABBIT_PASS']
queuename = 'hello'

def callback(channel, method, properties, body):
	print(" [x] Received %r" % body)

credentials = pika.PlainCredentials(rabbituser,rabbitpass)
connection = pika.BlockingConnection(pika.ConnectionParameters(host,5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue=queuename)

channel.basic_consume(callback,queue=queuename,no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

