from exceptions import ElementDoesNotExist


class Element:
    """
    Represents an element of the periodic table.
    There are currently 118 discovered elements.
    For reference, the first five elements are:
    hydrogen, helium, lithium, beryllium, boron
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
                self.has_stable_isotope = True
                self.discovery = "Henry Cavendish"
                self.discovery_year = 1766

            case "helium" | "he" | 2:
                self.name = "helium"
                self.symbol = "He"
                self.atomic_number = 2
                self.atomic_mass = 4.0026
                self.electrons_per_shell = (2,)
                self.state = "gas"
                self.group = 18
                self.period = 1
                self.melting_point_k = 0.95
                self.boiling_point_k = 4.222
                self.density = 0.0001786
                self.has_stable_isotope = True
                self.discovery = "Pierre Janssen, Norman Lockyer"
                self.discovery_year = 1868

            case "lithium" | "li" | 3:
                self.name = "lithium"
                self.symbol = "Li"
                self.atomic_number = 3
                self.atomic_mass = 6.94
                self.electrons_per_shell = (2, 1)
                self.state = "solid"
                self.group = 1
                self.period = 2
                self.melting_point_k = 453.65
                self.boiling_point_k = 1603
                self.density = 0.534
                self.has_stable_isotope = True
                self.discovery = "Johan August Arfwedson"
                self.discovery_year = 1817
            
            case "beryllium" | "be" | 4:
                self.name = "beryllium"
                self.symbol = "Be"
                self.atomic_number = 4
                self.atomic_mass = 9.0122
                self.electrons_per_shell = (2, 2)
                self.state = "solid"
                self.group = 2
                self.period = 2
                self.melting_point_k = 1560
                self.boiling_point_k = 2742
                self.density = 1.85
                self.has_stable_isotope = True
                self.discovery = "Louis Nicolas Vauquelin"
                self.discovery_year = 1798
            
            case "boron" | "b" | 5:
                self.name = "boron"
                self.symbol = "B"
                self.atomic_number = 5
                self.atomic_mass = 10.81
                self.electrons_per_shell = (2, 3)
                self.state = "solid"
                self.group = 13
                self.period = 2
                self.melting_point_k = 2349
                self.boiling_point_k = 4200
                self.density = 2.34
                self.has_stable_isotope = True
                self.discovery = (
                    "Joseph Louis Gay-Lussac, Louis Jacques Thénard")
                self.discovery_year = 1808
            
            case "carbon" | "c" | 6:
                self.name = "carbon"
                self.symbol = "C"
                self.atomic_number = 6
                self.atomic_mass = 12.011
                self.electrons_per_shell = (2, 4)
                self.state = "solid"
                self.group = 14
                self.period = 2
                self.melting_point_k = 3823
                self.boiling_point_k = 5100
                self.density = 2.27
                self.has_stable_isotope = True
                self.discovery = "Antoine Lavoisier"
                self.discovery_year = 1789
            
            case "nitrogen" | "n" | 7:
                self.name = "nitrogen"
                self.symbol = "N"
                self.atomic_number = 7
                self.atomic_mass = 14.007
                self.electrons_per_shell = (2, 5)
                self.state = "gas"
                self.group = 15
                self.period = 2
                self.melting_point_k = 63.23
                self.boiling_point_k = 77.355
                self.density = 0.00125
                self.has_stable_isotope = True
                self.discovery = "Daniel Rutherford"
                self.discovery_year = 1772
            
            case "oxygen" | "o" | 8:
                self.name = "oxygen"
                self.symbol = "O"
                self.atomic_number = 8
                self.atomic_mass = 15.999
                self.electrons_per_shell = (2, 6)
                self.state = "gas"
                self.group = 16
                self.period = 2
                self.melting_point_k = 54.36
                self.boiling_point_k = 90.188
                self.density = 0.001429
                self.has_stable_isotope = True
                self.discovery = "Carl Wilhelm Scheele"
                self.discovery_year = 1771
            
            case "fluorine" | "f" | 9:
                self.name = "fluorine"
                self.symbol = "F"
                self.atomic_number = 9
                self.atomic_mass = 18.998
                self.electrons_per_shell = (2, 7)
                self.state = "gas"
                self.group = 17
                self.period = 2
                self.melting_point_k = 53.48
                self.boiling_point_k = 85.03
                self.density = 0.001696
                self.has_stable_isotope = True
                self.discovery = "André-Marie Ampère"
                self.discovery_year = 1810
            
            case "neon" | "ne" | 10:
                self.name = "neon"
                self.symbol = "Ne"
                self.atomic_number = 10
                self.atomic_mass = 20.18
                self.electrons_per_shell = (2, 8)
                self.state = "gas"
                self.group = 18
                self.period = 2
                self.melting_point_k = 24.56
                self.boiling_point_k = 27.104
                self.density = 0.0009002
                self.has_stable_isotope = True
                self.discovery = "William Ramsay, Morris Travers"
                self.discovery_year = 1898
            
            case "sodium" | "na" | 11:
                self.name = "sodium"
                self.symbol = "Na"
                self.atomic_number = 11
                self.atomic_mass = 22.99
                self.electrons_per_shell = (2, 8, 1)
                self.state = "solid"
                self.group = 1
                self.period = 3
                self.melting_point_k = 370.944
                self.boiling_point_k = 1156.09
                self.density = 0.968
                self.has_stable_isotope = True
                self.discovery = "Humphry Davy"
                self.discovery_year = 1807 
            
            case "magnesium" | "mg" | 12:
                self.name = "magnesium"
                self.symbol = "Mg"
                self.atomic_number = 12
                self.atomic_mass = 24.305
                self.electrons_per_shell = (2, 8, 2)
                self.state = "solid"
                self.group = 2
                self.period = 3
                self.melting_point_k = 923
                self.boiling_point_k = 1363
                self.density = 1.738
                self.has_stable_isotope = True
                self.discovery = "Joseph Black"
                self.discovery_year = 1755

            case "aluminium" | "al" | 13:
                self.name = "aluminium"
                self.symbol = "Al"
                self.atomic_number = 13
                self.atomic_mass = 26.982
                self.electrons_per_shell = (2, 8, 3)
                self.state = "solid"
                self.group = 13
                self.period = 3
                self.melting_point_k = 933.47
                self.boiling_point_k = 2743
                self.density = 2.7
                self.has_stable_isotope = True
                self.discovery = "Hans Christian Ørsted"
                self.discovery_year = 1824
            
            case "silicon" | "si" | 14:
                self.name = "silicon"
                self.symbol = "Si"
                self.atomic_number = 14
                self.atomic_mass = 28.085
                self.electrons_per_shell = (2, 8, 4)
                self.state = "solid"
                self.group = 14
                self.period = 3
                self.melting_point_k = 1414
                self.boiling_point_k = 3538
                self.density = 2.329
                self.has_stable_isotope = True
                self.discovery = "Jöns Jacob Berzelius"
                self.discovery_year = 1823

            case "phosphorus" | "p" | 15:
                self.name = "phosphorus"
                self.symbol = "P"
                self.atomic_number = 15
                self.atomic_mass = 30.974
                self.electrons_per_shell = (2, 8, 5)
                self.state = "solid"
                self.group = 15
                self.period = 3
                self.melting_point_k = 317.3
                self.boiling_point_k = 553.7
                self.density = 1.823
                self.has_stable_isotope = True
                self.discovery = "Hennig Brand"
                self.discovery_year = 1669

            case "sulfur" | "sulphur" | "s" | 16:
                self.name = "sulfur"
                self.symbol = "S"
                self.atomic_number = 16
                self.atomic_mass = 32.06
                self.electrons_per_shell = (2, 8, 6)
                self.state = "solid"
                self.group = 16
                self.period = 3
                self.melting_point_k = 388.36
                self.boiling_point_k = 717.8
                self.density = 2.07
                self.has_stable_isotope = True
                self.discovery = "Antoine Lavoisier"
                self.discovery_year = 1777

            case "chlorine" | "cl" | 17:
                self.name = "chlorine"
                self.symbol = "Cl"
                self.atomic_number = 17
                self.atomic_mass = 35.45
                self.electrons_per_shell = (2, 8, 7)
                self.state = "gas"
                self.group = 17
                self.period = 3
                self.melting_point_k = 171.6
                self.boiling_point_k = 239.11
                self.density = 0.0032
                self.has_stable_isotope = True
                self.discovery = "Carl Wilhelm Scheele"
                self.discovery_year = 1774
            
            case "argon" | "ar" | 18:
                self.name = "argon"
                self.symbol = "Ar"
                self.atomic_number = 18
                self.atomic_mass = 39.95
                self.electrons_per_shell = (2, 8, 8)
                self.state = "gas"
                self.group = 18
                self.period = 3
                self.melting_point_k = 83.81
                self.boiling_point_k = 87.302
                self.density = 0.001784
                self.has_stable_isotope = True
                self.discovery = "Lord Rayleigh, William Ramsay"
                self.discovery_year = 1894

            case "potassium" | "k" | 19:
                self.name = "potassium"
                self.symbol = "K"
                self.atomic_number = 19
                self.atomic_mass = 39.098
                self.electrons_per_shell = (2, 8, 8, 1)
                self.state = "solid"
                self.group = 1
                self.period = 4
                self.melting_point_k = 336.7
                self.boiling_point_k = 1032
                self.density = 0.89
                self.has_stable_isotope = True
                self.discovery = "Humphry Davy"
                self.discovery_year = 1807

            case "calcium" | "ca" | 20:
                self.name = "calcium"
                self.symbol = "Ca"
                self.atomic_number = 20
                self.atomic_mass = 40.078
                self.electrons_per_shell = (2, 8, 8, 2)
                self.state = "solid"
                self.group = 2
                self.period = 4
                self.melting_point_k = 1115
                self.boiling_point_k = 1757
                self.density = 1.55
                self.has_stable_isotope = True
                self.discovery = "Humphry Davy"
                self.discovery_year = 1808

            case _:
                raise ElementDoesNotExist(
                    ("Info does not match the name, symbol or atomic number "
                    "of any element.")
                )

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
            f"Atomic mass: {self.atomic_mass}"
        ]

        if self.electrons_per_shell is not None:
            lines.append(f"Electrons per shell: {self.electrons_per_shell}")

        if self.state is not None:
            lines.append(f"State (room temperature): {self.state.title()}")

        lines.append(f"Group: {self.group}")
        lines.append(f"Period: {self.period}")

        if self.melting_point_k is not None:
            lines.append(
                "Melting point: {} K / {} °C / {} °F".format(
                    self.melting_point_k, 
                    self.melting_point_c,
                    self.melting_point_f
                )
            )
        
        if self.boiling_point_k is not None:
            lines.append(
                "Melting point: {} K / {} °C / {} °F".format(
                    self.boiling_point_k, 
                    self.boiling_point_c,
                    self.boiling_point_f
                )
            )
        
        if self.density is not None:
            lines.append(f"Density (room temperature): {self.density} g/cm³")
        
        lines.append(f"Has stable isotope(s): {self.has_stable_isotope}")
        lines.append(
            f"Discovered by: {self.discovery} in {self.discovery_year}")

        return "\n".join(lines)


if __name__ == "__main__":
    for i in range(1, 21):
        print(Element(i).get_display_data())