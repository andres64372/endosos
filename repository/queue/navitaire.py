from conf import settings
from repository.error_response import get_error_from_response
from conf.settings import SessionManager
from domain.authentication import Token


class QueueRepository(Token):
 
    def next_in_queue(self):
        queue_endpoint = f"/api/nsk/v2/queues/bookings/{settings.CASHBACK_QUEUE}/next"
        session = SessionManager().get()
        queue_response = session.get(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                })
        if queue_response.status_code != 200:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element

    def quit_queue(self,item_key:str):
        queue_request = {
            "authorizedBy": "FELATA",
            "notes": "Endosed"
        }
        queue_endpoint = f"/api/nsk/v1/queues/bookings/{settings.CASHBACK_QUEUE}/items/{item_key}"
        session = SessionManager().get()
        queue_response = session.delete(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                },json=queue_request)
        if queue_response.status_code != 200:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element

    def retrieve_by_record_locator(self, record_locator : str):
        queue_endpoint = f"/api/nsk/v1/booking/retrieve/byRecordLocator/{record_locator}"
        session = SessionManager().get()
        queue_response = session.get(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                })

        if queue_response.status_code != 200:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element
    
    def queue_history(self, booking_key : str):
        queue_endpoint = f"/api/nsk/v1/bookings/{booking_key}/queue/history"
        session = SessionManager().get()
        queue_request = {
            "lastPageIndex": 1,
            "fromArchive": False
        }
        queue_response = session.post(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                }, json = queue_request)

        if queue_response.status_code != 200:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element

    def passenger_keys(self):
        queue_endpoint = f"/api/nsk/v1/booking/passengers"
        session = SessionManager().get()
        queue_response = session.get(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                })

        if queue_response.status_code != 200:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element

    def delete_segment(self,segment_key : str):
        queue_endpoint = f"/api/nsk/v1/booking/journeys/{segment_key}"
        queue_element = {
            "waivePenaltyFee": True,
            "waiveSpoilageFee": True,
            "preventReprice": True,
            "forceRefareForItineraryIntegrity": True
        }
        session = SessionManager().get()
        queue_response = session.delete(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                },json=queue_element)

        if queue_response.status_code != 200:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element

    def return_to_queue(self,item_key : str):
        queue_endpoint = f"/api/nsk/v1/queues/bookings/items/{item_key}"
        session = SessionManager().get()
        queue_response = session.post(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                })

        if queue_response.status_code != 200:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element

    def create_fee(self,code : str):
        queue_endpoint = f"/api/nsk/v1/booking/fee"
        queue_request = {
            "feeCode": code
        }
        session = SessionManager().get()
        queue_response = session.post(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                },json=queue_request)
        if queue_response.status_code != 201:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element

    def amount(self,passenger_key : str, total : float):
        queue_endpoint = f"/api/nsk/v1/booking/fee/{passenger_key}"
        queue_request = {
            "amount": total
        }
        session = SessionManager().get()
        queue_response = session.put(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                },json=queue_request)

        if queue_response.status_code != 200:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element


    def commit(self):
        queue_endpoint = f"/api/nsk/v3/booking"
        session = SessionManager().get()
        queue_response = session.put(f"{settings.NAVITAIRE_HOST}{queue_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                }, json={})

        if queue_response.status_code != 200:
            raise get_error_from_response(queue_response)
        else:
            queue_element = queue_response.json()
            return queue_element