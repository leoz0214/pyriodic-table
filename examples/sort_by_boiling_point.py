from pyriodic_table.periodictable import PeriodicTable


def sort_by_boiling_point():
    # Elements with no boiling points placed at the end - infinity.

    periodic_table = PeriodicTable()

    return sorted(
        periodic_table, key=lambda element: element.boiling_point_k
        if element.boiling_point_k is not None else float("inf"))


if __name__ == "__main__":
    print(sort_by_boiling_point())


# Output:
"""
[helium, hydrogen, neon, nitrogen, fluorine, argon,
oxygen, krypton, xenon, radon, chlorine, bromine, iodine,
phosphorus, mercury, sulfur, arsenic, caesium, francium, selenium,
rubidium, potassium, cadmium, sodium, zinc, polonium, tellurium,
magnesium, ytterbium, lithium, strontium, thallium, calcium,
europium, bismuth, antimony, radium, lead, barium, samarium,
thulium, manganese, indium, silver, gallium, beryllium, aluminium,
copper, dysprosium, holmium, tin, chromium, nickel, germanium,
scandium, iron, erbium, cobalt, yttrium, palladium, gold, promethium,
gadolinium, neodymium, curium, terbium, praseodymium, actinium, plutonium,
silicon, titanium, lutetium, vanadium, cerium, lanthanum, rhodium, platinum,
boron, protactinium, iridium, uranium, ruthenium, technetium, zirconium,
hafnium, molybdenum, niobium, thorium, carbon, osmium, tantalum, rhenium,
tungsten, astatine, neptunium, americium, berkelium, californium, einsteinium,
fermium, mendelevium, nobelium, lawrencium, rutherfordium, dubnium,
seaborgium, bohrium, hassium, meitnerium, darmstadtium, roentgenium, copernicium,
nihonium, flerovium, moscovium, livermorium, tennessine, oganesson]
"""
# Correct!