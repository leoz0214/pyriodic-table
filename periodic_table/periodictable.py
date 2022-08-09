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

        self._elements_with_stable_isotope = []
        self._elements_without_stable_isotope = []

        self._alkali_metals = []
        self._alkaline_earth_metals = []
        self._lanthanides = []
        self._actinides = []
        self._halogens = []
        self._noble_gases = []

        for atomic_number in range(1, NUMBER_OF_ELEMENTS + 1):
            element = chemelements.Element(atomic_number)

            setattr(self, element.name, element)
            setattr(self, element.symbol.lower(), element)
            setattr(self, element.symbol.title(), element)

            self._elements.append(element)

            if element.group == 1 and element.atomic_number != 1:
                self._alkali_metals.append(element)
            elif element.group == 2:
                self._alkaline_earth_metals.append(element)
            elif element.group == 17:
                self._halogens.append(element)
            elif element.group == 18:
                self._noble_gases.append(element)

            if 57 <= element.atomic_number <= 71:
                self._lanthanides.append(element)
            elif 89 <= element.atomic_number <= 103:
                self._actinides.append(element)

            if element.has_stable_isotope:
                self._elements_with_stable_isotope.append(element)
            else:
                self._elements_without_stable_isotope.append(element)
    
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
        if 1 <= atomic_number <= NUMBER_OF_ELEMENTS:
            return self._elements[atomic_number - 1]
        
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
        State must either be 'solid', 'liquid' or 'gas',
        or their corresponding shorthands - 's', 'l', 'g'.
        Case-insensitive
        """
        state = state.lower()

        # Accepts shorthand for each of the 3 states.
        state = {"s": "solid", "l": "liquid", "g": "gas"}.get(state, state)

        if state not in ("solid", "liquid", "gas"):
            raise ValueError(
                "State must either be 'solid', 'liquid' or 'gas'")

        return [
            element for element in self if element.state == state]
    
    def get_elements_by_group(
        self, group: int | None) -> list[chemelements.Element]:
        """
        Finds elements in a particular Group (column).
        If 'group' is passed as None, all the elements not in
        a group are returned.
        """
        return [element for element in self if element.group == group]

    def get_elements_by_period(
        self, period: int) -> list[chemelements.Element]:
        """
        Finds elements in a particular Period (row).
        """
        return [element for element in self if element.period == period]
    
    def _get_elements_by_temperature(func: Callable) -> Callable:
        def wrap(
            self, minimum: int | float, maximum: int | float, unit: str = "k"
        ) -> list[chemelements.Element]:
            unit = unit.lower()

            if unit not in ("k", "c", "f"):
                raise ValueError("Unit must either be 'k', 'f' or 'c'")
            
            elements = []
            target_attribute = func()

            for element in self:
                # Gets required melting/boiling point in required unit.
                temperature = getattr(element, f"{target_attribute}_{unit}")

                if temperature and minimum <= temperature <= maximum:
                    elements.append(element)  

            return elements
        return wrap

    @_get_elements_by_temperature
    def get_elements_by_melting_point():
        """
        Finds elements with a melting point in a given range.
        Unit must either be 'k' (kelvin), 'c' (celsius), or
        'f' (fahrenheit). Case-insensitive.
        """
        return "melting_point"
    
    @_get_elements_by_temperature
    def get_elements_by_boiling_point():
        """
        Finds elements with a boiling point in a given range.
        Unit must either be 'k' (kelvin), 'c' (celsius), or
        'f' (fahrenheit). Case-insensitive.
        """
        return "boiling_point"
    
    def get_elements_by_density(
        self, minimum: int | float, maximum: int | float
    ) -> list[chemelements.Element]:
        """
        Finds elements with a density in a given range.
        Unit = g/cm^3
        """
        return [
            element for element in self
            if element.density and minimum <= element.density <= maximum]
    
    def get_elements_by_discovery_year(
        self, minimum: int, maximum: int) -> list[chemelements.Element]:
        """
        Finds elements discovered within a given time period.
        For BC years, use negative integers.
        For example, for 5000 BC, use -5000
        """
        return [
            element for element in self
            if element.discovery_year
            and minimum <= element.discovery_year <= maximum]
        
    @property
    def elements(self) -> list[chemelements.Element]:
        return self._elements
    
    @property
    def elements_with_stable_isotope(self) -> list[chemelements.Element]:
        return self._elements_with_stable_isotope
    
    @property
    def elements_without_stable_isotope(self) -> list[chemelements.Element]:
        return self._elements_without_stable_isotope
    
    @property
    def alkali_metals(self) -> list[chemelements.Element]:
        return self._alkali_metals
    
    @property
    def alkaline_earth_metals(self) -> list[chemelements.Element]:
        return self._alkaline_earth_metals
    
    @property
    def lanthanides(self) -> list[chemelements.Element]:
        return self._lanthanides
    
    @property
    def actinides(self) -> list[chemelements.Element]:
        return self._actinides
    
    @property
    def halogens(self) -> list[chemelements.Element]:
        return self._halogens
    
    @property
    def noble_gases(self) -> list[chemelements.Element]:
        return self._noble_gases

    def __len__(self) -> int:
        """
        Returns the number of elements in the periodic table (118).
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
    
    def __repr__(self) -> str:
        """
        Displays basic element data as a string.
        """
        return " | ".join(
            ["{} {} ({})".format(
            element.atomic_number, element.name, element.symbol)
            for element in self]
        )
    
    def __contains__(self, info: str) -> bool:
        """
        Checks if name/symbol matches an existing element.
        Case-insensitive.
        """
        # For name check.
        lower = info.lower()
        # For symbol check.
        title = info.title()
    
        return any(
            lower == element.name or title == element.symbol
            for element in self)

    def asdict(
        self, elements_to_dict: bool = True, elements_only: bool = False
        ) -> dict:
        """
        Returns a dictionary of the periodic table data; 
        also casting element data into dictionaries if specified.
        If 'elements_only' is passed as True, only a dictionary
        of the elements will be returned, not the different
        categories of elements alongside.
        """
        if elements_only:
            
            if not elements_to_dict:
                return {element.name: element for element in self}
            
            return {element.name: element.asdict() for element in self}


        if not elements_to_dict:
            return {
                "elements": {element.name: element for element in self},
                "elements_with_stable_isotope":
                self._elements_with_stable_isotope,
                "elements_without_stable_isotope":
                self.elements_without_stable_isotope,
                "alkali_metals": self._alkali_metals,
                "alkaline_earth_metals": self._alkaline_earth_metals,
                "lanthanides": self._lanthanides,
                "actinides": self._actinides,
                "halogens": self._halogens,
                "noble_gases": self._noble_gases
            }

        # Converts all elements' data into dicts once
        # for use multiple times below.
        element_dicts = {element.name: element.asdict() for element in self}

        return {
            "elements": element_dicts,
            "elements_with_stable_isotope": [
                element_dicts[element.name]
                for element in self._elements_with_stable_isotope],
            "elements_without_stable_isotope": [
                element_dicts[element.name]
                for element in self._elements_without_stable_isotope],
            "alkali_metals": [
                element_dicts[element.name]
                for element in self._alkali_metals],
            "alkaline_earth_metals": [
                element_dicts[element.name]
                for element in self._alkaline_earth_metals],
            "lanthanides": [
                element_dicts[element.name]
                for element in self._lanthanides],
            "actinides": [
                element_dicts[element.name]
                for element in self._actinides],
            "halogens": [
                element_dicts[element.name]
                for element in self._halogens],
            "noble_gases": [
                element_dicts[element.name]
                for element in self._noble_gases]
        }