from Game.Deed import Deed
from Game.Player import Player


def test_addHouse():
    deed = Deed(id="aaa", group="red", value=5)
    deed.addHouse()
    assert deed.getHouses() == 1


def test_addHotel():
    deed = Deed(id="aaa", group="red", value=5)
    deed.addHotel()
    assert deed.getHotel() == 1


def test_clear_deed():
    deed = Deed(id="aaa", group="red", value=5)
    deed.setHouses(5)
    deed.setHotel(5)
    deed.clearDeed()
    assert deed.getHouses() == 0
    assert deed.getHotel() == 0


def test_active_value():
    pass


def test_full_value_houses():
    deed = Deed(id="aaa", group="red", value=5, housePrice=10, hotelPrice=5)
    deed.setHouses(4)
    assert deed.getFullValue() == 45


def test_full_value_hotel():
    val = 5
    house = 10
    hotel = 5
    deed = Deed(id="aaa", group="red", value=val, housePrice=house, hotelPrice=hotel)
    deed.setHotel(1)
    assert deed.getFullValue() == val + hotel


def test_getUpgradeCost():
    val = 5
    house = 10
    hotel = 5
    deed = Deed(id="aaa", group="red", value=val, housePrice=house, hotelPrice=hotel)
    cost = deed.getUpgradeCost(house=3)
    assert cost == house * 3


def test_upgradeHouse_Hotel():
    val = 5
    house = 10
    hotel = 5
    deed = Deed(id="aaa", group="red", value=val, housePrice=house, hotelPrice=hotel)
    cost = deed.getUpgradeCost(house=3, hotel=1)
    assert cost == hotel * 1 + house * 3


def test_rent_basic():
    val = 5
    house = 10
    hotel = 5
    deed = Deed(
        id="aaa", group="red", value=val, housePrice=house, hotelPrice=hotel, rent=5
    )
    assert deed.calculateRent(False) == 5


def test_rent_houses():
    val = 5
    house = 10
    hotel = 5
    deed = Deed(
        id="aaa", group="red", value=val, housePrice=house, hotelPrice=hotel, rent=5
    )
    deed.setHouses(2)
    assert deed.calculateRent(False) == 5
