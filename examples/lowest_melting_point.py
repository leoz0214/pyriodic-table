from pyriodic_table.periodictable import PeriodicTable


def lowest_melting_point():
    periodic_table = PeriodicTable()

    # Temperature unit does not matter.
    # If element has no melting point data,
    # make it impossible to be the minimum,
    # by setting it to positive infinity.
    
    # This prevents TypeError due to
    # NoneType and [int or float] being uncomparable.

    return min(
        periodic_table, key=lambda element:
        element.melting_point_k
        if element.melting_point_k is not None else float("inf")
    )


if __name__ == "__main__":
    print(lowest_melting_point())

# Output:
# helium

# Correct!