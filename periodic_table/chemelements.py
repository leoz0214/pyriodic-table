import json

from exceptions import ElementDoesNotExist


class Element:
    """
    Represents an element of the periodic table.
    There are currently 118 discovered elements.
    For reference, the first five elements are:
    hydrogen, helium, lithium, beryllium, boron
    """

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
                    else f"{abs(self.discovery_year)} BC")
                )

        return "\n".join(lines)
    
    def __eq__(self, element) -> bool:
        """
        Checks if two elements instances are the same (atomic number).
        Opposite is != (not equal)
        """
        if not isinstance(element, Element):
            raise False
        
        return self.atomic_number == element.atomic_number
    
    def __gt__(self, element) -> bool:
        """
        Checks if the element has a greater atomic number than another.
        Opposite is < (less than)
        """
        if not isinstance(element, Element):
            return False
        
        return self.atomic_number > element.atomic_number
    
    def __ge__(self, element) -> bool:
        """
        Checks if the element has a greater atomic number than
        or equal to another. Opposite is <= (less than or equal)
        """
        if not isinstance(element, Element):
            return False
        
        return self.atomic_number >= element.atomic_number
    
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
        Returns element data in JSON form.
        'compact' to True removes all unnecessary whitespace in
        the JSON string.
        """
        dict_data = self.asdict()

        if compact:
            return json.dumps(dict_data, indent=indent, separators=(",", ":"))

        return json.dumps(dict_data, indent=indent)

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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Joseph Black"
                self.discovery_year = 1755

            case "aluminium" | "aluminum" | "al" | 13:
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
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
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Humphry Davy"
                self.discovery_year = 1808

            case "scandium" | "sc" | 21:
                self.name = "scandium"
                self.symbol = "Sc"
                self.atomic_number = 21
                self.atomic_mass = 44.956
                self.electrons_per_shell = (2, 8, 9, 2)
                self.state = "solid"
                self.group = 3
                self.period = 4
                self.melting_point_k = 1814
                self.boiling_point_k = 3109
                self.density = 2.985
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Lars Fredrik Nilson"
                self.discovery_year = 1879
            
            case "titanium" | "ti" | 22:
                self.name = "titanium"
                self.symbol = "Ti"
                self.atomic_number = 22
                self.atomic_mass = 47.867
                self.electrons_per_shell = (2, 8, 10, 2)
                self.state = "solid"
                self.group = 4
                self.period = 4
                self.melting_point_k = 1941
                self.boiling_point_k = 3560
                self.density = 4.506
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "William Gregor"
                self.discovery_year = 1791

            case "vanadium" | "v" | 23:
                self.name = "vanadium"
                self.symbol = "V"
                self.atomic_number = 23
                self.atomic_mass = 50.942
                self.electrons_per_shell = (2, 8, 11, 2)
                self.state = "solid"
                self.group = 5
                self.period = 4
                self.melting_point_k = 2183
                self.boiling_point_k = 3680
                self.density = 6.11
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Nils Gabriel Sefström"
                self.discovery_year = 1830

            case "chromium" | "cr" | 24:
                self.name = "chromium"
                self.symbol = "Cr"
                self.atomic_number = 24
                self.atomic_mass = 51.996
                self.electrons_per_shell = (2, 8, 13, 1)
                self.state = "solid"
                self.group = 6
                self.period = 4
                self.melting_point_k = 2180
                self.boiling_point_k = 2944
                self.density = 7.15
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Louis Nicolas Vauquelin"
                self.discovery_year = 1794
            
            case "manganese" | "mn" | 25:
                self.name = "manganese"
                self.symbol = "Mn"
                self.atomic_number = 25
                self.atomic_mass = 54.938
                self.electrons_per_shell = (2, 8, 13, 2)
                self.state = "solid"
                self.group = 7
                self.period = 4
                self.melting_point_k = 1519
                self.boiling_point_k = 2334
                self.density = 7.21
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Carl Wilhelm Scheele"
                self.discovery_year = 1774

            case "iron" | "fe" | 26:
                self.name = "iron"
                self.symbol = "Fe"
                self.atomic_number = 26
                self.atomic_mass = 55.845
                self.electrons_per_shell = (2, 8, 14, 2)
                self.state = "solid"
                self.group = 8
                self.period = 4
                self.melting_point_k = 1811
                self.boiling_point_k = 3134
                self.density = 7.874
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = None
                self.discovery_year = None
            
            case "cobalt" | "co" | 27:
                self.name = "cobalt"
                self.symbol = "Co"
                self.atomic_number = 27
                self.atomic_mass = 58.933
                self.electrons_per_shell = (2, 8, 15, 2)
                self.state = "solid"
                self.group = 9
                self.period = 4
                self.melting_point_k = 1768
                self.boiling_point_k = 3200
                self.density = 8.9
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Georg Brandt"
                self.discovery_year = 1735

            case "nickel" | "ni" | 28:
                self.name = "nickel"
                self.symbol = "Ni"
                self.atomic_number = 28
                self.atomic_mass = 58.693
                self.electrons_per_shell = (2, 8, 16, 2)
                self.state = "solid"
                self.group = 10
                self.period = 4
                self.melting_point_k = 1728
                self.boiling_point_k = 3003
                self.density = 8.908
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Axel Fredrik Cronstedt"
                self.discovery_year = 1751
            
            case "copper" | "cu" | 29:
                self.name = "copper"
                self.symbol = "Cu"
                self.atomic_number = 29
                self.atomic_mass = 63.546
                self.electrons_per_shell = (2, 8, 18, 1)
                self.state = "solid"
                self.group = 11
                self.period = 4
                self.melting_point_k = 1357.77
                self.boiling_point_k = 2835
                self.density = 8.96
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Middle East"
                self.discovery_year = -9000
            
            case "zinc" | "zn" | 30:
                self.name = "zinc"
                self.symbol = "Zn"
                self.atomic_number = 30
                self.atomic_mass = 65.38
                self.electrons_per_shell = (2, 8, 18, 2)
                self.state = "solid"
                self.group = 12
                self.period = 4
                self.melting_point_k = 692.68
                self.boiling_point_k = 1180
                self.density = 7.14
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Andreas Sigismund Marggraf"
                self.discovery_year = 1746

            case "gallium" | "ga" | 31:
                self.name = "gallium"
                self.symbol = "Ga"
                self.atomic_number = 31
                self.atomic_mass = 69.723
                self.electrons_per_shell = (2, 8, 18, 3)
                self.state = "solid"
                self.group = 13
                self.period = 4
                self.melting_point_k = 302.9146
                self.boiling_point_k = 2673
                self.density = 5.91
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Lecoq de Boisbaudran"
                self.discovery_year = 1875

            case "germanium" | "ge" | 32:
                self.name = "germanium"
                self.symbol = "Ge"
                self.atomic_number = 32
                self.atomic_mass = 72.63
                self.electrons_per_shell = (2, 8, 18, 4)
                self.state = "solid"
                self.group = 14
                self.period = 4
                self.melting_point_k = 1211.4
                self.boiling_point_k = 3106
                self.density = 5.323
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Clemens Winkler"
                self.discovery_year = 1886

            case "arsenic" | "as" | 33:
                self.name = "arsenic"
                self.symbol = "As"
                self.atomic_number = 33
                self.atomic_mass = 74.922
                self.electrons_per_shell = (2, 8, 18, 5)
                self.state = "solid"
                self.group = 15
                self.period = 4
                self.melting_point_k = 1090
                self.boiling_point_k = 887
                self.density = 5.727
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Albertus Magnus"
                self.discovery_year = 1250
            
            case "selenium" | "se" | 34:
                self.name = "selenium"
                self.symbol = "Se"
                self.atomic_number = 34
                self.atomic_mass = 78.971
                self.electrons_per_shell = (2, 8, 18, 6)
                self.state = "solid"
                self.group = 16
                self.period = 4
                self.melting_point_k = 494
                self.boiling_point_k = 958
                self.density = 4.81
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Jöns Jakob Berzelius"
                self.discovery_year = 1817
            
            case "bromine" | "br" | 35:
                self.name = "bromine"
                self.symbol = "Br"
                self.atomic_number = 35
                self.atomic_mass = 79.904
                self.electrons_per_shell = (2, 8, 18, 7)
                self.state = "liquid"
                self.group = 17
                self.period = 4
                self.melting_point_k = 265.8
                self.boiling_point_k = 332
                self.density = 3.1028
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Antoine Jérôme Balard"
                self.discovery_year = 1825
            
            case "krypton" | "kr" | 36:
                self.name = "krypton"
                self.symbol = "Kr"
                self.atomic_number = 36
                self.atomic_mass = 83.798
                self.electrons_per_shell = (2, 8, 18, 8)
                self.state = "gas"
                self.group = 18
                self.period = 4
                self.melting_point_k = 115.78
                self.boiling_point_k = 119.93
                self.density = 0.003749
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "William Ramsay, Morris Travers"
                self.discovery_year = 1898
            
            case "rubidium" | "rb" | 37:
                self.name = "rubidium"
                self.symbol = "Rb"
                self.atomic_number = 37
                self.atomic_mass = 85.468
                self.electrons_per_shell = (2, 8, 18, 8, 1)
                self.state = "solid"
                self.group = 1
                self.period = 5
                self.melting_point_k = 312.45
                self.boiling_point_k = 961
                self.density = 1.532
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Robert Bunsen, Gustav Kirchhoff"
                self.discovery_year = 1861
            
            case "strontium" | "sr" | 38:
                self.name = "strontium"
                self.symbol =  "Sr"
                self.atomic_number = 38
                self.atomic_mass = 87.62
                self.electrons_per_shell = (2, 8, 18, 8, 2)
                self.state = "solid"
                self.group = 2
                self.period = 5
                self.melting_point_k = 1050
                self.boiling_point_k = 1650
                self.density = 2.64
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "William Cruickshank"
                self.discovery_year = 1787

            case "yttrium" | "y" | 39:
                self.name = "yttrium"
                self.symbol = "Y"
                self.atomic_number = 39
                self.atomic_mass = 88.906
                self.electrons_per_shell = (2, 8, 18, 9, 2)
                self.state = "solid"
                self.group = 3
                self.period = 5
                self.melting_point_k = 1799
                self.boiling_point_k = 3203
                self.density = 4.472
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Johan Gadolin"
                self.discovery_year = 1794

            case "zirconium" | "zr" | 40:
                self.name = "zirconium"
                self.symbol = "Zr"
                self.atomic_number = 40
                self.atomic_mass = 91.224
                self.electrons_per_shell = (2, 8, 18, 10, 2)
                self.state = "solid"
                self.group = 4
                self.period = 5
                self.melting_point_k = 2125
                self.boiling_point_k = 4650
                self.density = 6.52
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Martin Heinrich Klaproth"
                self.discovery_year = 1789
            
            case "niobium" | "nb" | 41:
                self.name = "niobium"
                self.symbol = "Nb"
                self.atomic_number = 41
                self.atomic_mass = 92.906
                self.electrons_per_shell = (2, 8, 18, 12, 1)
                self.state = "solid"
                self.group = 5
                self.period = 5
                self.melting_point_k = 2750
                self.boiling_point_k = 5017
                self.density = 8.57
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Charles Hatchett"
                self.discovery_year = 1801
            
            case "molybdenum" | "mo" | 42:
                self.name = "molybdenum"
                self.symbol = "Mo"
                self.atomic_number = 42
                self.atomic_mass = 95.95
                self.electrons_per_shell = (2, 8, 18, 13, 1)
                self.state = "solid"
                self.group = 6
                self.period = 5
                self.melting_point_k = 2896
                self.boiling_point_k = 4912
                self.density = 10.28
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Carl Wilhelm Scheele"
                self.discovery_year = 1778
            
            case "technetium" | "tc" | 43:
                self.name = "technetium"
                self.symbol = "Tc"
                self.atomic_number = 43
                self.atomic_mass = 98
                self.electrons_per_shell = (2, 8, 18, 13, 2)
                self.state = "solid"
                self.group = 7
                self.period = 5
                self.melting_point_k = 2430
                self.boiling_point_k = 4538
                self.density = 11
                self.natural = True # extremely trace amounts from decay.
                self.has_stable_isotope = False
                self.discovery = "Emilio Segrè, Carlo Perrier"
                self.discovery_year = 1937
            
            case "ruthenium" | "ru" | 44:
                self.name = "ruthenium"
                self.symbol = "Ru"
                self.atomic_number = 44
                self.atomic_mass = 101.07
                self.electrons_per_shell = (2, 8, 18, 15, 1)
                self.state = "solid"
                self.group = 8
                self.period = 5
                self.melting_point_k = 2607
                self.boiling_point_k = 4423
                self.density = 12.45
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Karl Ernst Claus"
                self.discovery_year = 1844
            
            case "rhodium" | "rh" | 45:
                self.name = "rhodium"
                self.symbol = "Rh"
                self.atomic_number = 45
                self.atomic_mass = 102.91
                self.electrons_per_shell = (2, 8, 18, 16, 1)
                self.state = "solid"
                self.group = 9
                self.period = 5
                self.melting_point_k = 2237
                self.boiling_point_k = 3968
                self.density = 12.41
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "William Hyde Wollaston"
                self.discovery_year = 1804

            case "palladium" | "pd" | 46:
                self.name = "palladium"
                self.symbol = "Pd"
                self.atomic_number = 46
                self.atomic_mass = 106.42
                self.electrons_per_shell = (2, 8, 18, 18)
                self.state = "solid"
                self.group = 10
                self.period = 5
                self.melting_point_k = 1828.05
                self.boiling_point_k = 3236
                self.density = 12.023
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "William Hyde Wollaston"
                self.discovery_year = 1802

            case "silver" | "ag" | 47:
                self.name = "silver"
                self.symbol = "Ag"
                self.atomic_number = 47
                self.atomic_mass = 107.87
                self.electrons_per_shell = (2, 8, 18, 18, 1)
                self.state = "solid"
                self.group = 11
                self.period = 5
                self.melting_point_k = 1234.93
                self.boiling_point_k = 2435
                self.density = 10.49
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = None
                self.discovery_year = None

            case "cadmium" | "cd" | 48:
                self.name = "cadmium"
                self.symbol = "Cd"
                self.atomic_number = 48
                self.atomic_mass = 112.41
                self.electrons_per_shell = (2, 8, 18, 18, 2)
                self.state = "solid"
                self.group = 12
                self.period = 5
                self.melting_point_k = 594.22
                self.boiling_point_k = 1040
                self.density = 8.65
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = (
                    "Karl Samuel Leberecht Hermann, Friedrich Stromeyer")
                self.discovery_year = 1817
            
            case "indium" | "in" | 49:
                self.name = "indium"
                self.symbol = "In"
                self.atomic_number = 49
                self.atomic_mass = 114.82
                self.electrons_per_shell = (2, 8, 18, 18, 3)
                self.state = "solid"
                self.group = 13
                self.period = 5
                self.melting_point_k = 429.7485
                self.boiling_point_k = 2345
                self.density = 7.31
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = (
                    "Ferdinand Reich, Hieronymous Theodor Richter")
                self.discovery_year = 1863
            
            case "tin" | "sn" | 50:
                self.name = "tin"
                self.symbol = "Sn"
                self.atomic_number = 50
                self.atomic_mass = 118.71
                self.electrons_per_shell = (2, 8, 18, 18, 4)
                self.state = "solid"
                self.group = 14
                self.period = 5
                self.melting_point_k = 505.08
                self.boiling_point_k = 2875
                self.density = 7.265
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = None
                self.discovery_year = None

            case "antimony" | "sb" | 51:
                self.name = "antimony"
                self.symbol = "Sb"
                self.atomic_number = 51
                self.atomic_mass = 121.76
                self.electrons_per_shell = (2, 8, 18, 18, 5)
                self.state = "solid"
                self.group = 15
                self.period = 5
                self.melting_point_k = 903.78
                self.boiling_point_k = 1908
                self.density = 6.697
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = None
                self.discovery_year = None
            
            case "tellurium" | "te" | 52:
                self.name = "tellurium"
                self.symbol = "Te"
                self.atomic_number = 52
                self.atomic_mass = 127.6
                self.electrons_per_shell = (2, 8, 18, 18, 6)
                self.state = "solid"
                self.group = 16
                self.period = 5
                self.melting_point_k = 722.66
                self.boiling_point_k = 1261
                self.density = 6.24
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Franz-Joseph Müller von Reichenstein"
                self.discovery_year = 1782
            
            case "iodine" | "i" | 53:
                self.name = "iodine"
                self.symbol = "I"
                self.atomic_number = 53
                self.atomic_mass = 126.9
                self.electrons_per_shell = (2, 8, 18, 18, 7)
                self.state = "solid"
                self.group = 17
                self.period = 5
                self.melting_point_k = 386.85
                self.boiling_point_k = 457.4
                self.density = 4.933
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Bernard Courtois"
                self.discovery_year = 1811

            case "xenon" | "xe" | 54:
                self.name = "xenon"
                self.symbol = "Xe"
                self.atomic_number = 54
                self.atomic_mass = 131.29
                self.electrons_per_shell = (2, 8, 18, 18, 8)
                self.state = "gas"
                self.group = 18
                self.period = 5
                self.melting_point_k = 161.4
                self.boiling_point_k = 165.051
                self.density = 0.005894
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "William Ramsay, Morris Travers"
                self.discovery_year = 1898
            
            case "caesium" | "cesium" | "cs" | 55:
                self.name = "caesium"
                self.symbol = "Cs"
                self.atomic_number = 55
                self.atomic_mass = 132.91
                self.electrons_per_shell = (2, 8, 18, 18, 8, 1)
                self.state = "solid"
                self.group = 1
                self.period = 6
                self.melting_point_k = 301.7
                self.boiling_point_k = 944
                self.density = 1.93
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Robert Bunsen, Gustav Kirchhoff"
                self.discovery_year = 1860
            
            case "barium" | "ba" | 56:
                self.name = "barium"
                self.symbol = "Ba"
                self.atomic_number = 56
                self.atomic_mass = 137.33
                self.electrons_per_shell = (2, 8, 18, 18, 8, 2)
                self.state = "solid"
                self.group = 2
                self.period = 6
                self.melting_point_k = 1000
                self.boiling_point_k = 2118
                self.density = 3.51
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Carl Wilhelm Scheele"
                self.discovery_year = 1772
            
            case "lanthanum" | "la" | 57:
                self.name = "lanthanum"
                self.symbol = "La"
                self.atomic_number = 57
                self.atomic_mass = 138.91
                self.electrons_per_shell = (2, 8, 18, 18, 9, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1193
                self.boiling_point_k = 3737
                self.density = 6.162
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Carl Gustaf Mosander"
                self.discovery_year = 1838

            case "cerium" | "ce" | 58:
                self.name = "cerium"
                self.symbol = "Ce"
                self.atomic_number = 58
                self.atomic_mass = 140.12
                self.electrons_per_shell = (2, 8, 18, 19, 9, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1068
                self.boiling_point_k = 3716
                self.density = 6.77
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = (
                    "Martin Heinrich Klaproth, Jöns Jakob Berzelius, "
                    "Wilhelm Hisinger")
                self.discovery_year = 1803
            
            case "praseodymium" | "pr" | 59:
                self.name = "praseodymium"
                self.symbol = "Pr"
                self.atomic_number = 59
                self.atomic_mass = 140.91
                self.electrons_per_shell = (2, 8, 18, 21, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1208
                self.boiling_point_k = 3403
                self.density = 6.77
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Carl Auer von Welsbach"
                self.discovery_year = 1885

            case "neodymium" | "nd" | 60:
                self.name = "neodymium"
                self.symbol = "Nd"
                self.atomic_number = 60
                self.atomic_mass = 144.24
                self.electrons_per_shell = (2, 8, 18, 22, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1297
                self.boiling_point_k = 3347
                self.density = 7.01
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Carl Auer von Welsbach"
                self.discovery_year = 1885

            case "promethium" | "pm" | 61: 
                self.name = "promethium"
                self.symbol = "Pm"
                self.atomic_number = 61
                self.atomic_mass = 145
                self.electrons_per_shell = (2, 8, 18, 23, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1315
                self.boiling_point_k = 3273
                self.density = 7.26
                self.natural = True # extremely trace amounts from decay.
                self.has_stable_isotope = False
                self.discovery = (
                    "Charles D. Coryell, Jacob A. Marinsky, "
                    "Lawrence E. Glendenin")
                self.discovery_year = 1945

            case "samarium" | "sm" | 62:
                self.name = "samarium"
                self.symbol = "Sm"
                self.atomic_number = 62
                self.atomic_mass = 150.36
                self.electrons_per_shell = (2, 8, 18, 24, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1345
                self.boiling_point_k = 2173
                self.density = 7.52
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Lecoq de Boisbaudran"
                self.discovery_year = 1879

            case "europium" | "eu" | 63:
                self.name = "europium"
                self.symbol = "Eu"
                self.atomic_number = 63
                self.atomic_mass = 151.96
                self.electrons_per_shell = (2, 8, 18, 25, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1099
                self.boiling_point_k = 1802
                self.density = 5.244
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Eugène-Anatole Demarçay"
                self.discovery_year = 1896
            
            case "gadolinium" | "gd" | 64:
                self.name = "gadolinium"
                self.symbol = "Gd"
                self.atomic_number = 64
                self.atomic_mass = 157.25
                self.electrons_per_shell = (2, 8, 18, 25, 9, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1585
                self.boiling_point_k = 3273
                self.density = 7.9
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Jean Charles Galissard de Marignac"
                self.discovery_year = 1880
            
            case "terbium" | "tb" | 65:
                self.name = "terbium"
                self.symbol = "Tb"
                self.atomic_number = 65
                self.atomic_mass = 158.93
                self.electrons_per_shell = (2, 8, 18, 27, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1629
                self.boiling_point_k = 3396
                self.density = 8.23
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Carl Gustaf Mosander"
                self.discovery_year = 1843
            
            case "dysprosium" | "dy" | 66:
                self.name = "dysprosium"
                self.symbol = "Dy"
                self.atomic_number = 66
                self.atomic_mass = 162.5
                self.electrons_per_shell = (2, 8, 18, 28, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1680
                self.boiling_point_k = 2840
                self.density = 8.54
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Lecoq de Boisbaudran"
                self.discovery_year = 1886

            case "holmium" | "ho" | 67:
                self.name = "holmium"
                self.symbol = "Ho"
                self.atomic_number = 67
                self.atomic_mass = 164.93
                self.electrons_per_shell = (2, 8, 18, 29, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1734
                self.boiling_point_k = 2873
                self.density = 8.79
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = (
                    "Jacques-Louis Soret, Marc Delafontaine, "
                    "Per Teodor Cleve")
                self.discovery_year = 1878
            
            case "erbium" | "er" | 68:
                self.name = "erbium"
                self.symbol = "Er"
                self.atomic_number = 68
                self.atomic_mass = 167.26
                self.electrons_per_shell = (2, 8, 18, 30, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1802
                self.boiling_point_k = 3141
                self.density = 9.066
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Carl Gustaf Mosander"
                self.discovery_year = 1843

            case "thulium" | "tm" | 69:
                self.name = "thulium"
                self.symbol = "Tm"
                self.atomic_number = 69
                self.atomic_mass = 168.93
                self.electrons_per_shell = (2, 8, 18, 31, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1818
                self.boiling_point_k = 2223
                self.density = 9.32
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Per Teodor Cleve"
                self.discovery_year = 1879

            case "ytterbium" | "yb" | 70:
                self.name = "ytterbium"
                self.symbol = "Yb"
                self.atomic_number = 70
                self.atomic_mass = 173.05
                self.electrons_per_shell = (2, 8, 18, 32, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 6
                self.melting_point_k = 1097
                self.boiling_point_k = 1469
                self.density = 6.9
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Jean Charles Galissard de Marignac"
                self.discovery_year = 1878
            
            case "lutetium" | "lu" | 71:
                self.name = "lutetium"
                self.symbol = "Lu"
                self.atomic_number = 71
                self.atomic_mass = 174.97
                self.electrons_per_shell = (2, 8, 18, 32, 9, 2)
                self.state = "solid"
                self.group = 3
                self.period = 6
                self.melting_point_k = 1925
                self.boiling_point_k = 3675
                self.density = 9.841
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Carl Auer von Welsbach, Georges Urbain"
                self.discovery_year = 1906
            
            case "hafnium" | "hf" | 72:
                self.name = "hafnium"
                self.symbol = "Hf"
                self.atomic_number = 72
                self.atomic_mass = 178.49
                self.electrons_per_shell = (2, 8, 18, 32, 10, 2)
                self.state = "solid"
                self.group = 4
                self.period = 6
                self.melting_point_k = 2506
                self.boiling_point_k = 4876
                self.density = 13.31
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Dirk Coster, George de Hevesy"
                self.discovery_year = 1922
            
            case "tantalum" | "ta" | 73:
                self.name = "tantalum"
                self.symbol = "Ta"
                self.atomic_number = 73
                self.atomic_mass = 180.95
                self.electrons_per_shell = (2, 8, 18, 32, 11, 2)
                self.state = "solid"
                self.group = 5
                self.period = 6
                self.melting_point_k = 3290
                self.boiling_point_k = 5731
                self.density = 16.69
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Anders Gustaf Ekeberg"
                self.discovery_year = 1802
            
            case "tungsten" | "w" | 74:
                self.name = "tungsten"
                self.symbol = "W"
                self.atomic_number = 74
                self.atomic_mass = 183.84
                self.electrons_per_shell = (2, 8, 18, 32, 12, 2)
                self.state = "solid"
                self.group = 6
                self.period = 6
                self.melting_point_k = 3695
                self.boiling_point_k = 6203
                self.density = 19.25
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Juan José Elhuyar, Fausto Elhuyar"
                self.discovery_year = 1783
            
            case "rhenium" | "re" | 75:
                self.name = "rhenium"
                self.symbol = "Re"
                self.atomic_number = 75
                self.atomic_mass = 186.21
                self.electrons_per_shell = (2, 8, 18, 32, 13, 2)
                self.state = "solid"
                self.group = 7
                self.period = 6
                self.melting_point_k = 3459
                self.boiling_point_k = 5903
                self.density = 21.02
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Walter Noddack, Ida Noddack, Otto Berg"
                self.discovery_year = 1925
            
            case "osmium" | "os" | 76:
                self.name = "osmium"
                self.symbol = "Os"
                self.atomic_number = 76
                self.atomic_mass = 190.23
                self.electrons_per_shell = (2, 8, 18, 32, 14, 2)
                self.state = "solid"
                self.group = 8
                self.period = 6
                self.melting_point_k = 3306
                self.boiling_point_k = 5285
                self.density = 22.59
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Smithson Tennant"
                self.discovery_year = 1803
            
            case "iridium" | "ir" | 77:
                self.name = "iridium"
                self.symbol = "Ir"
                self.atomic_number = 77
                self.atomic_mass = 192.22
                self.electrons_per_shell = (2, 8, 18, 32, 15, 2)
                self.state = "solid"
                self.group = 9
                self.period = 6
                self.melting_point_k = 2719
                self.boiling_point_k = 4403
                self.density = 22.56
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Smithson Tennant"
                self.discovery_year = 1803

            case "platinum" | "pt" | 78:
                self.name = "platinum"
                self.symbol = "Pt"
                self.atomic_number = 78
                self.atomic_mass = 195.08
                self.electrons_per_shell = (2, 8, 18, 32, 17, 1)
                self.state = "solid"
                self.group = 10
                self.period = 6
                self.melting_point_k = 2041.4
                self.boiling_point_k = 4098
                self.density = 21.45
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Antonio de Ulloa"
                self.discovery_year = 1735
            
            case "gold" | "au" | 79:
                self.name = "gold"
                self.symbol = "Au"
                self.atomic_number = 79
                self.atomic_mass = 196.97
                self.electrons_per_shell = (2, 8, 18, 32, 18, 1)
                self.state = "solid"
                self.group = 11
                self.period = 6
                self.melting_point_k = 1337.33
                self.boiling_point_k = 3243
                self.density = 19.3
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Middle East"
                self.discovery_year = None
            
            case "mercury" | "hg" | 80:
                self.name = "mercury"
                self.symbol = "Hg"
                self.atomic_number = 80
                self.atomic_mass = 200.59
                self.electrons_per_shell = (2, 8, 18, 32, 18, 2)
                self.state = "liquid"
                self.group = 12
                self.period = 6
                self.melting_point_k = 234.321
                self.boiling_point_k = 629.88
                self.density = 13.534
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = None
                self.discovery_year = None
            
            case "thallium" | "tl" | 81:
                self.name = "thallium"
                self.symbol = "Tl"
                self.atomic_number = 81
                self.atomic_mass = 204.38
                self.electrons_per_shell = (2, 8, 18, 32, 18, 3)
                self.state = "solid"
                self.group = 13
                self.period = 6
                self.melting_point_k = 577
                self.boiling_point_k = 1746
                self.density = 11.85
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "William Crookes"
                self.discovery_year = 1861
            
            case "lead" | "pb" | 82:
                self.name = "lead"
                self.symbol = "Pb"
                self.atomic_number = 82
                self.atomic_mass = 207.2
                self.electrons_per_shell = (2, 8, 18, 32, 18, 4)
                self.state = "solid"
                self.group = 14
                self.period = 6
                self.melting_point_k = 600.61
                self.boiling_point_k = 2022
                self.density = 11.34
                self.natural = True
                self.has_stable_isotope = True
                self.discovery = "Middle East"
                self.discovery_year = None

            case "bismuth" | "bi" | 83:
                self.name = "bismuth"
                self.symbol = "Bi"
                self.atomic_number = 83
                self.atomic_mass = 208.98
                self.electrons_per_shell = (2, 8, 18, 32, 18, 5)
                self.state = "solid"
                self.group = 15
                self.period = 6
                self.melting_point_k = 544.7
                self.boiling_point_k = 1837
                self.density = 9.78
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Claude François Geoffroy"
                self.discovery_year = 1753
            
            case "polonium" | "po" | 84:
                self.name = "polonium"
                self.symbol = "Po"
                self.atomic_number = 84
                self.atomic_mass = 209
                self.electrons_per_shell = (2, 8, 18, 32, 18, 6)
                self.state = "solid"
                self.group = 16
                self.period = 6
                self.melting_point_k = 527
                self.boiling_point_k = 1235
                self.density = 9.196
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Marie Curie, Pierre Curie"
                self.discovery_year = 1898
            
            case "astatine" | "at" | 85:
                self.name = "astatine"
                self.symbol = "At"
                self.atomic_number = 85
                self.atomic_mass = 210
                self.electrons_per_shell = (2, 8, 18, 32, 18, 7)
                self.state = None
                self.group = 17
                self.period = 6
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = (
                    "Dale R. Corson, Kenneth R. Mackenzie, "
                    "Emilio Segre")
                self.discovery_year = 1940
            
            case "radon" | "rn" | 86:
                self.name = "radon"
                self.symbol = "Rn"
                self.atomic_number = 86
                self.atomic_mass = 222
                self.electrons_per_shell = (2, 8, 18, 32, 18, 8)
                self.state = "gas"
                self.group = 18
                self.period = 6
                self.melting_point_k = 202
                self.boiling_point_k = 211.5
                self.density = 0.00973
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Ernest Rutherford, Robert B. Owens"
                self.discovery_year = 1899
            
            case "francium" | "fr" | 87:
                self.name = "francium"
                self.symbol = "Fr"
                self.atomic_number = 87
                self.atomic_mass = 223
                self.electrons_per_shell = (2, 8, 18, 32, 18, 8, 1)
                self.state = "solid"
                self.group = 1
                self.period = 7
                self.melting_point_k = 300
                self.boiling_point_k = 950
                self.density = None
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Marguerite Perey"
                self.discovery_year = 1939
            
            case "radium" | "ra" | 88:
                self.name = "radium"
                self.symbol = "Ra"
                self.atomic_number = 88
                self.atomic_mass = 226
                self.electrons_per_shell = (2, 8, 18, 32, 18, 8, 2)
                self.state = "solid"
                self.group = 2
                self.period = 7
                self.melting_point_k = 973
                self.boiling_point_k = 2010
                self.density = 5.5
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Marie Curie, Pierre Curie"
                self.discovery_year = 1898
            
            case "actinium" | "ac" | 89:
                self.name = "actinium"
                self.symbol = "Ac"
                self.atomic_number = 89
                self.atomic_mass = 227
                self.electrons_per_shell = (2, 8, 18, 32, 18, 9, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1323
                self.boiling_point_k = 3473
                self.density = 10
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Friedrich Oskar Giesel"
                self.discovery_year = 1902
            
            case "thorium" | "th" | 90:
                self.name = "thorium"
                self.symbol = "Th"
                self.atomic_number = 90
                self.atomic_mass = 232.04
                self.electrons_per_shell = (2, 8, 18, 32, 18, 10, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 2023
                self.boiling_point_k = 5061
                self.density = 11.7
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Jöns Jakob Berzelius"
                self.discovery_year = 1829
            
            case "protactinium" | "pa" | 91:
                self.name = "protactinium"
                self.symbol = "Pa"
                self.atomic_number = 91
                self.atomic_mass = 231.04
                self.electrons_per_shell = (2, 8, 18, 32, 20, 9, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1841
                self.boiling_point_k = 4300
                self.density = 15.37
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Kasimir Fajans, Oswald Helmuth Göhring"
                self.discovery_year = 1913
            
            case "uranium" | "u" | 92:
                self.name = "uranium"
                self.symbol = "U"
                self.atomic_number = 92
                self.atomic_mass = 238.03
                self.electrons_per_shell = (2, 8, 18, 32, 21, 9, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1405.3
                self.boiling_point_k = 4404
                self.density = 19.1
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Martin Heinrich Klaproth"
                self.discovery_year = 1789
            
            case "neptunium" | "np" | 93:
                self.name = "neptunium"
                self.symbol = "Np"
                self.atomic_number = 93
                self.atomic_mass = 237
                self.electrons_per_shell = (2, 8, 18, 32, 22, 9, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 912
                self.boiling_point_k = None
                self.density = 20.45
                self.natural = True
                self.has_stable_isotope = False
                self.discovery = "Edwin McMillan, Philip H. Abelson"
                self.discovery_year = 1940
            
            case "plutonium" | "pu" | 94:
                self.name = "plutonium"
                self.symbol = "Pu"
                self.atomic_number = 94
                self.atomic_mass = 244
                self.electrons_per_shell = (2, 8, 18, 32, 24, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 912.5
                self.boiling_point_k = 3505
                self.density = 19.85
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Glenn T. Seaborg, Arthur Wahl, Joseph W. Kennedy, "
                    "Edwin McMillan")
                self.discovery_year = 1940

            case "americium" | "am" | 95:
                self.name = "americium"
                self.symbol = "Am"
                self.atomic_number = 95
                self.atomic_mass = 243
                self.electrons_per_shell = (2, 8, 18, 32, 25, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1449
                self.boiling_point_k = None
                self.density = 12
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Glenn T. Seaborg, Ralph A. James, Leon O. Morgan, "
                    "Albert Ghiorso")
                self.discovery_year = 1944
            
            case "curium" | "cm" | 96:
                self.name = "curium"
                self.symbol = "Cm"
                self.atomic_number = 96
                self.atomic_mass = 247
                self.electrons_per_shell = (2, 8, 18, 32, 25, 9, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1613
                self.boiling_point_k = 3383
                self.density = 13.51
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Glenn T. Seaborg, Ralph A. James, Albert Ghiorso")
                self.discovery_year = 1944
            
            case "berkelium" | "bk" | 97:
                self.name = "berkelium"
                self.symbol = "Bk"
                self.atomic_number = 97
                self.atomic_mass = 247
                self.electrons_per_shell = (2, 8, 18, 32, 27, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1259
                self.boiling_point_k = None
                self.density = 14.78
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Lawrence Berkeley National Laboratory"
                self.discovery_year = 1949
            
            case "californium" | "cf" | 98:
                self.name = "californium"
                self.symbol = "Cf"
                self.atomic_number = 98
                self.atomic_mass = 251
                self.electrons_per_shell = (2, 8, 18, 32, 28, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1173
                self.boiling_point_k = None
                self.density = 15.1
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Lawrence Berkeley National Laboratory"
                self.discovery_year = 1950
            
            case "einsteinium" | "es" | 99:
                self.name = "einsteinium"
                self.symbol = "Es"
                self.atomic_number = 99
                self.atomic_mass = 252
                self.electrons_per_shell = (2, 8, 18, 32, 29, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1133
                self.boiling_point_k = None
                self.density = 8.84
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Lawrence Berkeley National Laboratory"
                self.discovery_year = 1952
            
            case "fermium" | "fm" | 100:
                self.name = "fermium"
                self.symbol = "Fm"
                self.atomic_number = 100
                self.atomic_mass = 257
                self.electrons_per_shell = (2, 8, 18, 32, 30, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1800
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Lawrence Berkeley National Laboratory"
                self.discovery_year = 1952
            
            case "mendelevium" | "md" | 101:
                self.name = "mendelevium"
                self.symbol = "Md"
                self.atomic_number = 101
                self.atomic_mass = 258
                self.electrons_per_shell = (2, 8, 18, 32, 31, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1100
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Lawrence Berkeley National Laboratory"
                self.discovery_year = 1955
            
            case "nobelium" | "no" | 102:
                self.name = "nobelium"
                self.symbol = "No"
                self.atomic_number = 102
                self.atomic_mass = 259
                self.electrons_per_shell = (2, 8, 18, 32, 32, 8, 2)
                self.state = "solid"
                self.group = None
                self.period = 7
                self.melting_point_k = 1100
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Joint Institute for Nuclear Research"
                self.discovery_year = 1966
            
            case "lawrencium" | "lr" | 103:
                self.name = "lawrencium"
                self.symbol = "Lr"
                self.atomic_number = 103
                self.atomic_mass = 266
                self.electrons_per_shell = (2, 8, 18, 32, 32, 8, 3)
                self.state = "solid"
                self.group = 3
                self.period = 7
                self.melting_point_k = 1900
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Lawrence Berkeley National Laboratory, "
                    "Joint Institute for Nuclear Research")
                self.discovery_year = 1961
            
            case "rutherfordium" | "rf" | 104:
                self.name = "rutherfordium"
                self.symbol = "Rf"
                self.atomic_number = 104
                self.atomic_mass = 267
                self.electrons_per_shell = (2, 8, 18, 32, 32, 10, 2)
                self.state = "solid"
                self.group = 4
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Joint Institute for Nuclear Research"
                self.discovery_year = 1964
            
            case "dubnium" | "db" | 105:
                self.name = "dubnium"
                self.symbol = "Db"
                self.atomic_number = 105
                self.atomic_mass = 268
                self.electrons_per_shell = (2, 8, 18, 32, 32, 11, 2)
                self.state = "solid"
                self.group = 5
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Lawrence Berkeley National Laboratory, "
                    "Joint Institute for Nuclear Research")
                self.discovery_year = 1970
            
            case "seaborgium" | "sg" | 106:
                self.name = "seaborgium"
                self.symbol = "Sg"
                self.atomic_number = 106
                self.atomic_mass = 269
                self.electrons_per_shell = (2, 8, 18, 32, 32, 12, 2)
                self.state = "solid"
                self.group = 6
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Lawrence Berkeley National Laboratory"
                self.discovery_year = 1974
            
            case "bohrium" | "bh" | 107:
                self.name = "bohrium"
                self.symbol = "Bh"
                self.atomic_number = 107
                self.atomic_mass = 270
                self.electrons_per_shell = (2, 8, 18, 32, 32, 13, 2)
                self.state = "solid"
                self.group = 7
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Gesellschaft für Schwerionenforschung"
                self.discovery_year = 1981
            
            case "hassium" | "hs" | 108:
                self.name = "hassium"
                self.symbol = "Hs"
                self.atomic_number = 108
                self.atomic_mass = 269
                self.electrons_per_shell = (2, 8, 18, 32, 32, 14, 2)
                self.state = "solid"
                self.group = 8
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Gesellschaft für Schwerionenforschung"
                self.discovery_year = 1984

            case "meitnerium" | "mt" | 109:
                self.name = "meitnerium"
                self.symbol = "Mt"
                self.atomic_number = 109
                self.atomic_mass = 278
                self.electrons_per_shell = (2, 8, 18, 32, 32, 15, 2)
                self.state = "solid"
                self.group = 9
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Gesellschaft für Schwerionenforschung"
                self.discovery_year = 1982

            case "darmstadtium" | "ds" | 110:
                self.name = "darmstadtium"
                self.symbol = "Ds"
                self.atomic_number = 110
                self.atomic_mass = 281
                self.electrons_per_shell = (2, 8, 18, 32, 32, 16, 2)
                self.state = "solid"
                self.group = 10
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Gesellschaft für Schwerionenforschung"
                self.discovery_year = 1994
            
            case "roentgenium" | "rg" | 111:
                self.name = "roentgenium"
                self.symbol = "Rg"
                self.atomic_number = 111
                self.atomic_mass = 282
                self.electrons_per_shell = (2, 8, 18, 32, 32, 17, 2)
                self.state = "solid"
                self.group = 11
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Gesellschaft für Schwerionenforschung"
                self.discovery_year = 1994
            
            case "copernicium" | "cn" | 112:
                self.name = "copernicium"
                self.symbol = "Cn"
                self.atomic_number = 112
                self.atomic_mass = 285
                self.electrons_per_shell = (2, 8, 18, 32, 32, 18, 2)
                self.state = None
                self.group = 12
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Gesellschaft für Schwerionenforschung"
                self.discovery_year = 1996

            case "nihonium" | "nh" | 113:
                self.name = "nihonium"
                self.symbol = "Nh"
                self.atomic_number = 113
                self.atomic_mass = 286
                self.electrons_per_shell = (2, 8, 18, 32, 32, 18, 3)
                self.state = "solid"
                self.group = 13
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = "Riken"
                self.discovery_year = 2004
            
            case "flerovium" | "fl" | 114:
                self.name = "flerovium"
                self.symbol = "Fl"
                self.atomic_number = 114
                self.atomic_mass = 289
                self.electrons_per_shell = (2, 8, 18, 32, 32, 18, 4)
                self.state = None
                self.group = 14
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Joint Institute for Nuclear Research, "
                    "Lawrence Livermore National Laboratory")
                self.discovery_year = 1998
            
            case "moscovium" | "mc" | 115:
                self.name = "moscovium"
                self.symbol = "Mc"
                self.atomic_number = 115
                self.atomic_mass = 290
                self.electrons_per_shell = (2, 8, 18, 32, 32, 18, 5)
                self.state = "solid"
                self.group = 15
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Joint Institute for Nuclear Research, "
                    "Lawrence Livermore National Laboratory")
                self.discovery_year = 2003
            
            case "livermorium" | "lv" | 116:
                self.name = "livermorium"
                self.symbol = "Lv"
                self.atomic_number = 116
                self.atomic_mass = 293
                self.electrons_per_shell = (2, 8, 18, 32, 32, 18, 6)
                self.state = "solid"
                self.group = 16
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Joint Institute for Nuclear Research, "
                    "Lawrence Livermore National Laboratory")
                self.discovery_year = 2000
            
            case "tennessine" | "ts" | 117:
                self.name = "tennessine"
                self.symbol = "Ts"
                self.atomic_number = 117
                self.atomic_mass = 294
                self.electrons_per_shell = (2, 8, 18, 32, 32, 18, 7)
                self.state = "solid"
                self.group = 17
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Joint Institute for Nuclear Research, "
                    "Lawrence Livermore National Laboratory, "
                    "Vanderbilt University, Oak Ridge National Laboratory")
                self.discovery_year = 2009

            case "oganesson" | "og" | 118:
                self.name = "oganesson"
                self.symbol = "Og"
                self.atomic_number = 118
                self.atomic_mass = 294
                self.electrons_per_shell = (2, 8, 18, 32, 32, 18, 8)
                self.state = "solid"
                self.group = 18
                self.period = 7
                self.melting_point_k = None
                self.boiling_point_k = None
                self.density = None
                self.natural = False
                self.has_stable_isotope = False
                self.discovery = (
                    "Joint Institute for Nuclear Research, "
                    "Lawrence Livermore National Laboratory")
                self.discovery_year = 2002

            case _:
                raise ElementDoesNotExist(
                    ("Info does not match the name, symbol or atomic number "
                    f"of any element: {info}")
                )