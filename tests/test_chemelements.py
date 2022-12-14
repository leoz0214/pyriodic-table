import sys
import unittest

sys.path.append(".")
sys.path.append("./pyriodic_table")

from pyriodic_table.chemelements import Element


class TestChemElements(unittest.TestCase):

    def test_hydrogen(self):
        hydrogen = Element("Hydrogen")
        self.assertEqual(hydrogen.name, "hydrogen")
        self.assertEqual(hydrogen.symbol, "H")
        self.assertEqual(hydrogen.atomic_number, 1)
        self.assertEqual(hydrogen.protons, 1)
        self.assertEqual(hydrogen.electrons, 1)
        self.assertEqual(hydrogen.atomic_mass, 1.008)
        self.assertEqual(hydrogen.electrons_per_shell, (1,))
        self.assertEqual(hydrogen.state, "gas")
        self.assertEqual(hydrogen.group, 1)
        self.assertEqual(hydrogen.period, 1)
        self.assertEqual(hydrogen.melting_point_k, 13.99)
        self.assertEqual(hydrogen.melting_point_c, -259.16)
        self.assertEqual(hydrogen.melting_point_f, -434.488)
        self.assertEqual(hydrogen.boiling_point_k, 20.271)
        self.assertEqual(hydrogen.boiling_point_c, round(20.271 - 273.15, 10))
        self.assertEqual(hydrogen.boiling_point_f, 
            round(1.8 * (hydrogen.boiling_point_k - 273.15) + 32, 10))
        self.assertEqual(hydrogen.density, 0.00008988)
        self.assertTrue(hydrogen.natural)
        self.assertTrue(hydrogen.has_stable_isotope)
        self.assertEqual(hydrogen.discovery, "Henry Cavendish")
        self.assertEqual(hydrogen.discovery_year, 1766)
    
    def test_elements(self):
        for atomic_number in range(1, 119):
            element = Element(atomic_number)
            self.assertEqual(element.atomic_number, atomic_number)
            self.assertEqual(element.name, str(element))
    
    def test_comparisons(self):
        self.assertEqual(Element("NEON"), Element("ne"))
        self.assertNotEqual(Element(1), Element(2))
        self.assertGreater(Element("mn"), Element("MG"))
        self.assertGreaterEqual(Element(2), Element("HE"))
        self.assertGreaterEqual(Element("bARIUm"), Element("Tc"))
        self.assertLess(Element("terbium"), Element(82))
        self.assertLessEqual(Element("AU"), Element("gold"))
        self.assertLessEqual(Element("astatine"), Element("ACTINIUM"))
        self.assertNotEqual(Element(2), "He")

if __name__ == "__main__":
    unittest.main()