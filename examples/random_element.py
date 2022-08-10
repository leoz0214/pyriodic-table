import random

from pyriodic_table.chemelements import Element
from pyriodic_table.periodictable import PeriodicTable


# Two way


def element_way():
    random_atomic_number = random.randint(1, 118)
    element = Element(random_atomic_number)
    print(element.get_display_data())


def periodic_table_way():
    periodic_table = PeriodicTable()
    element = random.choice(periodic_table.elements)
    print(element.get_display_data())


if __name__ == "__main__":
    element_way()
    print("\n")
    periodic_table_way()


# Example output
"""
Name: Thulium
Symbol: Tm
Atomic number: 69
Atomic mass: 168.93
Electrons per shell: (2, 8, 18, 31, 8, 2)
State (room temperature): Solid
Period: 6
Melting point: 1818 K / 1544.85 °C / 2812.73 °F
Boiling point: 2223 K / 1949.85 °C / 3541.73 °F
Density (room temperature): 9.32 g/cm³
Found naturally: True
Has stable isotope(s): True
Discovered by: Per Teodor Cleve in 1879


Name: Selenium
Symbol: Se
Atomic number: 34
Atomic mass: 78.971
Electrons per shell: (2, 8, 18, 6)
State (room temperature): Solid
Group: 16
Period: 4
Melting point: 494 K / 220.85 °C / 429.53 °F
Boiling point: 958 K / 684.85 °C / 1264.73 °F
Density (room temperature): 4.81 g/cm³
Found naturally: True
Has stable isotope(s): True
Discovered by: Jöns Jakob Berzelius in 1817
"""

