from typing import Callable

import chemelements
from exceptions import ElementDoesNotExist


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
            element = chemelements.Element(atomic_number)

            setattr(self, element.name, element)
            setattr(self, element.symbol.lower(), element)
            setattr(self, element.symbol.title(), element)

            self._elements.append(element)
    
    def get_element_by_name(self, name: str) -> chemelements.Element:
        """
        Finds element by its name. Case-insensitive.
        """
        name = name.lower()

        for element in self:
            if element.name == name:
                return element

        raise ElementDoesNotExist(f"No such element with the name: {name}")
    
    def get_elements_by_name(
        self, function_check: Callable) -> list[chemelements.Element]:
        """
        Finds elements whose name evaluates to True
        when passed into a function.

        For example, given the following functions:

        lambda name: name.startswith("bo");
        [boron, bohrium] would be returned.

        lambda x: len(x) < 4;
        [tin] would be returned

        Note that the element name is passed into the function.
        """
        return [element for element in self if function_check(element.name)]
    
    def get_element_by_atomic_number(
        self, atomic_number: int) -> chemelements.Element:
        """
        Finds element by its atomic number (number of protons).
        """
        for element in self:
            if element.atomic_number == atomic_number:
                return element
        
        raise ElementDoesNotExist(
            f"No such element with the atomic number: {atomic_number}")
    
    def get_elements_by_atomic_number(
        self, start: int, stop: int, step: int = 1
        ) -> list[chemelements.Element]:
        """
        Finds elements which have an atomic number within a particular range.
        Works just like the range() function,
        so the 'stop' atomic number is not included.
        """
        if start < 1:
            # First atomic number is one, so no point in checking lower.
            start = 1

        if stop > NUMBER_OF_ELEMENTS + 1:
            # Last atomic number is 118, so no point in checking higher.
            stop = NUMBER_OF_ELEMENTS + 1

        return [
            self._elements[atomic_number - 1]
            for atomic_number in range(start, stop, step)]
    
    def get_element_by_symbol(self, symbol: str) -> chemelements.Element:
        """
        Finds element by its symbol. Case-insensitive.
        """
        symbol = symbol.title()
        
        for element in self:
            if element.symbol == symbol:
                return element
        
        raise ElementDoesNotExist(f"No such element with the symbol: {symbol}")
    
    def get_elements_by_symbol(
        self, function_check: Callable) -> list[chemelements.Element]:
        """
        Finds elements whose symbol evaluates to True
        when passed into a function.

        For example, given the following function:

        lambda symbol: len(symbol) == 1;
        [hydrogen, boron, carbon, nitrogen, oxygen, fluorine,
        phosphorus,sulfur, potassium, vanadium, yttrium,
        iodine, tungsten, uranium] would be returned.

        Note that the element symbol is passed into the function.
        """
        return [element for element in self if function_check(element.symbol)]
    
    def get_elements_by_state(self, state: str) -> list[chemelements.Element]:
        """
        Finds elements at a particular state at room temperature.
        State must either be 'solid', 'liquid' or 'gas'
        """
        if state not in ("solid", "liquid", "gas"):
            raise ValueError(
                "State must either be 'solid', 'liquid' or 'gas'")

        return [
            element for element in self if element.state == state]
        
    @property
    def elements(self) -> list[chemelements.Element]:
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
    
    def __reversed__(self) -> list[chemelements.Element]:
        """
        Returns the elements in reverse order.
        """
        return self._elements[::-1]


if __name__ == "__main__":
    periodic_table = PeriodicTable()
    print(periodic_table.get_elements_by_atomic_number(1, 10, 2))