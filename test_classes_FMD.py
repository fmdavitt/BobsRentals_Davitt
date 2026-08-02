#<-------------------------------------------------------------->
#
# .py/assignment designation: test_classes_FMD.py
#
#<-------------------------------------------------------------->

#<-------------------------------------------------------------->
#
# Notes:
# Hello Mrs. Brockman,
# It's Finn again. Here is the testing file for my
# Final Part 1 class library.
# I hope you have a great day and a great week. Ciao!
#
#<-------------------------------------------------------------->

from datetime import datetime, timedelta

from ski_FMD import Ski
from snowboard_FMD import Snowboard
from customer_FMD import Customer
from rental_FMD import Rental
from rental_shop_FMD import RentalShop


def main():

    try:

        # ------------------------------------------------------
        # Create Equipment Objects
        # ------------------------------------------------------

        objSki = Ski()
        objSnowboard = Snowboard()

        print("EQUIPMENT OBJECT TESTS")
        print("----------------------")

        objSki.display_equipment()
        print()

        objSnowboard.display_equipment()
        print()

        # ------------------------------------------------------
        # Test Polymorphism
        # ------------------------------------------------------

        print("POLYMORPHISM TEST")
        print("-----------------")

        arrEquipment = [
            objSki,
            objSnowboard
        ]

        for objEquipment in arrEquipment:

            objEquipment.display_equipment()
            print()

        # ------------------------------------------------------
        # Test Best Price
        # ------------------------------------------------------

        print("BEST-PRICE TEST")
        print("---------------")

        print(
            "Ski price for 4 hours: $",
            format(
                objSki.calculate_best_price(4),
                ".2f"
            ),
            sep=""
        )

        print(
            "Expected best price: $50.00"
        )

        print()

        # ------------------------------------------------------
        # Create Customer Object
        # ------------------------------------------------------

        objCustomer = Customer(
            "Finnegan Davitt",
            1001,
            "WINTERBBP"
        )

        print("CUSTOMER OBJECT TEST")
        print("--------------------")

        objCustomer.display_customer()
        print()

        # ------------------------------------------------------
        # Create Rental Shop
        # ------------------------------------------------------

        objRentalShop = RentalShop(
            30,
            20
        )

        print("STARTING INVENTORY TEST")
        print("-----------------------")

        objRentalShop.display_inventory()
        print()

        # ------------------------------------------------------
        # Create Rental
        # ------------------------------------------------------

        objRental = Rental(
            objCustomer,
            objSki,
            objSnowboard,
            3,
            2,
            "Hourly",
            4
        )

        # Five items qualify for family discount.
        # Coupon ending in BBP qualifies for coupon discount.

        print("RENTAL OBJECT TEST")
        print("------------------")

        objRental.display_rental()
        print()

        # ------------------------------------------------------
        # Test Estimated Cost
        # ------------------------------------------------------

        print("ESTIMATED COST TEST")
        print("-------------------")

        dblEstimatedCost = (
            objRental.calculate_estimated_cost()
        )

        print(
            "Estimated Discounted Cost: $",
            format(
                dblEstimatedCost,
                ".2f"
            ),
            sep=""
        )

        print()

        # ------------------------------------------------------
        # Test Inventory Reduction
        # ------------------------------------------------------

        objRentalShop.rent_equipment(
            objRental.intNumberOfSkis,
            objRental.intNumberOfSnowboards
        )

        print("INVENTORY AFTER RENTAL")
        print("----------------------")

        objRentalShop.display_inventory()
        print()

        # ------------------------------------------------------
        # Test Final Bill
        # ------------------------------------------------------

        objRental.dtmRentalTime = (
            datetime.now() -
            timedelta(hours=4)
        )

        objCustomer.dtmRentalTime = (
            objRental.dtmRentalTime
        )

        dtmReturnTime = datetime.now()

        print("FINAL BILL TEST")
        print("---------------")

        dblFinalBill = (
            objRentalShop.process_return(
                objRental,
                dtmReturnTime
            )
        )

        print(
            "Final Discounted Bill: $",
            format(
                dblFinalBill,
                ".2f"
            ),
            sep=""
        )

        print()

        # ------------------------------------------------------
        # Test Inventory Restoration
        # ------------------------------------------------------

        print("INVENTORY AFTER RETURN")
        print("----------------------")

        objRentalShop.display_inventory()
        print()

        # ------------------------------------------------------
        # Test Customer Return Information
        # ------------------------------------------------------

        print("CUSTOMER RETURN INFORMATION TEST")
        print("--------------------------------")

        objReturnInformation = (
            objCustomer.return_equipment()
        )

        print(
            "Return Information:",
            objReturnInformation
        )

        print()

        # ------------------------------------------------------
        # Test Daily Totals
        # ------------------------------------------------------

        print("DAILY TOTALS TEST")
        print("-----------------")

        objRentalShop.display_daily_totals()
        print()

        # ------------------------------------------------------
        # Test Inventory Validation
        # ------------------------------------------------------

        print("INVENTORY VALIDATION TEST")
        print("-------------------------")

        try:

            objRentalShop.rent_skis(31)

        except Exception as ex:

            print(
                "Expected Validation Error:",
                ex
            )

    except Exception as ex:

        print(
            "Unexpected Error:",
            ex
        )

    print()

    input(
        "Press Enter to close the testing program..."
    )


if __name__ == "__main__":

    main()
