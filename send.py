#!/usr/bin/env python
import os
import pika
import random
import string
import time
import datetime

host = os.environ['BROKER_HOST']
rabbituser = os.environ['RABBIT_USER']
rabbitpass = os.environ['RABBIT_PASS']
queuename = 'hello'
sleeptime=3
counter=1

while True:
	credentials = pika.PlainCredentials(rabbituser,rabbitpass)
	connection = pika.BlockingConnection(pika.ConnectionParameters(host,5672,'/',credentials))
	channel = connection.channel()

	channel.queue_declare(queue=queuename)

	channel.basic_publish(exchange='',routing_key=queuename,body='Message Number: '+str(counter))
	connection.close()

	print(datetime.datetime.now().strftime("%c"),": Sent to "+host)
	counter=int(counter)+1
	time.sleep(int(sleeptime))
