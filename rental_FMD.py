#<-------------------------------------------------------------->
#
# .py/assignment designation: rental_FMD.py
#
#<-------------------------------------------------------------->

#<-------------------------------------------------------------->
#
# Notes:
# Hello Mrs. Brockman,
# It's Finn again. Here is the rental_FMD.py partition
# of my Final Part 1 submission.
# I hope you have a great day and a great week, ciao!
#
#<-------------------------------------------------------------->

from datetime import datetime
from math import ceil


class Rental:

    def __init__(
        self,
        objCustomer,
        objSki,
        objSnowboard,
        intNumberOfSkis,
        intNumberOfSnowboards,
        strRentalBasis,
        intRentalDuration
    ):

        self.objCustomer = objCustomer
        self.objSki = objSki
        self.objSnowboard = objSnowboard
        self.intNumberOfSkis = intNumberOfSkis
        self.intNumberOfSnowboards = intNumberOfSnowboards
        self.strRentalBasis = strRentalBasis
        self.intRentalDuration = intRentalDuration
        self.dtmRentalTime = datetime.now()

        self.objCustomer.strRentalBasis = strRentalBasis
        self.objCustomer.dtmRentalTime = self.dtmRentalTime
        self.objCustomer.intNumberOfItems = (
            intNumberOfSkis +
            intNumberOfSnowboards
        )

    # ----------------------------------------------------------
    # Customer Property
    # ----------------------------------------------------------

    @property
    def objCustomer(self):
        return self.__objCustomer

    @objCustomer.setter
    def objCustomer(self, objCustomer):

        if objCustomer is None:
            raise Exception(
                "A customer object is required."
            )

        self.__objCustomer = objCustomer

    # ----------------------------------------------------------
    # Ski Object Property
    # ----------------------------------------------------------

    @property
    def objSki(self):
        return self.__objSki

    @objSki.setter
    def objSki(self, objSki):

        if objSki is None:
            raise Exception(
                "A ski object is required."
            )

        self.__objSki = objSki

    # ----------------------------------------------------------
    # Snowboard Object Property
    # ----------------------------------------------------------

    @property
    def objSnowboard(self):
        return self.__objSnowboard

    @objSnowboard.setter
    def objSnowboard(self, objSnowboard):

        if objSnowboard is None:
            raise Exception(
                "A snowboard object is required."
            )

        self.__objSnowboard = objSnowboard

    # ----------------------------------------------------------
    # Number of Skis Property
    # ----------------------------------------------------------

    @property
    def intNumberOfSkis(self):
        return self.__intNumberOfSkis

    @intNumberOfSkis.setter
    def intNumberOfSkis(self, intNumberOfSkis):

        if intNumberOfSkis < 0:
            raise Exception(
                "Number of skis cannot be negative."
            )

        self.__intNumberOfSkis = intNumberOfSkis

    # ----------------------------------------------------------
    # Number of Snowboards Property
    # ----------------------------------------------------------

    @property
    def intNumberOfSnowboards(self):
        return self.__intNumberOfSnowboards

    @intNumberOfSnowboards.setter
    def intNumberOfSnowboards(
        self,
        intNumberOfSnowboards
    ):

        if intNumberOfSnowboards < 0:
            raise Exception(
                "Number of snowboards cannot be negative."
            )

        self.__intNumberOfSnowboards = (
            intNumberOfSnowboards
        )

    # ----------------------------------------------------------
    # Rental Basis Property
    # ----------------------------------------------------------

    @property
    def strRentalBasis(self):
        return self.__strRentalBasis

    @strRentalBasis.setter
    def strRentalBasis(self, strRentalBasis):

        if (
            strRentalBasis != "Hourly" and
            strRentalBasis != "Daily" and
            strRentalBasis != "Weekly"
        ):
            raise Exception(
                "Rental basis must be Hourly, Daily, or Weekly."
            )

        self.__strRentalBasis = strRentalBasis

    # ----------------------------------------------------------
    # Rental Duration Property
    # ----------------------------------------------------------

    @property
    def intRentalDuration(self):
        return self.__intRentalDuration

    @intRentalDuration.setter
    def intRentalDuration(self, intRentalDuration):

        if intRentalDuration <= 0:
            raise Exception(
                "Rental duration must be greater than zero."
            )

        self.__intRentalDuration = intRentalDuration

    # ----------------------------------------------------------
    # Rental Time Property
    # ----------------------------------------------------------

    @property
    def dtmRentalTime(self):
        return self.__dtmRentalTime

    @dtmRentalTime.setter
    def dtmRentalTime(self, dtmRentalTime):

        if dtmRentalTime is None:
            raise Exception(
                "Rental time cannot be blank."
            )

        self.__dtmRentalTime = dtmRentalTime

    # ----------------------------------------------------------
    # Total Number of Items Method
    # ----------------------------------------------------------

    def get_total_number_of_items(self):

        return (
            self.intNumberOfSkis +
            self.intNumberOfSnowboards
        )

    # ----------------------------------------------------------
    # Estimated Cost Method
    # ----------------------------------------------------------

    def calculate_estimated_cost(self):

        if self.get_total_number_of_items() <= 0:
            raise Exception(
                "At least one rental item is required."
            )

        if self.strRentalBasis == "Hourly":

            dblSkiCost = (
                self.objSki.calculate_hourly_price(
                    self.intRentalDuration
                ) *
                self.intNumberOfSkis
            )

            dblSnowboardCost = (
                self.objSnowboard.calculate_hourly_price(
                    self.intRentalDuration
                ) *
                self.intNumberOfSnowboards
            )

        elif self.strRentalBasis == "Daily":

            dblSkiCost = (
                self.objSki.calculate_daily_price(
                    self.intRentalDuration
                ) *
                self.intNumberOfSkis
            )

            dblSnowboardCost = (
                self.objSnowboard.calculate_daily_price(
                    self.intRentalDuration
                ) *
                self.intNumberOfSnowboards
            )

        else:

            dblSkiCost = (
                self.objSki.calculate_weekly_price(
                    self.intRentalDuration
                ) *
                self.intNumberOfSkis
            )

            dblSnowboardCost = (
                self.objSnowboard.calculate_weekly_price(
                    self.intRentalDuration
                ) *
                self.intNumberOfSnowboards
            )

        dblEstimatedCost = (
            dblSkiCost +
            dblSnowboardCost
        )

        return self.apply_discounts(
            dblEstimatedCost
        )

    # ----------------------------------------------------------
    # Best Available Price Method
    # ----------------------------------------------------------

    def calculate_best_price(self, dblHoursRented):

        if dblHoursRented <= 0:
            raise Exception(
                "Hours rented must be greater than zero."
            )

        intHours = ceil(dblHoursRented)

        intDays = ceil(
            dblHoursRented / 24
        )

        intWeeks = ceil(
            dblHoursRented / 168
        )

        dblHourlySkiCost = (
            self.objSki.calculate_hourly_price(
                intHours
            ) *
            self.intNumberOfSkis
        )

        dblHourlySnowboardCost = (
            self.objSnowboard.calculate_hourly_price(
                intHours
            ) *
            self.intNumberOfSnowboards
        )

        dblHourlyTotal = (
            dblHourlySkiCost +
            dblHourlySnowboardCost
        )

        dblDailySkiCost = (
            self.objSki.calculate_daily_price(
                intDays
            ) *
            self.intNumberOfSkis
        )

        dblDailySnowboardCost = (
            self.objSnowboard.calculate_daily_price(
                intDays
            ) *
            self.intNumberOfSnowboards
        )

        dblDailyTotal = (
            dblDailySkiCost +
            dblDailySnowboardCost
        )

        dblWeeklySkiCost = (
            self.objSki.calculate_weekly_price(
                intWeeks
            ) *
            self.intNumberOfSkis
        )

        dblWeeklySnowboardCost = (
            self.objSnowboard.calculate_weekly_price(
                intWeeks
            ) *
            self.intNumberOfSnowboards
        )

        dblWeeklyTotal = (
            dblWeeklySkiCost +
            dblWeeklySnowboardCost
        )

        return min(
            dblHourlyTotal,
            dblDailyTotal,
            dblWeeklyTotal
        )

    # ----------------------------------------------------------
    # Family Discount Method
    # ----------------------------------------------------------

    def apply_family_discount(self, dblRentalCost):

        if self.objCustomer.qualifies_for_family_discount():

            dblRentalCost = (
                dblRentalCost *
                0.75
            )

        return dblRentalCost

    # ----------------------------------------------------------
    # Coupon Discount Method
    # ----------------------------------------------------------

    def apply_coupon_discount(self, dblRentalCost):

        if self.objCustomer.qualifies_for_coupon():

            dblRentalCost = (
                dblRentalCost *
                0.90
            )

        return dblRentalCost

    # ----------------------------------------------------------
    # Apply All Discounts Method
    # ----------------------------------------------------------

    def apply_discounts(self, dblRentalCost):

        if dblRentalCost < 0:
            raise Exception(
                "Rental cost cannot be negative."
            )

        dblDiscountedCost = (
            self.apply_family_discount(
                dblRentalCost
            )
        )

        dblDiscountedCost = (
            self.apply_coupon_discount(
                dblDiscountedCost
            )
        )

        return dblDiscountedCost

    # ----------------------------------------------------------
    # Final Bill Method
    # ----------------------------------------------------------

    def calculate_final_bill(
        self,
        dtmReturnTime=None
    ):

        if dtmReturnTime is None:
            dtmReturnTime = datetime.now()

        if dtmReturnTime < self.dtmRentalTime:
            raise Exception(
                "Return time cannot be before rental time."
            )

        objRentalLength = (
            dtmReturnTime -
            self.dtmRentalTime
        )

        dblHoursRented = (
            objRentalLength.total_seconds() /
            3600
        )

        if dblHoursRented <= 0:
            dblHoursRented = 1

        dblBestPrice = (
            self.calculate_best_price(
                dblHoursRented
            )
        )

        dblFinalBill = (
            self.apply_discounts(
                dblBestPrice
            )
        )

        return dblFinalBill

    # ----------------------------------------------------------
    # Return Information Method
    # ----------------------------------------------------------

    def get_return_information(self):

        return (
            self.dtmRentalTime,
            self.strRentalBasis,
            self.intNumberOfSkis,
            self.intNumberOfSnowboards
        )

    # ----------------------------------------------------------
    # Display Rental Method
    # ----------------------------------------------------------

    def display_rental(self):

        print(
            "Customer:",
            self.objCustomer.strCustomerName
        )

        print(
            "Rental Basis:",
            self.strRentalBasis
        )

        print(
            "Number of Skis:",
            self.intNumberOfSkis
        )

        print(
            "Number of Snowboards:",
            self.intNumberOfSnowboards
        )

        print(
            "Total Number of Items:",
            self.get_total_number_of_items()
        )

        print(
            "Rental Start Time:",
            self.dtmRentalTime
        )
