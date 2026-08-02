#<-------------------------------------------------------------->
#
# .py/assignment designation: rental_equipment_FMD.py
#
#<-------------------------------------------------------------->

#<-------------------------------------------------------------->
#
# Notes:
# Hello Mrs. Brockman,
# It's Finn again. Here is the rental_equipment_FMD.py partition 
# of my Final Part 1 submission.
# I hope you have a great day and a great week, ciao!
#
#<-------------------------------------------------------------->

#<-------------------------------------------------------------->
#
# RentalEquipment Parent Class
# Bob's Ski & Snowboard Rentals
#
# This parent class stores information common to all rental
# equipment and provides pricing methods that can be inherited
# by subclasses.
#
#<-------------------------------------------------------------->


class RentalEquipment:

    def __init__(
        self,
        strEquipmentName,
        dblHourlyRate,
        dblDailyRate,
        dblWeeklyRate
    ):

        self.strEquipmentName = strEquipmentName
        self.dblHourlyRate = dblHourlyRate
        self.dblDailyRate = dblDailyRate
        self.dblWeeklyRate = dblWeeklyRate

    # ----------------------------------------------------------
    # Equipment Name Property
    # ----------------------------------------------------------

    @property
    def strEquipmentName(self):
        return self.__strEquipmentName

    @strEquipmentName.setter
    def strEquipmentName(self, strEquipmentName):

        if strEquipmentName == "":
            raise Exception(
                "Equipment name cannot be blank."
            )

        self.__strEquipmentName = strEquipmentName

    # ----------------------------------------------------------
    # Hourly Rate Property
    # ----------------------------------------------------------

    @property
    def dblHourlyRate(self):
        return self.__dblHourlyRate

    @dblHourlyRate.setter
    def dblHourlyRate(self, dblHourlyRate):

        if dblHourlyRate <= 0:
            raise Exception(
                "Hourly rate must be greater than zero."
            )

        self.__dblHourlyRate = dblHourlyRate

    # ----------------------------------------------------------
    # Daily Rate Property
    # ----------------------------------------------------------

    @property
    def dblDailyRate(self):
        return self.__dblDailyRate

    @dblDailyRate.setter
    def dblDailyRate(self, dblDailyRate):

        if dblDailyRate <= 0:
            raise Exception(
                "Daily rate must be greater than zero."
            )

        self.__dblDailyRate = dblDailyRate

    # ----------------------------------------------------------
    # Weekly Rate Property
    # ----------------------------------------------------------

    @property
    def dblWeeklyRate(self):
        return self.__dblWeeklyRate

    @dblWeeklyRate.setter
    def dblWeeklyRate(self, dblWeeklyRate):

        if dblWeeklyRate <= 0:
            raise Exception(
                "Weekly rate must be greater than zero."
            )

        self.__dblWeeklyRate = dblWeeklyRate

    # ----------------------------------------------------------
    # Pricing Methods
    # ----------------------------------------------------------

    def calculate_hourly_price(
        self,
        intHours
    ):

        if intHours <= 0:
            raise Exception(
                "Hours must be greater than zero."
            )

        return (
            intHours *
            self.dblHourlyRate
        )

    def calculate_daily_price(
        self,
        intDays
    ):

        if intDays <= 0:
            raise Exception(
                "Days must be greater than zero."
            )

        return (
            intDays *
            self.dblDailyRate
        )

    def calculate_weekly_price(
        self,
        intWeeks
    ):

        if intWeeks <= 0:
            raise Exception(
                "Weeks must be greater than zero."
            )

        return (
            intWeeks *
            self.dblWeeklyRate
        )

    # ----------------------------------------------------------
    # Best Price Method
    # ----------------------------------------------------------

    def calculate_best_price(
        self,
        intHours
    ):

        if intHours <= 0:
            raise Exception(
                "Rental time must be greater than zero."
            )

        dblHourlyCost = (
            self.calculate_hourly_price(
                intHours
            )
        )

        intDays = (
            intHours + 23
        ) // 24

        dblDailyCost = (
            self.calculate_daily_price(
                intDays
            )
        )

        intWeeks = (
            intDays + 6
        ) // 7

        dblWeeklyCost = (
            self.calculate_weekly_price(
                intWeeks
            )
        )

        return min(
            dblHourlyCost,
            dblDailyCost,
            dblWeeklyCost
        )

    # ----------------------------------------------------------
    # Display Method
    # ----------------------------------------------------------

    def display_equipment(self):

        print(
            "Equipment:",
            self.strEquipmentName
        )

        print(
            "Hourly Rate: $",
            format(
                self.dblHourlyRate,
                ".2f"
            ),
            sep=""
        )

        print(
            "Daily Rate: $",
            format(
                self.dblDailyRate,
                ".2f"
            ),
            sep=""
        )

        print(
            "Weekly Rate: $",
            format(
                self.dblWeeklyRate,
                ".2f"
            ),
            sep=""
        )
