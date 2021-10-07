from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json

class SendMessageQueue:

    # def send_single_message(self, sender, message):
    #     print(message)
    #     # create a Service Bus message
    #     message = ServiceBusMessage(json.dumps(message))
    #     message.content_type = "application/json"
    #     # send the message to the queue
    #     sender.send_messages(message)

    # def send_message(self, queue, azure_queue, data):
    #     print(queue)
    #     servicebus_client = ServiceBusClient.from_connection_string(conn_str=azure_queue, logging_enable=True)
    #     with servicebus_client:
    #         sender = servicebus_client.get_queue_sender(queue_name=queue)
    #         with sender:
    #             self.send_single_message(sender, data)


    def send_single_message(self, sender, message):
        # create a Service Bus message
        message = ServiceBusMessage(json.dumps(message))
        message.content_type = "application/json"
        # send the message to the queue
        sender.send_messages(message)

    def scheduled_single_message(self, sender, message, date_time):
        # create a Service Bus message
        message = ServiceBusMessage(json.dumps(message))
        message.content_type = "application/json"
        # send the message to the queue
        sender.schedule_messages(message, date_time)

    def send_message(self, queue, azure_queue, data, date_time=None):
        servicebus_client = ServiceBusClient.from_connection_string(conn_str=azure_queue, logging_enable=True)
        with servicebus_client:
            sender = servicebus_client.get_queue_sender(queue_name=queue)
            with sender:
                if date_time == None:
                    self.send_single_message(sender, data)
                else:
                    self.scheduled_single_message(sender, data, date_time)