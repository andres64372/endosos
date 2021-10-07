from repository.login.navitaire import LoginRepository
from repository.queue.navitaire import QueueRepository

from use_cases.authenticate import Authenticate
from use_cases.queue_element import QueuElement


login_repo = LoginRepository()
authenticate_uc = Authenticate(login_repo)
token = authenticate_uc.execute()
next_element= QueuElement(QueueRepository(token))
response = next_element.execute()
