import elements


class PeriodicTable:
    """
    Holds the data for all 118 elements.
    """

    def __init__(self) -> None:
        """
        Creates a new instance of the periodic table.
        """
        self.elements = []
        self.element_names = []

        for atomic_number in range(1, 21):
            element = elements.Element(atomic_number)
            setattr(self, element.name, element)

            self.elements.append(element)
            self.element_names.append(element.name)


if __name__ == "__main__":
    periodic_table = PeriodicTable()
    print(periodic_table.element_names)