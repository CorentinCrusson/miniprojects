'''
Created on 12/07/2013

@author: luke
'''
from abc import *

class Entity(metaclass=ABCMeta):
    
    @abstractproperty
    def id_number(self):
        return 0

class Product(Entity):
    '''
    classdocs
    '''
    id      = 0


    def __init__(self, name=None):
        '''
        Constructor
        '''
        self._id    = Product.id
        Product.id  = Product.id + 1
        if not name:
            self._name = "{0}_{1}".format(self.__class__, self._id)
    
    @property
    def id_number(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    def __repr__(self):
        return "{0}: {1}".format(self.__class__, self._id)
    
class Inventory(Entity):
    
    id      = 0
    
    def __init__(self):
        self._id        = Inventory.id
        Inventory.id    = Inventory.id + 1
        self._products  = []
        
    def product_add(self, *args):
        for arg in args:
            if isinstance(arg, tuple) or isinstance(arg,list):
                for prod in arg:
                    self._products.append(prod)
            elif isinstance(arg,Product):
                self._products.append(arg)
            # if it's not a product it won't get added
    
    @property
    def product_count(self):
        """
        @return: int: amt of product on hand
        """
        return len(self._products)

    @property
    def products(self):
        """
        @return: list(Product): product on hand
        """
        return self._products
        
    @property
    def id_number(self):
        """
        @return:  int: identity number of product
        """
        return self._id
    
    def __repr__(self):
        return "{0}: {1}".format(self.__class__, self._id)
    
class ObjFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def get_object(self):
        return 0
    
    def __repr__(self):
        return "{0}: {1}".format(self.__class__, self._id)
    
class InventoryFactory(ObjFactory):
    
    def get_object(self, amt=1):
        for i in range(amt):
            yield Inventory()

class ProductFactory(ObjFactory):
    
    def get_object(self, amt=1):
        for i in range(amt):
            yield Product()