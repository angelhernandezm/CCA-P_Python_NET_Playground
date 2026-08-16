"""Strategy design pattern exercise.

Demonstrates how to decouple an algorithm (discount calculation) from the
context that uses it (the shopping cart), so new discount strategies can be
added without modifying existing code (Open/Closed Principle).
"""

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Base interface for all discount strategies."""

    @abstractmethod
    def apply(self, total: float) -> float:
        """Return the total price after applying the discount."""
        raise NotImplementedError


class NoDiscount(DiscountStrategy):
    """No discount is applied."""

    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    """Applies a percentage-based discount (e.g. 0.1 for 10%)."""

    def __init__(self, percentage: float):
        if not 0 <= percentage <= 1:
            raise ValueError("percentage must be between 0 and 1")
        self.percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage)


class FlatDiscount(DiscountStrategy):
    """Applies a flat amount discount, never going below zero."""

    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.amount = amount

    def apply(self, total: float) -> float:
        return max(0.0, total - self.amount)


class ShoppingCart:
    """Context that delegates discount calculation to a strategy."""

    def __init__(self, strategy: DiscountStrategy = None):
        self.items: list[float] = []
        self.strategy = strategy or NoDiscount()

    def add_item(self, price: float) -> None:
        if price < 0:
            raise ValueError("price must be non-negative")
        self.items.append(price)

    def set_strategy(self, strategy: DiscountStrategy) -> None:
        self.strategy = strategy

    def total(self) -> float:
        subtotal = sum(self.items)
        return self.strategy.apply(subtotal)
