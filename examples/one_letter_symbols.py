from pyriodic_table.periodictable import PeriodicTable


def one_letter_symbols():
    return [element.symbol
        for element in PeriodicTable().get_elements_by_symbol(
            lambda symbol: len(symbol) == 1)
    ]


if __name__ == "__main__":
    print(one_letter_symbols())

# Output:
# ['H', 'B', 'C', 'N', 'O', 'F', 'P', 'S', 'K', 'V', 'Y', 'I', 'W', 'U']

# Correct!