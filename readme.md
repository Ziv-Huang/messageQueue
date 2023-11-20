
- run rabbitmq in docker:
    - 下載: `docker pull rabbitmq:management`
    - 執行: `docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management`
    - 備註: 可以在 `localhost:15672` 看到rabbitmq的管理系統

- 按照順序執行資料夾下的consumer.py 與 producer.py 即可溝通

- reference: https://hackmd.io/@SuFrank/rJ5Tgyb6q