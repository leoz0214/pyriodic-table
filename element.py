class Element:
    """
    Represents an element of the periodic table.
    There are currently 118 discovered elements.
    For reference, the first five elements are:
    hydrogen, helium, lithium, beryllium, boron
    """

    def __init__(self, info: str | int):
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

        # Information on units:
        # For melting point and boiling point, the three temperature units:
        # Kelvin, Celsius and Fahrenheit
        # are all supported.
        # Density is in g/cm^3
        match info:
            case "hydrogen" | "h" | 1:
                self.name = "hydrogen"
                self.symbol = "H"
                self.atomic_number = 1
                self.atomic_mass = 1.008
                self.electrons_per_shell = (1,)
                self.state = "gas"
                self.group = 1
                self.period = 1
                self.melting_point_k = 13.99
                self.boiling_point_k = 20.271
                self.density = 0.00008988
                self.stable = True
                self.discoverer = "Henry Cavendish"
                self.discovery_year = 1766
            case _:
                raise ValueError(
                    ("Info does not match the name, symbol or atomic number "
                    "of any element.")
                )

    @property
    def melting_point_c(self):
        if self.melting_point_k is None:
            return None

        return round(self.melting_point_k - 273.15, 10)
    
    @property
    def melting_point_f(self):
        if self.melting_point_k is None:
            return None

        return round(1.8 * (self.melting_point_k - 273.15) + 32, 10)

    @property
    def boiling_point_c(self):
        if self.boiling_point_k is None:
            return None

        return round(self.boiling_point_k - 273.15, 10)

    @property
    def boiling_point_f(self):
        if self.boiling_point_k is None:
            return None

        return round(1.8 * (self.boiling_point_k - 273.15) + 32, 10)
    
    @property
    def protons(self):
        # Number of protons = atomic number
        return self.atomic_number

    @property
    def electrons(self):
        # Number of electrons = atomic number
        return self.atomic_number

    def __repr__(self) -> str:
        lines = [
            f"Name: {self.name}",
            f"Symbol: {self.symbol}",
            f"Atomic number: {self.atomic_number}",
            f"Atomic mass: {self.atomic_mass}"
        ]

        if self.electrons_per_shell is not None:
            lines.append(f"Electrons per shell: {self.electrons_per_shell}")

        if self.state is not None:
            lines.append(f"State (room temperature): {self.state}")

        lines.append(f"Group: {self.group}")
        lines.append(f"Period: {self.period}")

        if self.melting_point_k is not None:
            lines.append(f"Melting point: {self.melting_point_k} K")
        
        if self.boiling_point_k is not None:
            lines.append(f"Boiling point: {self.boiling_point_k} K")
        
        if self.density is not None:
            lines.append(f"Density (room temperature): {self.density} g/cm³")
        
        lines.append(f"Is stable: {self.stable}")
        lines.append(
            f"Discovered by: {self.discoverer} in {self.discovery_year}"
        )

        return "\n".join(lines)




        
    

if __name__ == "__main__":
    print(Element("h"))