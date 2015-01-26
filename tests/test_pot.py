from pot import Pot


def test_setting_up_pot():
    """Testing that setting up the purse works"""

    new_pot = Pot(400)
    assert new_pot.purse == 400
    new_pot = Pot(-20000)
    assert new_pot.purse == -20000


def test_betting():
    """Testing bet fn stores a bet"""

    new_pot = Pot(100)
    new_pot.make_bet(100)
    assert new_pot.bet == 100
    new_pot.make_bet(1)
    assert new_pot.bet == 1


def test_add_bet():
    """Testing that returning bet adds bet to purse"""

    new_pot = Pot(100)
    new_pot.make_bet(100)
    new_pot.return_bet()
    assert new_pot.purse == 200


def test_subtract_bet():

    """Testing that subtracing bet removes it from purse"""
    new_pot = Pot(100)
    new_pot.make_bet(100)
    new_pot.subtract_bet()
    assert new_pot.purse == 0
