from datetime import datetime

from domain.queue_element import QueueElement
from repository.queue.navitaire import QueueRepository

class QueuElement:
    def __init__(self, queue_repository: QueueRepository):
        self.__queue_repository = queue_repository

    def execute(self) -> QueueElement:
        queue_element = self.__queue_repository.next_in_queue()
        if not queue_element["data"]["recordLocator"]:
            return
        record_locator = queue_element["data"]["recordLocator"]
        item_key = queue_element["data"]["bookingQueueItemKey"]
        print(f"Record locator: {record_locator}")
        print(f"Item key: {item_key}")
        try:
            booking_retrieve = self.__queue_repository.retrieve_by_record_locator(record_locator)
            journeys = booking_retrieve["data"]["journeys"]
            booking_key = booking_retrieve["data"]["bookingKey"]
            journey_to_endose = ''
            flights_to_endose = []
            passengers = self.__queue_repository.passenger_keys()
            passenger_keys = list(passengers["data"].keys())
            for journey in journeys:
                journey_key = journey["journeyKey"]
                flight_numbers = []
                check_ssr = False
                for segment in journey["segments"]:
                    flight_numbers.append(segment["identifier"]["identifier"])
                    for passenger in passenger_keys:
                        ssrs = segment["passengerSegment"][passenger]["ssrs"]
                        for ssr in ssrs:
                            if ssr["ssrCode"] == "FELA":
                                journey_to_endose = journey_key
                                check_ssr = True
                if check_ssr:
                    segment = journey["segments"][0]
                    fares = {}
                    fare = segment["fares"][0] 
                    for passegnger_fare in fare["passengerFares"]:
                        passenger_type = passegnger_fare["passengerType"]
                        service_charges = []
                        for service_charge in passegnger_fare["serviceCharges"]:
                            service_charges.append({"amount":service_charge["amount"],"type":service_charge["ticketCode"]})
                        fares[passenger_type] = service_charges
                    flights_to_endose = flight_numbers      
            felata = 0
            feiva = 0
            passengers = booking_retrieve["data"]["passengers"]
            for passenger in passenger_keys:
                code = passengers[passenger]["passengerTypeCode"]
                for fare in fares[code]:
                    if fare['type'] == 'YS':
                        feiva = feiva + fare['amount']
                    else:
                        felata = felata + fare['amount']
                passenger_fee = passengers[passenger]["fees"]
                for fee in passenger_fee: 
                    if fee["flightReference"][11:15] in flights_to_endose:
                        for charge in fee["serviceCharges"]:
                            if charge['ticketCode'] == 'YS':
                                feiva = feiva + charge['amount']
                            else: 
                                felata = felata + charge['amount'] 
            deleted = self.__queue_repository.delete_segment(journey_to_endose)
            commit = self.__queue_repository.commit()
            print("Total: FELATA = $"+str(felata)+" FEIVA = $"+str(feiva))
            created_fee = self.__queue_repository.create_fee('FELATA')
            created_fee = self.__queue_repository.create_fee('FEIVA')
            commit = self.__queue_repository.commit()
            passengers = self.__queue_repository.passenger_keys()
            passenger_keys = list(passengers["data"].keys())
            felata_flag = True
            feiva_flag = True
            for passenger in passenger_keys:
                fees = passengers["data"][passenger]["fees"]
                for fee in fees: 
                    if fee['code'] == 'FELATA' and felata_flag: 
                        fee_key = fee['passengerFeeKey']
                        self.__queue_repository.amount(fee_key,felata)
                        commit = self.__queue_repository.commit()
                        felata_flag = False
                    if fee['code'] == 'FEIVA' and feiva_flag: 
                        fee_key = fee['passengerFeeKey']
                        self.__queue_repository.amount(fee_key,feiva)
                        commit = self.__queue_repository.commit()
                        feiva_flag = False
            print(f"Journey to endose {journey_to_endose}")
            deleted = self.__queue_repository.quit_queue(item_key)
            commit = self.__queue_repository.commit()
            print('Success')
        except Exception as e:
            print(e)
            # deleted = self.__queue_repository.quit_queue(item_key)
            # commit = self.__queue_repository.commit()
            return_to_queue = self.__queue_repository.return_to_queue(item_key)
        return