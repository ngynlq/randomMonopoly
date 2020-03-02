class Deed:
    def __init__(self, id, group, value, housePrice=0, hotelPrice=0, rent=0):
        self.__id = id
        self.__mortgage = False
        self.__group = group
        self.__value = value
        self.__houses = 0
        self.__hotels = 0
        self.__morgagePrice = 0
        self.__housePrice = housePrice
        self.__hotelPrice = hotelPrice
        self.__rent = rent

    def getID(self):
        return self.__id

    def getHouses(self):
        return self.__houses

    def addHouse(self):
        self.__houses += 1

    def setHouses(self, val):
        self.__houses = val

    def addHotel(self):
        self.__hotels += 1

    def isMortgaged(self):
        return self.__mortgage

    def getMortgageValue(self):
        return self.__mortgagePrice

    def getHotel(self):
        return self.__hotels

    def setHotel(self, val):
        self.__hotels = val

    def clearDeed(self):
        self.__hotels = 0
        self.__houses = 0

    def getFullValue(self):
        return (
            self.__value
            + self.__houses * self.__housePrice
            + self.__hotels * self.__hotelPrice
        )

    def getUpgradeCost(self, house=0, hotel=0):
        return house * self.__housePrice + hotel * self.__hotelPrice

    def calculateRent(self, group):
        return 5
