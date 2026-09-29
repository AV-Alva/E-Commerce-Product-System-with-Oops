# 🛒 E-Commerce Product System

## 📌 Project Overview

The **E-Commerce Product System** is a Python-based mini application developed to demonstrate **Object-Oriented Programming (OOP)** concepts in a practical e-commerce scenario.

The application allows us to:

- Create different products
- Display product information
- Validate product prices
- Calculate the total price for a purchase
- Update product stock after a purchase
- Prevent purchases when sufficient stock is not available
- Handle invalid inputs using custom exceptions
- Record application activities and errors using logging

The project is organized using **Python packages and modules** to make the code structured, reusable, and maintainable.

---

# 🎯 Objective

The objective of this project is to understand and implement:

- Classes and objects
- Constructors
- Instance variables
- Instance methods
- Static methods
- Packages and modules
- Exception handling
- Custom exceptions
- Logging
- Stock management
- Real-world OOP implementation

---

# 📁 Project Structure

```text
ecommerce_product_system/
│
├── main.py
├── README.md
│
├── ecommerce/
│   ├── __init__.py
│   ├── product.py
│   ├── exceptions.py
│   └── logger_config.py
│
└── logs/
    └── ecommerce.log
```

---

# 📦 Modules

## 1. `main.py`

This is the entry point of the application.

It:

- Creates five different product objects
- Displays available products
- Demonstrates purchases
- Calculates total prices
- Updates stock
- Tests insufficient-stock scenarios
- Handles exceptions without crashing the application

---

## 2. `ecommerce/product.py`

This module contains the main `Product` class.

Every product contains:

```python
product_id
name
price
category
stock_quantity
```

### Methods

#### `display_product()`

Displays all information about a product.

Example:

```text
Product ID: P101
Name: Laptop
Price: ₹65000
Category: Electronics
Stock: 10
```

#### `calculate_total_price(quantity)`

Calculates the total cost of purchasing a given quantity.

Formula:

```text
Total Price = Product Price × Quantity
```

Example:

```text
Laptop Price = ₹65,000
Quantity = 2

Total = ₹65,000 × 2
      = ₹130,000
```

The method also verifies that sufficient stock is available.

#### `update_stock(quantity)`

Updates the available stock after a successful purchase.

Example:

```text
Original Stock = 10
Purchased = 2
Remaining Stock = 8
```

---

# 🔹 Static Method

The project uses the following static method:

```python
@staticmethod
def is_valid_price(price):
```

It validates whether a product price is acceptable.

### Example

```python
Product.is_valid_price(500)
```

Returns:

```text
True
```

While:

```python
Product.is_valid_price(-500)
```

Returns:

```text
False
```

A static method is useful here because price validation does not depend on the data of one specific product object.

---

# ⚠️ Custom Exception Handling

The project defines custom exceptions inside:

```text
ecommerce/exceptions.py
```

### `InvalidPriceError`

Raised when the product price is zero or negative.

Example:

```python
Product("P106", "Monitor", -5000, "Electronics", 10)
```

---

### `InvalidQuantityError`

Raised when an invalid quantity is provided.

For example:

```text
Quantity = 0
Quantity = -5
```

---

### `InsufficientStockError`

Raised when a customer tries to purchase more items than are currently available.

Example:

```text
Available Stock = 8
Requested Quantity = 100
```

The program raises:

```text
InsufficientStockError
```

Instead of terminating the entire application, the exception is caught and an appropriate message is displayed.

---

# 📝 Logging

Logging is configured inside:

```text
ecommerce/logger_config.py
```

Application activities are stored in:

```text
logs/ecommerce.log
```

The program logs events such as:

- Product creation
- Successful purchases
- Stock updates
- Price calculations
- Invalid prices
- Invalid quantities
- Insufficient stock
- Unexpected errors

Example log entries:

```text
2026-09-29 20:15:10 - INFO - Product created: Laptop
2026-09-29 20:15:15 - INFO - Purchase successful: 2 x Laptop
2026-09-29 20:15:15 - INFO - Stock updated for Laptop. Remaining stock: 8
2026-09-29 20:15:20 - ERROR - Insufficient stock for Laptop
```

