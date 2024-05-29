import pika
import os

import pika.credentials

os.system('cls')

cred = pika.PlainCredentials('mquser','mqpass')

connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=cred))

#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))#host='localhost', port=15672))
channel = connection.channel()

channel.queue_declare(queue='myqueue')
channel.basic_publish(exchange='', routing_key='myqueue', body = 'Hello World!!! 222')

print('go publush ...')

connection.close()