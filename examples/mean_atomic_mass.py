from pyriodic_table.periodictable import PeriodicTable


def mean_atomic_mass():
    periodic_table = PeriodicTable()
    return sum(element.atomic_mass for element in periodic_table) / 118


if __name__ == "__main__":
    print(mean_atomic_mass())

# Output:
# 146.49684576271187