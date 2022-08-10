from pyriodic_table.periodictable import (
    PeriodicTable, save_elements_data_to_csv)


def alkali_metals_to_csv():
    alkali_metals = PeriodicTable().alkali_metals
    save_elements_data_to_csv("alkali_metals.csv", alkali_metals)


if __name__ == "__main__":
    alkali_metals_to_csv()
    print("Success!")