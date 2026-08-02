#<-------------------------------------------------------------->
#
# .py/assignment designation: rental_shop_FMD.py
#
#<-------------------------------------------------------------->

#<-------------------------------------------------------------->
#
# Notes:
# Hello Mrs. Brockman,
# It's Finn again. Here is the rental_shop_FMD.py partition
# of my Final Part 1 submission.
# I hope you have a great day and a great week. Ciao!
#
#<-------------------------------------------------------------->


class RentalShop:

    def __init__(
        self,
        intStartingSkiInventory,
        intStartingSnowboardInventory
    ):

        self.intStartingSkiInventory = (
            intStartingSkiInventory
        )

        self.intStartingSnowboardInventory = (
            intStartingSnowboardInventory
        )

        self.intAvailableSkis = (
            intStartingSkiInventory
        )

        self.intAvailableSnowboards = (
            intStartingSnowboardInventory
        )

        self.intDailySkisRented = 0
        self.intDailySnowboardsRented = 0
        self.dblDailyRevenue = 0.0

    # ----------------------------------------------------------
    # Starting Ski Inventory Property
    # ----------------------------------------------------------

    @property
    def intStartingSkiInventory(self):
        return self.__intStartingSkiInventory

    @intStartingSkiInventory.setter
    def intStartingSkiInventory(
        self,
        intStartingSkiInventory
    ):

        if intStartingSkiInventory < 0:
            raise Exception(
                "Starting ski inventory cannot be negative."
            )

        self.__intStartingSkiInventory = (
            intStartingSkiInventory
        )

    # ----------------------------------------------------------
    # Starting Snowboard Inventory Property
    # ----------------------------------------------------------

    @property
    def intStartingSnowboardInventory(self):
        return self.__intStartingSnowboardInventory

    @intStartingSnowboardInventory.setter
    def intStartingSnowboardInventory(
        self,
        intStartingSnowboardInventory
    ):

        if intStartingSnowboardInventory < 0:
            raise Exception(
                "Starting snowboard inventory cannot be negative."
            )

        self.__intStartingSnowboardInventory = (
            intStartingSnowboardInventory
        )

    # ----------------------------------------------------------
    # Available Skis Property
    # ----------------------------------------------------------

    @property
    def intAvailableSkis(self):
        return self.__intAvailableSkis

    @intAvailableSkis.setter
    def intAvailableSkis(self, intAvailableSkis):

        if intAvailableSkis < 0:
            raise Exception(
                "Available ski inventory cannot be negative."
            )

        self.__intAvailableSkis = intAvailableSkis

    # ----------------------------------------------------------
    # Available Snowboards Property
    # ----------------------------------------------------------

    @property
    def intAvailableSnowboards(self):
        return self.__intAvailableSnowboards

    @intAvailableSnowboards.setter
    def intAvailableSnowboards(
        self,
        intAvailableSnowboards
    ):

        if intAvailableSnowboards < 0:
            raise Exception(
                "Available snowboard inventory cannot be negative."
            )

        self.__intAvailableSnowboards = (
            intAvailableSnowboards
        )

    # ----------------------------------------------------------
    # Daily Skis Rented Property
    # ----------------------------------------------------------

    @property
    def intDailySkisRented(self):
        return self.__intDailySkisRented

    @intDailySkisRented.setter
    def intDailySkisRented(self, intDailySkisRented):

        if intDailySkisRented < 0:
            raise Exception(
                "Daily ski rentals cannot be negative."
            )

        self.__intDailySkisRented = intDailySkisRented

    # ----------------------------------------------------------
    # Daily Snowboards Rented Property
    # ----------------------------------------------------------

    @property
    def intDailySnowboardsRented(self):
        return self.__intDailySnowboardsRented

    @intDailySnowboardsRented.setter
    def intDailySnowboardsRented(
        self,
        intDailySnowboardsRented
    ):

        if intDailySnowboardsRented < 0:
            raise Exception(
                "Daily snowboard rentals cannot be negative."
            )

        self.__intDailySnowboardsRented = (
            intDailySnowboardsRented
        )

    # ----------------------------------------------------------
    # Daily Revenue Property
    # ----------------------------------------------------------

    @property
    def dblDailyRevenue(self):
        return self.__dblDailyRevenue

    @dblDailyRevenue.setter
    def dblDailyRevenue(self, dblDailyRevenue):

        if dblDailyRevenue < 0:
            raise Exception(
                "Daily revenue cannot be negative."
            )

        self.__dblDailyRevenue = dblDailyRevenue

    # ----------------------------------------------------------
    # Display Inventory Method
    # ----------------------------------------------------------

    def display_inventory(self):

        print(
            "Available Skis:",
            self.intAvailableSkis
        )

        print(
            "Available Snowboards:",
            self.intAvailableSnowboards
        )

    # ----------------------------------------------------------
    # Rent Skis Method
    # ----------------------------------------------------------

    def rent_skis(self, intNumberOfSkis):

        if intNumberOfSkis <= 0:
            raise Exception(
                "Number of skis rented must be greater than zero."
            )

        if intNumberOfSkis > self.intAvailableSkis:
            raise Exception(
                "Not enough skis are available."
            )

        self.intAvailableSkis = (
            self.intAvailableSkis -
            intNumberOfSkis
        )

        self.intDailySkisRented = (
            self.intDailySkisRented +
            intNumberOfSkis
        )

        return True

    # ----------------------------------------------------------
    # Rent Snowboards Method
    # ----------------------------------------------------------

    def rent_snowboards(
        self,
        intNumberOfSnowboards
    ):

        if intNumberOfSnowboards <= 0:
            raise Exception(
                "Number of snowboards rented must be greater than zero."
            )

        if (
            intNumberOfSnowboards >
            self.intAvailableSnowboards
        ):
            raise Exception(
                "Not enough snowboards are available."
            )

        self.intAvailableSnowboards = (
            self.intAvailableSnowboards -
            intNumberOfSnowboards
        )

        self.intDailySnowboardsRented = (
            self.intDailySnowboardsRented +
            intNumberOfSnowboards
        )

        return True

    # ----------------------------------------------------------
    # Rent Mixed Equipment Method
    # ----------------------------------------------------------

    def rent_equipment(
        self,
        intNumberOfSkis,
        intNumberOfSnowboards
    ):

        if (
            intNumberOfSkis < 0 or
            intNumberOfSnowboards < 0
        ):
            raise Exception(
                "Rental quantities cannot be negative."
            )

        if (
            intNumberOfSkis == 0 and
            intNumberOfSnowboards == 0
        ):
            raise Exception(
                "At least one rental item is required."
            )

        if intNumberOfSkis > self.intAvailableSkis:
            raise Exception(
                "Not enough skis are available."
            )

        if (
            intNumberOfSnowboards >
            self.intAvailableSnowboards
        ):
            raise Exception(
                "Not enough snowboards are available."
            )

        if intNumberOfSkis > 0:
            self.rent_skis(
                intNumberOfSkis
            )

        if intNumberOfSnowboards > 0:
            self.rent_snowboards(
                intNumberOfSnowboards
            )

        return True

    # ----------------------------------------------------------
    # Return Skis Method
    # ----------------------------------------------------------

    def return_skis(self, intNumberOfSkis):

        if intNumberOfSkis <= 0:
            raise Exception(
                "Number of returned skis must be greater than zero."
            )

        if (
            self.intAvailableSkis +
            intNumberOfSkis >
            self.intStartingSkiInventory
        ):
            raise Exception(
                "Returned skis would exceed starting inventory."
            )

        self.intAvailableSkis = (
            self.intAvailableSkis +
            intNumberOfSkis
        )

        return True

    # ----------------------------------------------------------
    # Return Snowboards Method
    # ----------------------------------------------------------

    def return_snowboards(
        self,
        intNumberOfSnowboards
    ):

        if intNumberOfSnowboards <= 0:
            raise Exception(
                "Number of returned snowboards must be greater than zero."
            )

        if (
            self.intAvailableSnowboards +
            intNumberOfSnowboards >
            self.intStartingSnowboardInventory
        ):
            raise Exception(
                "Returned snowboards would exceed starting inventory."
            )

        self.intAvailableSnowboards = (
            self.intAvailableSnowboards +
            intNumberOfSnowboards
        )

        return True

    # ----------------------------------------------------------
    # Return Mixed Equipment Method
    # ----------------------------------------------------------

    def return_equipment(
        self,
        intNumberOfSkis,
        intNumberOfSnowboards
    ):

        if (
            intNumberOfSkis < 0 or
            intNumberOfSnowboards < 0
        ):
            raise Exception(
                "Return quantities cannot be negative."
            )

        if (
            intNumberOfSkis == 0 and
            intNumberOfSnowboards == 0
        ):
            raise Exception(
                "At least one returned item is required."
            )

        if (
            self.intAvailableSkis +
            intNumberOfSkis >
            self.intStartingSkiInventory
        ):
            raise Exception(
                "Returned skis would exceed starting inventory."
            )

        if (
            self.intAvailableSnowboards +
            intNumberOfSnowboards >
            self.intStartingSnowboardInventory
        ):
            raise Exception(
                "Returned snowboards would exceed starting inventory."
            )

        if intNumberOfSkis > 0:
            self.return_skis(
                intNumberOfSkis
            )

        if intNumberOfSnowboards > 0:
            self.return_snowboards(
                intNumberOfSnowboards
            )

        return True

    # ----------------------------------------------------------
    # Process Rental Return Method
    # ----------------------------------------------------------

    def process_return(
        self,
        objRental,
        dtmReturnTime=None
    ):

        if objRental is None:
            raise Exception(
                "A rental object is required."
            )

        dblFinalBill = (
            objRental.calculate_final_bill(
                dtmReturnTime
            )
        )

        self.return_equipment(
            objRental.intNumberOfSkis,
            objRental.intNumberOfSnowboards
        )

        self.dblDailyRevenue = (
            self.dblDailyRevenue +
            dblFinalBill
        )

        return dblFinalBill

    # ----------------------------------------------------------
    # Daily Totals Methods
    # ----------------------------------------------------------

    def get_daily_skis_rented(self):

        return self.intDailySkisRented

    def get_daily_snowboards_rented(self):

        return self.intDailySnowboardsRented

    def get_daily_revenue(self):

        return self.dblDailyRevenue

    # ----------------------------------------------------------
    # Display Daily Totals Method
    # ----------------------------------------------------------

    def display_daily_totals(self):

        print(
            "Total Skis Rented Today:",
            self.intDailySkisRented
        )

        print(
            "Total Snowboards Rented Today:",
            self.intDailySnowboardsRented
        )

        print(
            "Total Rental Revenue: $",
            format(
                self.dblDailyRevenue,
                ".2f"
            ),
            sep=""
        )
