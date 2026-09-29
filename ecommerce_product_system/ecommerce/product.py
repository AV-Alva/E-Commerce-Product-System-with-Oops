# ecommerce/product.py

from .exceptions import (
    InvalidPriceError,
    InvalidQuantityError,
    InsufficientStockError
)

from .logger_config import logger


class Product:

    def __init__(self, product_id, name, price, category, stock_quantity):

        if not Product.is_valid_price(price):
            logger.error(f"Invalid price for {name}: {price}")
            raise InvalidPriceError(
                "Product price must be greater than zero."
            )

        if stock_quantity < 0:
            logger.error(
                f"Invalid stock quantity for {name}: {stock_quantity}"
            )
            raise InvalidQuantityError(
                "Stock quantity cannot be negative."
            )

        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

        logger.info(
            f"Product created: {self.name}, "
            f"Price: {self.price}, "
            f"Stock: {self.stock_quantity}"
        )

    @staticmethod
    def is_valid_price(price):
        """Return True if price is greater than zero."""

        try:
            return float(price) > 0

        except (ValueError, TypeError):
            return False

    def display_product(self):
        """Display product information."""

        print("\n------------------------------")
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price: ₹", self.price)
        print("Category:", self.category)
        print("Stock:", self.stock_quantity)
        print("------------------------------")

    def calculate_total_price(self, quantity):
        """Calculate price for requested quantity."""

        if quantity <= 0:
            raise InvalidQuantityError(
                "Quantity must be greater than zero."
            )

        if quantity > self.stock_quantity:
            raise InsufficientStockError(
                f"Only {self.stock_quantity} units of "
                f"{self.name} are available."
            )

        total_price = self.price * quantity

        logger.info(
            f"Total calculated for {self.name}: "
            f"{quantity} x {self.price} = {total_price}"
        )

        return total_price

    def update_stock(self, quantity):
        """Reduce stock after a purchase."""

        if quantity <= 0:
            raise InvalidQuantityError(
                "Purchase quantity must be greater than zero."
            )

        if quantity > self.stock_quantity:
            raise InsufficientStockError(
                f"Cannot buy {quantity} units. "
                f"Only {self.stock_quantity} units are available."
            )

        self.stock_quantity -= quantity

        logger.info(
            f"Stock updated for {self.name}. "
            f"Remaining stock: {self.stock_quantity}"
        )