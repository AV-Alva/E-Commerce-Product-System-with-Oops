# main.py

from ecommerce.product import Product

from ecommerce.exceptions import (
    InvalidPriceError,
    InvalidQuantityError,
    InsufficientStockError
)

from ecommerce.logger_config import logger


def buy_product(product, quantity):

    try:
        print(f"\nBuying {quantity} x {product.name}")

        total_price = product.calculate_total_price(quantity)

        print("Total Price: ₹", total_price)

        product.update_stock(quantity)

        print("Purchase successful!")
        print("Remaining Stock:", product.stock_quantity)

        logger.info(
            f"Purchase successful: "
            f"{quantity} x {product.name}"
        )

    except InvalidQuantityError as error:
        print("Invalid quantity:", error)
        logger.error(error)

    except InsufficientStockError as error:
        print("Purchase failed:", error)
        logger.error(error)

    except Exception as error:
        print("Unexpected error:", error)
        logger.exception(error)


def main():

    try:

        # Create 5 Product objects

        laptop = Product(
            "P101",
            "Laptop",
            65000,
            "Electronics",
            10
        )

        smartphone = Product(
            "P102",
            "Smartphone",
            30000,
            "Electronics",
            20
        )

        headphones = Product(
            "P103",
            "Headphones",
            2500,
            "Accessories",
            30
        )

        keyboard = Product(
            "P104",
            "Mechanical Keyboard",
            4500,
            "Accessories",
            15
        )

        book = Product(
            "P105",
            "Python Programming Book",
            800,
            "Books",
            25
        )

        products = [
            laptop,
            smartphone,
            headphones,
            keyboard,
            book
        ]

        print("\n===== AVAILABLE PRODUCTS =====")

        for product in products:
            product.display_product()

        print("\n===== PURCHASE DEMONSTRATION =====")

        buy_product(laptop, 2)

        buy_product(smartphone, 3)

        buy_product(headphones, 5)

        buy_product(keyboard, 2)

        buy_product(book, 4)

        print("\n===== UPDATED PRODUCT STOCK =====")

        for product in products:
            product.display_product()

        # Demonstrating insufficient stock

        print("\n===== INVALID PURCHASE TEST =====")

        buy_product(laptop, 100)

    except InvalidPriceError as error:
        print("Invalid product price:", error)
        logger.error(error)

    except InvalidQuantityError as error:
        print("Invalid quantity:", error)
        logger.error(error)

    except Exception as error:
        print("Unexpected application error:", error)
        logger.exception(error)


if __name__ == "__main__":
    main()