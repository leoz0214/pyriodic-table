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
            lines.append(
                "Discovered by: {} in {}".format(
                    self.discovery,
                    self.discovery_year if self.discovery_year >= 0
                    else f"{abs(self.discovery_year)} BC"
                )
            )

        return "\n".join(lines)

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
                self.has_stable_isotope = True
                self.discovery = "Antoine Jérôme Balard"
                self.discovery_year = 1825
                







            case _:
                raise ElementDoesNotExist(
                    ("Info does not match the name, symbol or atomic number "
                    f"of any element: {info}")
                )


if __name__ == "__main__":
    print(Element("cu").get_display_data())