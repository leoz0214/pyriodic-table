import elements


class PeriodicTable:
    """
    Holds the data for all 118 elements.
    """

    def __init__(self) -> None:
        """
        Creates a new instance of the periodic table.
        Gets all the elements of the periodic table by atomic number.
        """
        self.elements = []

        for atomic_number in range(1, 21):
            element = elements.Element(atomic_number)
            setattr(self, element.name, element)

            self.elements.append(element)
    
    def get_elements_by_state(self, state: str) -> list[elements.Element]:
        """
        Finds elements at a particular state at room temperature.
        State must either be 'solid', 'liquid' or 'gas'
        """
        if state not in ("solid", "liquid", "gas"):
            raise ValueError(
                "State must either be 'solid', 'liquid' or 'gas'")

        return [
            element for element in self.elements if element.state == state]

    def __len__(self) -> int:
        """
        Returns the number of elements in the periodic table.
        """
        return len(self.elements)
        

if __name__ == "__main__":
    periodic_table = PeriodicTable()
    print(periodic_table.elements[20-1].get_display_data())
    print(periodic_table.get_elements_by_state("gas"))
    print(len(periodic_table))