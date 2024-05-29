import os, sys, pika

os.system('cls')

def main():
    print('start main')
    cred = pika.PlainCredentials('mquser','mqpass')
    connect = pika.BlockingConnection(pika.ConnectionParameters(credentials=cred))

    cannel = connect.channel()
    cannel.queue_declare('myqueue')

    def callback(ch, metchode, properties, body):
        print(f"[x] message{body}")

    cannel.basic_consume(queue='myqueue', on_message_callback = callback, auto_ack = True)
    cannel.start_consuming()

if (__name__ == '__main__'):
    try:
        main()
    except KeyboardInterrupt:
      try:
        print('KeyboardInterrupt')
        sys.exit(0)
      except SystemExit:
        os._exit(0)