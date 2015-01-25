import blackjack.functions as fun


def test_hit_stand():
    x = 'HIT'
    y = 'STAND'
    z = 'POTATO'
    assert fun.hit_stand(x) is True
    assert fun.hit_stand(y) is True
    assert fun.hit_stand(z) is False
