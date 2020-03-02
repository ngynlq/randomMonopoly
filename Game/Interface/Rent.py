from abc import ABC
from abc import abstractmethod


class Rent(ABC):
    """A helper class that enables extension of various rent payment 
    rules based on the requirement that rents can grow continously
    
    Arguments:
        ABC {[type]} -- [description]
    """

    def __init__(self, rents,payment):
        """constructor the class
        
        Arguments:
            rents {list} -- A list of rents from decreasing to increasing values;
             represents a hash table
            payment {[type]} -- the hashing function accepts
            houses, hotels, and the rent array for fixed values
        """
        self.__rents = rents
        self.__calculateRent = payment

    @abstractmethod
    """Method that returns a list of how payments are structured assuming
    that the rent only increases as the index increases
    """
    def getRents(self):
        pass

    def findRent(self, houses, hotel):
        """A member that calculates the rent for a property
        
        Arguments:
            houses {Number} -- number of houses on a property
            hotel {Number} -- number of houses on a poprerty
        """
        return self.__calculateRent(houses,hotels,self.__rents)
        
