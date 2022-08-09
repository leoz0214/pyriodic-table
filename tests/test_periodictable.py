import sys
import unittest

sys.path.append(".")
sys.path.append("./pyriodic_table")

from pyriodic_table.periodictable import PeriodicTable


class TestPeriodicTable(unittest.TestCase):

    def test_creation(self):
        periodic_table = PeriodicTable()
        self.assertEqual(len(periodic_table), 118)
        self.assertEqual(len(periodic_table.natural_elements), 93)
        self.assertEqual(len(periodic_table.synthetic_elements), 25)
        self.assertEqual(len(periodic_table.alkali_metals), 6)
        self.assertEqual(len(periodic_table.alkaline_earth_metals), 6)
        self.assertEqual(len(periodic_table.lanthanides), 15)
        self.assertEqual(len(periodic_table.actinides), 15)
        self.assertEqual(len(periodic_table.halogens), 6)
        self.assertEqual(len(periodic_table.noble_gases), 7)

        for element in periodic_table.elements_with_stable_isotope:
            self.assertTrue(element.has_stable_isotope)
        for element in periodic_table.elements_without_stable_isotope:
            self.assertFalse(element.has_stable_isotope)
    
    def test_name(self):
        periodic_table = PeriodicTable()
        self.assertEqual(periodic_table.get_element_by_name(
            "helium"
        ).atomic_number, 2)
        self.assertEqual(periodic_table.get_element_by_name(
            "BARIUM"
        ).protons, 56)
        self.assertEqual(periodic_table.get_element_by_name(
            "OgAnesSON"
        ).electrons, periodic_table.get_element_by_name(
            "acTinium"
        ).atomic_number + periodic_table.get_element_by_name(
            "cOPPER"
        ).protons)
    
    def test_names(self):
        def third(name: str):
            return len(name) >= 5 and name.endswith("on")

        pt = PeriodicTable()
        self.assertEqual(pt.get_elements_by_name(
            lambda name: len(name) == 3
        )[0].name, "tin")
        self.assertEqual(pt.get_elements_by_name(
            lambda name: name.startswith("bo")
        )[1].name, "bohrium")
        self.assertEqual(str(pt.get_elements_by_name(third)[-1]), "oganesson")
    
    def test_atomic_number(self):
        pt = PeriodicTable()
        for i in range(1, len(pt) + 1):
            self.assertEqual(
                pt.get_element_by_atomic_number(i), pt.elements[i-1]
            )
    
    def test_atomic_numbers(self):
        pt = PeriodicTable()
        self.assertEqual(
            len(pt.get_elements_by_atomic_number(1, 10, 2)), 5
        )
        self.assertEqual(pt.get_elements_by_atomic_number(
            33, 100, 3
        )[-1].name, "einsteinium")
        self.assertEqual(
            pt.get_elements_by_atomic_number(118, 0, -1)[-1].name, "hydrogen"
        )
        self.assertEqual(pt.get_elements_by_atomic_number(
            float("-inf"), float("inf")
        ), pt.get_elements_by_atomic_number(1, 119))
    
    def test_symbol(self):
        pt = PeriodicTable()
        for i in range(1, 119):
            self.assertEqual(
                pt.elements[i - 1],
                pt.get_element_by_symbol(pt.elements[i - 1].symbol)
            )
            self.assertEqual(
                pt.elements[i - 1],
                pt.get_element_by_symbol(pt.elements[i - 1].symbol.lower())
            )
            self.assertEqual(
                pt.elements[i - 1],
                pt.get_element_by_symbol(pt.elements[i - 1].symbol.upper())
            )
    
    def test_symbols(self):
        pt = PeriodicTable()
        self.assertEqual(len(pt.get_elements_by_symbol(
            lambda symbol: len(symbol) == 1
        )), 14)
        self.assertEqual(pt.get_elements_by_symbol(
            lambda symbol: symbol.startswith("O")
        )[-1].symbol, "Og")
    
    def test_states(self):
        pt = PeriodicTable()
        self.assertEqual(pt.get_elements_by_state(
            "solid"
        )[0].name, "lithium")
        self.assertEqual(pt.get_elements_by_state(
            "liquid"
        )[-1].name, "mercury")
        self.assertEqual(pt.get_elements_by_state(
            "gas"
        )[3].symbol, "O")

        self.assertEqual(pt.get_elements_by_state("SOLID"),
        pt.get_elements_by_state("S"))

        self.assertEqual(pt.get_elements_by_state("LiQuid"),
        pt.get_elements_by_state("l"))

        self.assertEqual(pt.get_elements_by_state("Gas"),
        pt.get_elements_by_state("G"))
    
    def test_groups(self):
        pt = PeriodicTable()
        self.assertEqual(pt.get_elements_by_group(
            1
        )[1:], pt.alkali_metals)
        self.assertEqual(pt.get_elements_by_group(
            2
        ), pt.alkaline_earth_metals)
        self.assertEqual(pt.get_elements_by_group(
            17
        ), pt.halogens)
        self.assertEqual(pt.get_elements_by_group(
            18
        ), pt.noble_gases)
    
    def test_periods(self):
        pt = PeriodicTable()
        self.assertEqual(pt.get_elements_by_period(
            1
        )[-1].atomic_number, 2)
        self.assertEqual(pt.get_elements_by_period(
            2
        )[3].name, "carbon")
        self.assertEqual(pt.get_elements_by_period(
            3
        )[-1].symbol, "Ar")
    
    def test_melting_points(self):
        pt = PeriodicTable()
        self.assertFalse(pt.get_elements_by_melting_point(
            float("-inf"), -273.16, "c"
        ))
        self.assertEqual(pt.get_elements_by_melting_point(
            -273.15, -250, "C"
        )[0].name, "hydrogen")
        self.assertEqual(pt.get_elements_by_melting_point(
            6191.3, 6191.4, "f"
        )[0].symbol, "W")
        self.assertEqual(pt.get_elements_by_melting_point(
            600, 601, "K"
        )[0].name, "lead")
    
    def test_boiling_points(self):
        pt = PeriodicTable()
        self.assertFalse(pt.get_elements_by_boiling_point(
            float("-inf"), -273.16, "c"
        ))
        self.assertEqual(pt.get_elements_by_boiling_point(
            pt.radon.boiling_point_f, pt.radon.boiling_point_f, "F"
        )[0].name, "radon")
    
    def test_density(self):
        pt = PeriodicTable()
        self.assertFalse(pt.get_elements_by_density(-1, 0))
        self.assertEqual(
            max(
                pt.get_elements_by_density(22, 23), key=lambda x: x.density
            ).name, "osmium"
        )
    
    def test_discovery_year(self):
        pt = PeriodicTable()
        self.assertFalse(pt.get_elements_by_discovery_year(-10000, -9999))
        self.assertEqual(pt.get_elements_by_discovery_year(-10000, 0)[0].name,
        "copper")
        self.assertEqual(pt.get_elements_by_discovery_year(
            2005, 2010
        )[0].atomic_number, 117)
        

if __name__ == "__main__":
    unittest.main()