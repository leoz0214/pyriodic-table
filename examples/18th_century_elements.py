from pyriodic_table.periodictable import PeriodicTable


def eighteenth_century_elements():
    periodic_table = PeriodicTable()
    return periodic_table.get_elements_by_discovery_year(1700, 1799)


if __name__ == "__main__":
    print(eighteenth_century_elements())

# Output:
"""
[hydrogen, beryllium, carbon, nitrogen, oxygen, magnesium, sulfur, chlorine,
titanium, chromium, manganese, cobalt, nickel, zinc, strontium, yttrium,
zirconium, molybdenum, tellurium, barium, tungsten, platinum, bismuth, uranium]
"""