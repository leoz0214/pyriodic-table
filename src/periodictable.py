import elements


NUMBER_OF_ELEMENTS = 118


class PeriodicTable:
    """
    Holds the data for all 118 elements.
    """

    def __init__(self) -> None:
        """
        Creates a new instance of the periodic table.
        Gets all the elements of the periodic table by atomic number.
        """
        self._elements = []

        for atomic_number in range(1, NUMBER_OF_ELEMENTS + 1):
            element = elements.Element(atomic_number)
            setattr(self, element.name, element)
            setattr(self, element.symbol.lower(), element)
            setattr(self, element.symbol.title(), element)

            self._elements.append(element)
    
    def get_elements_by_state(self, state: str) -> list[elements.Element]:
        """
        Finds elements at a particular state at room temperature.
        State must either be 'solid', 'liquid' or 'gas'
        """
        if state not in ("solid", "liquid", "gas"):
            raise ValueError(
                "State must either be 'solid', 'liquid' or 'gas'")

        return [
            element for element in self._elements if element.state == state]
        
    @property
    def elements(self):
        return self._elements

    def __len__(self) -> int:
        """
        Returns the number of elements in the periodic table.
        """
        return len(self._elements)
    
    def __iter__(self) -> None:
        """
        Iterates through the elements of the periodic table.
        """
        for element in self._elements:
            yield element
        

if __name__ == "__main__":
    periodic_table = PeriodicTable()
    print(periodic_table.Kr.atomic_mass)