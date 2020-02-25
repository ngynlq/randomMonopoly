from Game.TurnOrder import TurnOrder

def test_turnOrder():
    order = TurnOrder([1,2,3])
    orderTurn = iter(order)
    assert next(orderTurn) == 1

def test_turnLoop():
    order = TurnOrder([1,2])
    orderTurn = iter(order)
    next(orderTurn)
    next(orderTurn)
    assert next(orderTurn) == 1

def test_reverseOrder():
    order = TurnOrder([1,2,3,4])
    orderTurn = iter(order)
    orderTurn.reverseOrder()
    assert next(orderTurn) == 4
