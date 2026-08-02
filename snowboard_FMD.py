#<-------------------------------------------------------------->
#
# .py/assignment designation: snowboard_FMD.py
#
#<-------------------------------------------------------------->

#<-------------------------------------------------------------->
#
# Notes:
# Hello Mrs. Brockman,
# It's Finn again. Here is the snowboard_FMD.py
# partition of my Final Part 1 submission.
# I hope you have a great day and a great week, ciao!
#
#<-------------------------------------------------------------->

from rental_equipment_FMD import RentalEquipment


class Snowboard(RentalEquipment):

    def __init__(self):

        RentalEquipment.__init__(
            self,
            "Snowboard",
            10.00,
            40.00,
            160.00
        )

    # ----------------------------------------------------------
    # Overridden Display Method
    # ----------------------------------------------------------

    def display_equipment(self):

        print("Equipment Type: Snowboard")

        RentalEquipment.display_equipment(self)
