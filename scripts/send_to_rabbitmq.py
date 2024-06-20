# process_rabbitmq_tasks.py
import pymysql
import pika

# MySQL connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='myerp'
)

# RabbitMQ connection
rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = rabbit_connection.channel()
channel.queue_declare(queue='stock_update')

def send_to_queue(kode_barang, qty):
    message = f"{kode_barang},{qty}"
    channel.basic_publish(exchange='', routing_key='stock_update', body=message)

def process_tasks():
    with connection.cursor() as cursor:
        # Select unprocessed tasks
        cursor.execute("SELECT id, kode_barang, qty FROM rabbitmq_tasks WHERE processed = FALSE")
        tasks = cursor.fetchall()
        
        for task in tasks:
            task_id, kode_barang, qty = task
            send_to_queue(kode_barang, qty)
            
            # Mark task as processed
            cursor.execute("UPDATE rabbitmq_tasks SET processed = TRUE WHERE id = %s", (task_id,))
        
        connection.commit()

if __name__ == "__main__":
    process_tasks()



# # send_to_rabbitmq.py
# import pika
# import sys

# def send_to_queue(kode_barang, quantity):
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()

#     channel.queue_declare(queue='stock_update')

#     message = f"{kode_barang},{quantity}"
#     channel.basic_publish(exchange='', routing_key='stock_update', body=message)

#     connection.close()

# if __name__ == "__main__":
#     kode_barang = sys.argv[1]
#     quantity = sys.argv[2]
#     send_to_queue(kode_barang, quantity)
