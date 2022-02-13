from abc import ABC,abstractmethod
from personinfo import PersonInfo

class PersonServices(ABC):

    @abstractmethod
    def add_person_details(self,details):
        pass

    @abstractmethod
    def display_all_persons(self):
        pass

    @abstractmethod
    def get_person_details(self,pid):
        pass

    @abstractmethod
    def update_person_details(self,pid):
        pass

    @abstractmethod
    def delete_person_details(self,pid):
        pass


