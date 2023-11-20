import time

from domain.subscribe.consumer import consumer
from domain.subscribe.producer import producer


if __name__ == "__main__":
    c = consumer.new_consumer()
    p = producer.new_producer()

    c.basic_consume()
    p.basic_publish("aaaaaaaaaaa")

    time.sleep(3)
