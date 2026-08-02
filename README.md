# Bob's Ski & Snowboard Rentals

## Author

Finnegan Davitt

## Course

Object-Oriented Programming

## Project

Final Project – Part 1: Bob's Ski & Snowboard Rentals

## Project Description

This repository contains a reusable Python class library for Bob's Ski
& Snowboard Rentals.

My project supports customers, skis, snowboards, rental rates,
inventory, rental estimates, final billing, discounts, equipment
returns, and daily totals.

This repository contains the reusable classes needed by an application
programmer. It does not contain a menu system, continuous application
loop, complete rental workflow, or complete return workflow.

## Project Files

### `rental_equipment_FMD.py`

Contains the `RentalEquipment` parent class.

This class stores the information shared by all rental equipment,
including:

- Equipment name
- Hourly rate
- Daily rate
- Weekly rate

Important methods include:

- `calculate_hourly_price()`
- `calculate_daily_price()`
- `calculate_weekly_price()`
- `calculate_best_price()`
- `display_equipment()`

### `ski_FMD.py`

Contains the `Ski` child class.

The class inherits from `RentalEquipment` and sets the required ski
rates:

- $15 per hour
- $50 per day
- $200 per week

### `snowboard_FMD.py`

Contains the `Snowboard` child class.

The class inherits from `RentalEquipment` and sets the required
snowboard rates:

- $10 per hour
- $40 per day
- $160 per week

### `customer_FMD.py`

Contains the `Customer` class.

The class stores:

- Customer name
- Customer ID
- Coupon code
- Rental basis
- Rental time
- Number of rental items

Important methods include:

- `qualifies_for_coupon()`
- `qualifies_for_family_discount()`
- `return_equipment()`
- `display_customer()`

### `rental_FMD.py`

Contains the `Rental` class.

The class connects a customer with rented skis and snowboards. It
supports:

- Hourly, daily, and weekly rental periods
- Mixed ski and snowboard rentals
- Rental estimates
- Best available pricing
- Final billing
- Family discounts
- Coupon discounts
- Rental return information

Important methods include:

- `get_total_number_of_items()`
- `calculate_estimated_cost()`
- `calculate_best_price()`
- `apply_family_discount()`
- `apply_coupon_discount()`
- `apply_discounts()`
- `calculate_final_bill()`
- `get_return_information()`
- `display_rental()`

### `rental_shop_FMD.py`

Contains the `RentalShop` class.

The class stores and manages:

- Starting ski inventory
- Starting snowboard inventory
- Available ski inventory
- Available snowboard inventory
- Total skis rented during the day
- Total snowboards rented during the day
- Total daily rental revenue

Important methods include:

- `display_inventory()`
- `rent_skis()`
- `rent_snowboards()`
- `rent_equipment()`
- `return_skis()`
- `return_snowboards()`
- `return_equipment()`
- `process_return()`
- `get_daily_skis_rented()`
- `get_daily_snowboards_rented()`
- `get_daily_revenue()`
- `display_daily_totals()`

### `test_classes_FMD.py`

Contains a focused `main()` testing function.

The testing file demonstrates:

- Object creation
- Property values
- Equipment rates
- Best-price calculations
- Family discounts
- Coupon discounts
- Inventory reduction
- Inventory restoration
- Final billing
- Daily totals
- Inheritance
- Polymorphism
- Validation exceptions

The testing file is not a complete rental application.

## Business Rules

### Ski Rates

- Hourly: $15
- Daily: $50
- Weekly: $200

### Snowboard Rates

- Hourly: $10
- Daily: $40
- Weekly: $160

### Family Discount

A rental containing three to five total items receives a 25% discount.

### Coupon Discount

A coupon code ending in `BBP` receives a 10% discount.

When both discounts apply, the family discount is applied first,
followed by the coupon discount.

### Best Available Price

The pricing methods compare the available hourly, daily, and weekly
prices and return the lowest qualifying cost.

For example, four hours of ski rental would normally cost $60 using the
hourly rate. Because the daily rate is $50, the customer is charged
$50.

## Object-Oriented Programming Concepts

### Encapsulation

Class attributes are protected through properties and setter methods.

The setter methods validate values before storing them. Examples
include customer IDs, rental quantities, inventory values, rental
rates, and rental durations.

### Inheritance

The `Ski` and `Snowboard` classes inherit from the
`RentalEquipment` parent class.

This allows both child classes to reuse the pricing and display methods
without duplicating the same code.

### Polymorphism

`Ski` and `Snowboard` objects can be processed through the same shared
method calls.

For example:

```python
equipment.display_equipment()
