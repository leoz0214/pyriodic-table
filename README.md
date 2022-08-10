# --- pyriodic_table ---

`pyriodic_table` is a simple Python package which aims to achieve the following:

- Provide *insightful* data (as accurate as possible) on the 118 chemical elements discovered to date,
starting with **hydrogen**, all the way to the super-heavy **oganesson**!
- Make this data easily accessible, in an organised manner.
- Allow easy identification of elements to access their data, through multiple methods.
- Be user-friendly and easy to use.

The PyPi page for the package is:
https://pypi.org/project/pyriodic-table/

The most recent version is 1.0.0.

## About the data

Various data points are provided for each element.

### Data Categories

#### Name

This is simply what the element is called, and is self-explanatory.

For example, the first element is called hydrogen.

#### Symbol

This is the abbrevation for an element, consisting of one or two Latin letters, and
starts with a capital letter. It is much more convenient than having to refer
to an element's name.

For example, the symbol for hydrogen is '**H**', and the symbol
for gold is '**Au**' (*aurum*).

As in the example of gold, element symbols can be misleading and not so obvious as to which element they represent.

#### Atomic number

This is just the number of protons in an atom's nucleus (which also happens to be
the number of electrons in an atom's shells - to cancel out the positive charge of the
protons). In addition, the atomic number indicates the nth element.

For example, hydrogen has an atomic number of **1** and is the **1**st element. And oganesson has an atomic number
of **118** and is the **118**th element.

#### Atomic mass

This is how heavy on average an atom of an element is, compared to the carbon-12 isotope,
which has a mass of exactly 12. For example, if element X has an isotope with mass
number of 25 (50% of element X), and an isotope with mass number of 27 (50% of element X),
element X would have an atomic mass of 26. If an element has no stable isotopes, the mass
number of its longest-lived isotope is considered to be its atomic mass.

For example, hydrogen has an atomic mass of **1.008**, and astatine, the rarest natural element,
has an atomic mass of **210** (astatine-210 has the longest half life of all astatine
radioisotopes).

#### Electrons per shell

This is the number of electrons in each energy level of an atom.

For example, hydrogen has only one electron and thus only 1 shell: **(1,)**.
But potassium has 19 electrons: **(2, 8, 8, 1)**.

#### State

This refers to what form the matter of an element takes at room temperature, either
*solid*, *liquid* or *gas*.

For example, oxygen is obviously a **gas** at room temperature, and
equally unsurprisingly, iron is a **solid** at room temperature.

Surprisingly, only two elements are liquids at room temperature: bromine and mercury.

#### Group

A group in the periodic table is a vertical column of elements. Most elements belong in one,
but some elements, including most lanthanides (e.g lanthanum), are not put into one.
Some groups also have special names, including:

- Group 1 - **alkali metals** (e.g sodium) [Be careful, hydrogen is also in group 1 but certainly is not a metal.]
- Group 2 - **alkaline earth metals** (e.g calcium)
- Group 17 - **halogens** (e.g iodine)
- Group 18 - **noble gases** (e.g helium)

#### Period

A period is a horizontal row of elements. For example, hydrogen is in period **1** and
copper is in period **4**.

#### Melting point

This is the temperature at which an element turns from a solid into a liquid. It varies
significantly over different elements. The three temperature units: *Kelvin (K)*,
*Celsius (°C)* and *Fahrenheit (°F)* are all supported.

For example, hydrogen has a melting point of **13.99 K / -259.16 °C / -434.488 °F**;
and titanium has a melting point of **1941 K / 1667.85 °C / 3034.13 °F**.

#### Boiling point

This is the temperature at which an element turns from a liquid into a gas. It varies
significantly over different elements. Like melting point, all three temperature
units are supported.

For example, hydrogen has a boiling point of **20.271 K / -252.897 °C / -423.1822 °F**;
and titanium has a boiling point of **3560 K / 3286.86 °C / 5948.33 °F**.

#### Density

This is the mass per unit volume of an element at room temperature. Gases have an
extremely low density compared to solids and liquids. The unit used by all elements
is nonetheless g/cm³.

For example, hydrogen has a density of only **0.00008988 g/cm³**, whilst
osmium has a whopping density of **22.59 g/cm³**.

#### Natural?

This refers to whether or not an element can be found naturally and is not synthetic (man-made). As long as an element exists in extremely trace quantities, it counts as natural, so this includes technetium and promethium!

For example, carbon is certainly found naturally,
whilst americium is synthetic.

#### Has stable isotope?

This refers to whether or not an element can be stable. If an element does not have at least one stable isotope, it is radioactive. Note that elements which have at least have one stable isotope certainly can also have several radioisotopes.

For example, tin has many stable isotopes, whilst uranium is radioactive.

#### Discovery

This refers to the person/people or place(s) that first found the element, either through
nature or synthetically.

For example, **Henry Cavendish** discovered hydrogen, but **Riken** (a large scientific
research institute in Japan) discovered nihonium.

#### Discovery year

Self-explanatory! This refers to the year of element discovery.
For example, hydrogen was discovered in **1766** (by Cavendish),
and nihonium was discovered relatively recently - in **2004**.

### Data accuracy, completeness and reliability

Element data has been manually obtained and entered carefully, from various sources, including:
- *Wikipedia* pages for each element.
- *Royal Society of Chemistry* - https://www.rsc.org/periodic-table

Unfortunately, many elements have missing data, such as melting/boiling points and density.
Furthermore, particular data for certain elements may be inaccurate.

Nonetheless, the common elements likely have high-quality accurate data, and conveniently, they are the
most used.

For example, unsurprisingly oxygen, an abundant element we need for respiration
is much better known than livermorium, a synthetic, radioactive, short-lived element of which
only a few atoms have ever been produced.

## Compatability

Python 3.9 or greater is supported.
