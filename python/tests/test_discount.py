import pytest

from exercises.strategy_pattern.discount import (
    FlatDiscount,
    NoDiscount,
    PercentageDiscount,
    ShoppingCart,
)


def test_no_discount_returns_full_total():
    cart = ShoppingCart(NoDiscount())
    cart.add_item(10)
    cart.add_item(20)
    assert cart.total() == 30


def test_percentage_discount_reduces_total():
    cart = ShoppingCart(PercentageDiscount(0.1))
    cart.add_item(100)
    assert cart.total() == 90


def test_flat_discount_never_goes_below_zero():
    cart = ShoppingCart(FlatDiscount(50))
    cart.add_item(10)
    assert cart.total() == 0


def test_set_strategy_changes_behavior_at_runtime():
    cart = ShoppingCart()
    cart.add_item(100)
    assert cart.total() == 100  # default NoDiscount

    cart.set_strategy(PercentageDiscount(0.5))
    assert cart.total() == 50


@pytest.mark.parametrize("invalid_percentage", [-0.1, 1.1])
def test_percentage_discount_rejects_invalid_values(invalid_percentage):
    with pytest.raises(ValueError):
        PercentageDiscount(invalid_percentage)


def test_flat_discount_rejects_negative_amount():
    with pytest.raises(ValueError):
        FlatDiscount(-1)


def test_add_item_rejects_negative_price():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item(-5)
