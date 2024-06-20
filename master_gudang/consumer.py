# master_gudang/consumers.py
import pika
from master_gudang.models import MasterGudang

def callback(ch, method, properties, body):
    kode_barang_transaksi, quantity = map(int, body.decode().split(','))
    try:
        product = MasterGudang.objects.get(kode_barang=kode_barang_transaksi)
        product.qty -= quantity
        product.save()
    except MasterGudang.DoesNotExist:
        pass

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='stock_update')

    channel.basic_consume(queue='stock_update', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    start_consumer()
