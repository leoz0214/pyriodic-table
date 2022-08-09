import json

from data import DATA
from exceptions import ElementDoesNotExist


class Element:
    """
    Represents an element of the periodic table.
    There are currently 118 discovered elements.

    For reference, the first five elements are:
    hydrogen, helium, lithium, beryllium, boron

    And the last five elements are:
    flerovium, moscovium, livermorium, tennessine, oganesson
    """

    def __init__(self, info: str | int) -> None:
        """
        The 'info' parameter allows for 3 ways to identify an element:
        - Name of element e.g hydrogen <str>
        - Symbol of element e.g H for hydrogen <str>
        - Atomic number e.g 1 for hydrogen <int>

        Name/symbol are case-insensitive.
        """
        # Name/symbol are case-insensitive.
        if isinstance(info, str):
            info = info.lower()
        elif not isinstance(info, int):
            raise TypeError(
                ("Invalid argument type for parameter 'info', expected type "
                "<'str'> (name/symbol) or type <'int'> (atomic number), "
                f"not type <{str(type(info)).split()[1]}")
            )

        # For melting point and boiling point, the three temperature units
        # Kelvin, Celsius and Fahrenheit are all supported.
        # Density is in g/cm^3

        for element_data in DATA:
            if info in (
                element_data["name"],
                element_data["symbol"].lower(),
                element_data["atomic_number"]
            ):
                # Sets all attributes of element from dict.

                self.name = element_data["name"]
                self.symbol = element_data["symbol"]
                self.atomic_number = element_data["atomic_number"]
                self.atomic_mass = element_data["atomic_mass"]
                self.electrons_per_shell = element_data["electrons_per_shell"]
                self.state = element_data["state"]
                self.group = element_data["group"]
                self.period = element_data["period"]
                self.melting_point_k = element_data["melting_point_k"]
                self.boiling_point_k = element_data["boiling_point_k"]
                self.density = element_data["density"]
                self.natural = element_data["natural"]
                self.has_stable_isotope = element_data["has_stable_isotope"]
                self.discovery = element_data["discovery"]
                self.discovery_year = element_data["discovery_year"]
                
                break
        else:
            raise ElementDoesNotExist(
                ("Info does not match the name, symbol or atomic number "
                f"of any element: {info}"))

    @property
    def melting_point_c(self) -> float:
        if self.melting_point_k is None:
            return None

        return round(self.melting_point_k - 273.15, 10)
    
    @property
    def melting_point_f(self) -> float:
        if self.melting_point_k is None:
            return None

        return round(1.8 * (self.melting_point_k - 273.15) + 32, 10)

    @property
    def boiling_point_c(self) -> float:
        if self.boiling_point_k is None:
            return None

        return round(self.boiling_point_k - 273.15, 10)

    @property
    def boiling_point_f(self) -> float:
        if self.boiling_point_k is None:
            return None

        return round(1.8 * (self.boiling_point_k - 273.15) + 32, 10)
    
    @property
    def protons(self) -> int:
        # Number of protons = atomic number
        return self.atomic_number

    @property
    def electrons(self) -> int:
        # Number of electrons = atomic number
        return self.atomic_number
    
    def __repr__(self) -> str:
        return self.name

    def get_display_data(self) -> str:
        """
        Returns available element information as one string.
        Useful for outputting element data to the console.
        """
        lines = [
            f"Name: {self.name.title()}",
            f"Symbol: {self.symbol}",
            f"Atomic number: {self.atomic_number}",
            f"Atomic mass: {self.atomic_mass}"]

        if self.electrons_per_shell is not None:
            lines.append(f"Electrons per shell: {self.electrons_per_shell}")

        if self.state is not None:
            lines.append(f"State (room temperature): {self.state.title()}")

        if self.group is not None:
            lines.append(f"Group: {self.group}")
        lines.append(f"Period: {self.period}")

        if self.melting_point_k is not None:
            lines.append(
                "Melting point: {} K / {} °C / {} °F".format(
                    self.melting_point_k, 
                    self.melting_point_c,
                    self.melting_point_f))
        
        if self.boiling_point_k is not None:
            lines.append(
                "Boiling point: {} K / {} °C / {} °F".format(
                    self.boiling_point_k,
                    self.boiling_point_c,
                    self.boiling_point_f))
        
        if self.density is not None:
            lines.append(f"Density (room temperature): {self.density} g/cm³")
        
        lines.append(f"Found naturally: {self.natural}")
        lines.append(f"Has stable isotope(s): {self.has_stable_isotope}")

        if self.discovery is not None:
            discovery_line = f"Discovered by: {self.discovery}"

            if self.discovery_year is not None:
                discovery_line += " in {}".format(
                    self.discovery_year if self.discovery_year >= 0
                    else f"{abs(self.discovery_year)} BC")

            lines.append(discovery_line)
        
        elif self.discovery_year is not None:
            lines.append("Discovered in {}".format(
                    self.discovery_year if self.discovery_year >= 0
                    else f"{abs(self.discovery_year)} BC"))

        return "\n".join(lines)
    
    def _validate_object_to_compare(self, obj) -> None:
        if not isinstance(obj, Element):
            raise TypeError("Cannot compare <{} with Element.".format(
                str(type(obj)).split()[1]))
    
    def __eq__(self, element) -> bool:
        """
        Checks if two elements instances are the same (atomic number).
        Opposite is != (not equal)
        """
        if not isinstance(element, Element):
            return False
        
        return self.atomic_number == element.atomic_number
    
    def __gt__(self, element) -> bool:
        """
        Checks if the element has a greater atomic number than another.
        """
        self._validate_object_to_compare(element)

        return self.atomic_number > element.atomic_number
    
    def __ge__(self, element) -> bool:
        """
        Checks if the element has a greater atomic number than
        or equal to another.
        """
        self._validate_object_to_compare(element)
        
        return self.atomic_number >= element.atomic_number

    def __lt__(self, element) -> bool:
        """
        Checks if the element has a lower atomic number than another.
        """
        self._validate_object_to_compare(element)
        
        return self.atomic_number < element.atomic_number
    
    def __le__(self, element) -> bool:
        """
        Checks if the element has a lower atomic number than
        or equal to another.
        """
        self._validate_object_to_compare(element)
        
        return self.atomic_number <= element.atomic_number
    
    def asdict(self) -> dict:
        """
        Returns a dictionary of the element data.
        """
        return dict(self.__dict__) | {
            # Additional element data (properties).
            "protons": self.protons,
            "electrons": self.electrons,
            "melting_point_c": self.melting_point_c,
            "melting_point_f": self.melting_point_f,
            "boiling_point_c": self.boiling_point_c,
            "boiling_point_f": self.boiling_point_f
        }
    
    def to_json(
        self, indent: int | None = None, compact: bool = False) -> str:
        """
        Returns element data as a JSON string.
        'compact' to True removes all unnecessary whitespace in
        the JSON string.
        """
        dict_data = self.asdict()

        if compact:
            return json.dumps(dict_data, indent=indent, separators=(",", ":"))

        return json.dumps(dict_data, indent=indent)