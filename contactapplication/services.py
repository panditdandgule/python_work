from abc import ABC, abstractmethod


class ContactServices(ABC):

    @abstractmethod
    def add_contact(self):
        pass

    @abstractmethod
    def display_contacts(self):
        pass

    @abstractmethod
    def search_contact(self):
        pass

    @abstractmethod
    def update_contact(self):
        pass

    @abstractmethod
    def delete_contact(self):
        pass
