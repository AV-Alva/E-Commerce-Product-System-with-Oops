# ecommerce/exceptions.py


class InvalidPriceError(Exception):
    """Raised when a product price is zero or negative."""
    pass


class InvalidQuantityError(Exception):
    """Raised when the requested quantity is invalid."""
    pass


class InsufficientStockError(Exception):
    """Raised when requested quantity is greater than available stock."""
    pass