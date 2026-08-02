#<-------------------------------------------------------------->
#
# .py/assignment designation: customer_FMD.py
#
#<-------------------------------------------------------------->

#<-------------------------------------------------------------->
#
# Notes:
# Hello Mrs. Brockman,
# It's Finn again. Here is the customer_FMD.py partition
# of my Final Part 1 submission.
# I hope you have a great day and a great week, ciao!
#
#<-------------------------------------------------------------->


class Customer:

    def __init__(
        self,
        strCustomerName,
        intCustomerID,
        strCouponCode=""
    ):

        self.strCustomerName = strCustomerName
        self.intCustomerID = intCustomerID
        self.strCouponCode = strCouponCode

        self.strRentalBasis = ""
        self.dtmRentalTime = None
        self.intNumberOfItems = 0

    # ----------------------------------------------------------
    # Customer Name Property
    # ----------------------------------------------------------

    @property
    def strCustomerName(self):
        return self.__strCustomerName

    @strCustomerName.setter
    def strCustomerName(self, strCustomerName):

        if strCustomerName == "":
            raise Exception(
                "Customer name cannot be blank."
            )

        self.__strCustomerName = strCustomerName

    # ----------------------------------------------------------
    # Customer ID Property
    # ----------------------------------------------------------

    @property
    def intCustomerID(self):
        return self.__intCustomerID

    @intCustomerID.setter
    def intCustomerID(self, intCustomerID):

        if intCustomerID <= 0:
            raise Exception(
                "Customer ID must be greater than zero."
            )

        self.__intCustomerID = intCustomerID

    # ----------------------------------------------------------
    # Coupon Code Property
    # ----------------------------------------------------------

    @property
    def strCouponCode(self):
        return self.__strCouponCode

    @strCouponCode.setter
    def strCouponCode(self, strCouponCode):

        if strCouponCode is None:
            strCouponCode = ""

        self.__strCouponCode = strCouponCode

    # ----------------------------------------------------------
    # Rental Basis Property
    # ----------------------------------------------------------

    @property
    def strRentalBasis(self):
        return self.__strRentalBasis

    @strRentalBasis.setter
    def strRentalBasis(self, strRentalBasis):

        if (
            strRentalBasis != "" and
            strRentalBasis != "Hourly" and
            strRentalBasis != "Daily" and
            strRentalBasis != "Weekly"
        ):
            raise Exception(
                "Rental basis must be Hourly, Daily, or Weekly."
            )

        self.__strRentalBasis = strRentalBasis

    # ----------------------------------------------------------
    # Rental Time Property
    # ----------------------------------------------------------

    @property
    def dtmRentalTime(self):
        return self.__dtmRentalTime

    @dtmRentalTime.setter
    def dtmRentalTime(self, dtmRentalTime):

        self.__dtmRentalTime = dtmRentalTime

    # ----------------------------------------------------------
    # Number of Items Property
    # ----------------------------------------------------------

    @property
    def intNumberOfItems(self):
        return self.__intNumberOfItems

    @intNumberOfItems.setter
    def intNumberOfItems(self, intNumberOfItems):

        if intNumberOfItems < 0:
            raise Exception(
                "Number of rental items cannot be negative."
            )

        self.__intNumberOfItems = intNumberOfItems

    # ----------------------------------------------------------
    # Coupon Qualification Method
    # ----------------------------------------------------------

    def qualifies_for_coupon(self):

        return (
            len(self.strCouponCode) >= 3 and
            self.strCouponCode.upper().endswith("BBP")
        )

    # ----------------------------------------------------------
    # Family Discount Qualification Method
    # ----------------------------------------------------------

    def qualifies_for_family_discount(self):

        return (
            self.intNumberOfItems >= 3 and
            self.intNumberOfItems <= 5
        )

    # ----------------------------------------------------------
    # Return Equipment Information Method
    # ----------------------------------------------------------

    def return_equipment(self):

        if (
            self.strRentalBasis != "" and
            self.dtmRentalTime is not None and
            self.intNumberOfItems > 0
        ):

            return (
                self.dtmRentalTime,
                self.strRentalBasis,
                self.intNumberOfItems
            )

        return None

    # ----------------------------------------------------------
    # Display Customer Method
    # ----------------------------------------------------------

    def display_customer(self):

        print(
            "Customer Name:",
            self.strCustomerName
        )

        print(
            "Customer ID:",
            self.intCustomerID
        )

        if self.strCouponCode == "":
            print(
                "Coupon Code: None"
            )

        else:
            print(
                "Coupon Code:",
                self.strCouponCode
            )

        print(
            "Rental Basis:",
            self.strRentalBasis
            if self.strRentalBasis != ""
            else "Not Assigned"
        )

        print(
            "Number of Items:",
            self.intNumberOfItems
        )
