from abc import ABC, abstractmethod
from ecominventory.productinfo import Product


class ProductServices(ABC):  # Abstract Base Classes -->
    '''What services we are going to offer the end users..'''

    @abstractmethod
    def add_product(self, prod: Product) -> str:
        pass

    @abstractmethod
    def delete_product(self, pid: int) -> bool:
        pass

    @abstractmethod
    def get_all_product(self) -> list:
        pass

    @abstractmethod
    def search_by_id(self, pid: int) -> Product:
        pass

    @abstractmethod
    def search_by_vendor(self, ven: str) -> list:
        pass

    @abstractmethod
    def search_by_category(self, cate: str) -> list:
        pass

    @abstractmethod
    def min_product_price(self) -> Product:
        pass

    @abstractmethod
    def max_product_price(self) -> Product:
        pass

    @abstractmethod
    def total_product_price(self) -> float:
        pass

    @abstractmethod
    def avg_product_price(self) -> float:
        pass

    @abstractmethod
    def update_product(self, pid: int, prod: Product) -> Product:
        pass
