from pyriodic_table.periodictable import PeriodicTable


def densest_element():
    periodic_table = PeriodicTable()
    # For elements with no density data, -1 instead.
    return max(periodic_table, key=lambda element: element.density or -1)


if __name__ == "__main__":
    print(densest_element())

# Output:
# osmium

# Correct!