Logging is useful because it provides a record of what happened inside the application and helps developers troubleshoot problems.

---

# 🛍️ Products Used

The application demonstrates at least five different products:

| Product ID | Product | Category | Price | Initial Stock |
|---|---|---|---:|---:|
| P101 | Laptop | Electronics | ₹65,000 | 10 |
| P102 | Smartphone | Electronics | ₹30,000 | 20 |
| P103 | Headphones | Accessories | ₹2,500 | 30 |
| P104 | Mechanical Keyboard | Accessories | ₹4,500 | 15 |
| P105 | Python Programming Book | Books | ₹800 | 25 |

---

# 🛒 Purchase Flow

The basic application flow is:

```text
Start Program
      ↓
Create Product Objects
      ↓
Validate Product Price
      ↓
Display Products
      ↓
Select Product & Quantity
      ↓
Validate Quantity
      ↓
Check Available Stock
      ↓
Calculate Total Price
      ↓
Update Stock
      ↓
Log Transaction
      ↓
Display Remaining Stock
      ↓
End
```

If sufficient stock is not available:

```text
Purchase Request
      ↓
Check Stock
      ↓
Insufficient Stock
      ↓
Raise InsufficientStockError
      ↓
Catch Exception
      ↓
Display Error Message
      ↓
Write Error to Log
```

---

# ▶️ How to Run the Project

## Step 1 — Open the project

Open the project folder in **VS Code**.

## Step 2 — Open the terminal

Make sure the terminal is pointing to:

```text
ecommerce_product_system/
```

## Step 3 — Run the program

```bash
python main.py
```

---

# 🖥️ Sample Output

```text
===== AVAILABLE PRODUCTS =====

------------------------------
Product ID: P101
Name: Laptop
Price: ₹65000
Category: Electronics
Stock: 10
------------------------------

===== PURCHASE DEMONSTRATION =====

Buying 2 x Laptop

Total Price: ₹130000
Purchase successful!
Remaining Stock: 8

Buying 3 x Smartphone

Total Price: ₹90000
Purchase successful!
Remaining Stock: 17
```

---

# ❌ Insufficient Stock Example

Suppose only 8 laptops are available and the customer requests:

```python
buy_product(laptop, 100)
```

The program checks:

```text
Requested = 100
Available = 8
```

Since:

```text
100 > 8
```

the program displays:

```text
Purchase failed: Only 8 units of Laptop are available.
```

The application continues running instead of crashing.

---

# 🧠 OOP Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Class | `Product` |
| Object | Laptop, Smartphone, Headphones, etc. |
| Constructor | `__init__()` |
| Instance Variables | `name`, `price`, `stock_quantity`, etc. |
| Instance Method | `display_product()` |
| Instance Method | `update_stock()` |
| Instance Method | `calculate_total_price()` |
| Static Method | `is_valid_price()` |
| Package | `ecommerce` |
| Modules | `product.py`, `exceptions.py`, `logger_config.py` |
| Exception Handling | `try`, `except` |
| Custom Exceptions | `InvalidPriceError`, `InvalidQuantityError`, `InsufficientStockError` |
| Logging | `ecommerce.log` |

---

# 🌍 Real-World Application

This project represents a simplified version of the backend logic used by an e-commerce platform.

For example, when a customer buys a product:

```text
Customer
   ↓
Selects Product
   ↓
Chooses Quantity
   ↓
System Checks Stock
   ↓
Calculates Price
   ↓
Purchase Completed
   ↓
Inventory Updated
```

Large e-commerce applications use much more sophisticated versions of the same concepts.

---

# 🚀 Future Enhancements

The project can be extended by adding:

- Shopping cart functionality
- Customer accounts
- Product search
- Product discounts
- GST calculation
- Order IDs
- Payment processing
- Purchase history
- Product ratings
- Database integration
- Web interface using Flask or Django

---

# ✅ Conclusion

The **E-Commerce Product System** demonstrates how Python OOP can be used to model a practical e-commerce application.

The project combines:

**Classes + Objects + Instance Methods + Static Methods + Packages + Modules + Exception Handling + Logging**

By separating different responsibilities into modules, the project is easier to understand, test, debug, maintain, and extend.
