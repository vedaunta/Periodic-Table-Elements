
import sys
from tabulate import tabulate 

elements =[
    {"name": "Hydrogen", "symbol": "H", "atomic_number": 1, "atomic_weight": 1.008, "category": ["Combustible Elements","Explosive Elements","Biologically Essential Elements","s-block elements","Non-Metals","Gaseous Elements"]},
    {"name": "Helium", "symbol": "He", "atomic_number": 2, "atomic_weight": 4.0026, "category": ["p-block elements","Noble Gases (Group 18)","Gaseous Elements","Non-Metals"]},
    {"name": "Lithium", "symbol": "Li", "atomic_number": 3, "atomic_weight": 6.94, "category": ["Combustible Elements","Explosive Elements","s-block elements","Alkali Metals (Group 1)","Solid Elements"]},
    {"name": "Beryllium", "symbol": "Be", "atomic_number": 4, "atomic_weight": 9.0122, "category": ["Combustible Elements","s-block elements","Alkaline Earth Metals (Group 2)","Solid Elements"]},
    {"name": "Boron", "symbol": "B", "atomic_number": 5, "atomic_weight": 10.81, "category": ["Semiconductive Elements","Combustible Elements","p-block elements","Solid Elements","Metalloids","Boron Family (Group 13)"]},
    {"name": "Carbon", "symbol": "C", "atomic_number": 6, "atomic_weight": 12.011, "category": ["Combustible Elements","Biologically Essential Elements","p-block elements","Solid Elements","Non-Metals","Carbon Family (Group 14)"]},
    {"name": "Nitrogen", "symbol": "N", "atomic_number": 7, "atomic_weight": 14.007, "category": ["Explosive Elements","Biologically Essential Elements","p-block elements","Non-Metals","Gaseous Elements","Nitrogen Family (Group 15)"]},
    {"name": "Oxygen", "symbol": "O", "atomic_number": 8, "atomic_weight": 15.999, "category": ["Explosive Elements","Biologically Essential Elements","p-block elements","Non-Metals","Gaseous Elements","Chalcogen (Group 16)"]},
    {"name": "Fluorine", "symbol": "F", "atomic_number": 9, "atomic_weight": 18.998, "category": ["Combustible Elements","Explosive Elements","Biologically Essential Elements","p-block elements","Non-Metals","Gaseous Elements","Halogen (Group 17)"]},
    {"name": "Neon", "symbol": "Ne", "atomic_number": 10, "atomic_weight": 20.180, "category": ["p-block elements","Noble Gases (Group 18)","Gaseous Elements","Non-Metals"]},
    {"name": "Sodium", "symbol": "Na", "atomic_number": 11, "atomic_weight": 22.990, "category": ["Combustible Elements","Explosive Elements","Biologically Essential Elements","s-block elements","Alkali Metals (Group 1)","Solid Elements"]},
    {"name": "Magnesium", "symbol": "Mg", "atomic_number": 12, "atomic_weight": 24.305, "category": ["Combustible Elements","Biologically Essential Elements","s-block elements","Alkaline Earth Metals (Group 2)","Solid Elements"]},
    {"name": "Aluminum", "symbol": "Al", "atomic_number": 13, "atomic_weight": 26.982, "category": ["Combustible Elements","p-block elements","Solid Elements","Post-Transition Metals","Boron Family (Group 13)"]},
    {"name": "Silicon", "symbol": "Si", "atomic_number": 14, "atomic_weight": 28.085, "category": ["Semiconductive Elements","Biologically Essential Elements","p-block elements","Solid Elements","Metalloids","Carbon Family (Group 14)"]},
    {"name": "Phosphorus", "symbol": "P", "atomic_number": 15, "atomic_weight": 30.974, "category": ["Combustible Elements","Explosive Elements","Biologically Essential Elements","p-block elements","Solid Elements","Non-Metals","Nitrogen Family (Group 15)"]},
    {"name": "Sulfur", "symbol": "S", "atomic_number": 16, "atomic_weight": 32.06, "category": ["Combustible Elements","Biologically Essential Elements","p-block elements","Solid Elements","Non-Metals","Chalcogen (Group 16)"]},
    {"name": "Chlorine", "symbol": "Cl", "atomic_number": 17, "atomic_weight": 35.45, "category": ["Combustible Elements","Explosive Elements","Biologically Essential Elements","p-block elements","Non-Metals","Gaseous Elements","Halogen (Group 17)"]},
    {"name": "Argon", "symbol": "Ar", "atomic_number": 18, "atomic_weight": 39.948, "category": ["p-block elements","Noble Gases (Group 18)","Gaseous Elmenets","Non-Metals"]},
    {"name": "Potassium", "symbol": "K", "atomic_number": 19, "atomic_weight": 39.098, "category": ["Combustible Elements","Explosive Elements","Biologically Essential Elements","s-block elements","Alkali Metals (Group 1)","Solid Elements"]},
    {"name": "Calcium", "symbol": "Ca", "atomic_number": 20, "atomic_weight": 40.078, "category": ["Combustible Elements","Biologically Essential Elements","s-block elements","Alkaline Earth Metals (Group 2)","Solid Elements"]},
    {"name": "Scandium", "symbol": "Sc", "atomic_number": 21, "atomic_weight": 44.955, "category": ["d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Titanium", "symbol": "Ti", "atomic_number": 22, "atomic_weight": 47.867, "category": ["Combustible Elements","d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Vanadium", "symbol": "V", "atomic_number": 23, "atomic_weight": 50.942, "category": ["Biologically Essential Elements","d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Chromium", "symbol": "Cr", "atomic_number": 24, "atomic_weight": 51.996, "category": ["Biologically Essential Elements","d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Manganese", "symbol": "Mn", "atomic_number": 25, "atomic_weight": 54.938, "category": ["Biologically Essential Elements","d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Iron", "symbol": "Fe", "atomic_number": 26, "atomic_weight": 55.845, "category": ["Catalytic Elements","Combustible Elements","Biologically Essential Elements","d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Cobalt", "symbol": "Co", "atomic_number": 27, "atomic_weight": 58.933, "category": ["Biologically Essential Elements","d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Nickel", "symbol": "Ni", "atomic_number": 28, "atomic_weight": 58.693, "category": ["Catalytic Elements","Biologically Essential Elements","d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Copper", "symbol": "Cu", "atomic_number": 29, "atomic_weight": 63.546, "category": ["Catalytic Elements","Combustible Elements","Biologically Essential Elements","d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Zinc", "symbol": "Zn", "atomic_number": 30, "atomic_weight": 65.38, "category": ["Combustible Elements","Biologically Essential Elements","d-block elements","Transition Metals","Solid Elements"]},
    {"name": "Gallium", "symbol": "Ga", "atomic_number": 31, "atomic_weight": 69.723, "category": ["p-block elements","Solid Elements","Post-Transition Metals","Boron Family (Group 13)"]},
    {"name": "Germanium", "symbol": "Ge", "atomic_number": 32, "atomic_weight": 72.63, "category": ["Semiconductive Elements","p-block elements","Solid Elements", "Metalloids","Carbon Family (Group 14)"]},
    {"name": "Arsenic", "symbol": "As", "atomic_number": 33, "atomic_weight": 74.922, "category": ["Semiconductive Elements","Biologically Essential Elements","p-block elements","Solid Elements", "Metalloids","Nitrogen Family (Group 15)"]},
    {"name": "Selenium", "symbol": "Se", "atomic_number": 34, "atomic_weight": 78.96, "category": ["Biologically Essential Elements","p-block elements","Solid Elements", "Non-Metals","Chalcogen (Group 16)"]},
    {"name": "Bromine", "symbol": "Br", "atomic_number": 35, "atomic_weight": 79.904, "category": ["p-block elements", "Non-Metals", "Liquid Elements", "Halogen (Group 17)"]},
    {"name": "Krypton", "symbol": "Kr", "atomic_number": 36, "atomic_weight": 83.798, "category": ["p-block elements", "Noble Gases (Group 18)", "Gaseous Elements","Non-Metals"]},
    {"name": "Rubidium", "symbol": "Rb", "atomic_number": 37, "atomic_weight": 85.468, "category": ["Explosive Elements","s-block elements", "Alkali Metals (Group 1)","Solid Elements"]},
    {"name": "Strontium", "symbol": "Sr", "atomic_number": 38, "atomic_weight": 87.62, "category": ["s-block elements", "Alkaline Earth Metals (Group 2)","Solid Elements"]},
    {"name": "Yttrium", "symbol": "Y", "atomic_number": 39, "atomic_weight": 88.906, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Zirconium", "symbol": "Zr", "atomic_number": 40, "atomic_weight": 91.224, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Niobium", "symbol": "Nb", "atomic_number": 41, "atomic_weight": 92.906, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Molybdenum", "symbol": "Mo", "atomic_number": 42, "atomic_weight": 95.95, "category": ["Catalytic Elements","Biologically Essential Elements","d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Technetium", "symbol": "Tc", "atomic_number": 43, "atomic_weight": 98, "category": ["d-block elements", "Transition Metals","Radioactive elements","Synthetic (Man-Made) element","Solid Elements"]},
    {"name": "Ruthenium", "symbol": "Ru", "atomic_number": 44, "atomic_weight": 101.07, "category": ["Catalytic Elements","d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Rhodium", "symbol": "Rh", "atomic_number": 45, "atomic_weight": 102.91, "category": ["Catalytic Elements","d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Palladium", "symbol": "Pd", "atomic_number": 46, "atomic_weight": 106.42, "category": ["Catalytic Elements","d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Silver", "symbol": "Ag", "atomic_number": 47, "atomic_weight": 107.87, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Cadmium", "symbol": "Cd", "atomic_number": 48, "atomic_weight": 112.41, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Indium", "symbol": "In", "atomic_number": 49, "atomic_weight": 114.82, "category": ["p-block elements","Solid Elements", "Post-Transition Metals","Boron Family (Group 13)"]},
    {"name": "Tin", "symbol": "Sn", "atomic_number": 50, "atomic_weight": 118.71, "category": ["Biologically Essential Elements","p-block elements","Solid Elements", "Post-Transition Metals","Carbon Family (Group 14)"]},
    {"name": "Antimony", "symbol": "Sb", "atomic_number": 51, "atomic_weight": 121.76, "category": ["Semiconductive Elements","Combustible Elements","p-block elements","Solid Elements", "Metalloids","Nitrogen Family (Group 15)"]},
    {"name": "Tellurium", "symbol": "Te", "atomic_number": 52, "atomic_weight": 127.60, "category": ["Semiconductive Elements","p-block elements","Solid Elements", "Metalloids","Chalcogen (Group 16)"]},
    {"name": "Iodine", "symbol": "I", "atomic_number": 53, "atomic_weight": 126.90, "category": ["Biologically Essential Elements","p-block elements","Solid Elements", "Non-Metals", "Halogen (Group 17)"]},
    {"name": "Xenon", "symbol": "Xe", "atomic_number": 54, "atomic_weight": 131.29, "category": ["p-block elements", "Noble Gases (Group 18)", "Gaseous Elements","Non-Metals"]},
    {"name": "Cesium", "symbol": "Cs", "atomic_number": 55, "atomic_weight": 132.91, "category": ["Explosive Elements","s-block elements", "Alkali Metals (Group 1)","Solid Elements"]},
    {"name": "Barium", "symbol": "Ba", "atomic_number": 56, "atomic_weight": 137.33, "category": ["s-block elements", "Alkaline Earth Metals (Group 2)","Solid Elements"]},
    {"name": "Lanthanum", "symbol": "La", "atomic_number": 57, "atomic_weight": 138.91, "category": ["Catalytic Elements","Combustible Elements","f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Cerium", "symbol": "Ce", "atomic_number": 58, "atomic_weight": 140.12, "category": ["Catalytic Elements","Combustible Elements","f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Praseodymium", "symbol": "Pr", "atomic_number": 59, "atomic_weight": 140.91, "category": ["Strongest Magnetic Property","f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Neodymium", "symbol": "Nd", "atomic_number": 60, "atomic_weight": 144.24, "category": ["Strongest Magnetic Property","Combustible Elements","f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Promethium", "symbol": "Pm", "atomic_number": 61, "atomic_weight": 145, "category": ["f-block elements","Radioactive elements", "Solid Elements","Lanthanides", "Synthetic (Man-Made) element"]},
    {"name": "Samarium", "symbol": "Sm", "atomic_number": 62, "atomic_weight": 150.36, "category": ["Strongest Magnetic Property","f-block elements", "Solid Elements","Lanthanides"]},
    {"name": "Europium", "symbol": "Eu", "atomic_number": 63, "atomic_weight": 151.96, "category": ["f-block elements", "Solid Elements","Lanthanides"]},
    {"name": "Gadolinium", "symbol": "Gd", "atomic_number": 64, "atomic_weight": 157.25, "category": ["f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Terbium", "symbol": "Tb", "atomic_number": 65, "atomic_weight": 158.93, "category": ["f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Dysprosium", "symbol": "Dy", "atomic_number": 66, "atomic_weight": 162.50, "category": ["Strongest Magnetic Property","f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Holmium", "symbol": "Ho", "atomic_number": 67, "atomic_weight": 164.93, "category": ["f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Erbium", "symbol": "Er", "atomic_number": 68, "atomic_weight": 167.26, "category": ["f-block elements", "Solid Elements","Lanthanides"]},
    {"name": "Thulium", "symbol": "Tm", "atomic_number": 69, "atomic_weight": 168.93, "category": ["f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Ytterbium", "symbol": "Yb", "atomic_number": 70, "atomic_weight": 173.05, "category": ["f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Lutetium", "symbol": "Lu", "atomic_number": 71, "atomic_weight": 174.97, "category": ["f-block elements","Solid Elements", "Lanthanides"]},
    {"name": "Hafnium", "symbol": "Hf", "atomic_number": 72, "atomic_weight": 178.49, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Tantalum", "symbol": "Ta", "atomic_number": 73, "atomic_weight": 180.95, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Tungsten", "symbol": "W", "atomic_number": 74, "atomic_weight": 183.84, "category": ["Catalytic Elements","d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Rhenium", "symbol": "Re", "atomic_number": 75, "atomic_weight": 186.21, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Osmium", "symbol": "Os", "atomic_number": 76, "atomic_weight": 190.23, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Iridium", "symbol": "Ir", "atomic_number": 77, "atomic_weight": 192.22, "category": ["Catalytic Elements","d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Platinum", "symbol": "Pt", "atomic_number": 78, "atomic_weight": 195.08, "category": ["Catalytic Elements","d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Gold", "symbol": "Au", "atomic_number": 79, "atomic_weight": 196.97, "category": ["d-block elements", "Transition Metals","Solid Elements"]},
    {"name": "Mercury", "symbol": "Hg", "atomic_number": 80, "atomic_weight": 200.59, "category": ["d-block elements", "Transition Metals", "Liquid Elements"]},
    {"name": "Thallium", "symbol": "Tl", "atomic_number": 81, "atomic_weight": 204.38, "category": ["p-block elements","Solid Elements", "Post-Transition Metals","Boron Family (Group 13)"]},
    {"name": "Lead", "symbol": "Pb", "atomic_number": 82, "atomic_weight": 207.2, "category": ["p-block elements","Solid Elements", "Post-Transition Metals","Carbon Family (Group 14)"]},
    {"name": "Bismuth", "symbol": "Bi", "atomic_number": 83, "atomic_weight": 208.98, "category": ["p-block elements","Solid Elements", "Post-Transition Metals","Nitrogen Family (Group 15)"]},
    {"name": "Polonium", "symbol": "Po", "atomic_number": 84, "atomic_weight": 209, "category": ["p-block elements","Radioactive elements", "Metalloids", "Chalcogen (Group 16)"]},
    {"name": "Astatine", "symbol": "At", "atomic_number": 85, "atomic_weight": 210, "category": ["Explosive Elements","p-block elements","Radioactive elements", "Metalloids", "Halogen (Group 17)","Synthetic (Man-Made) element"]},
    {"name": "Radon", "symbol": "Rn", "atomic_number": 86, "atomic_weight": 222, "category": ["p-block elements","Radioactive elements", "Noble Gases (Group 18)", "Gaseous Elements","Non-Metals"]},
    {"name": "Francium", "symbol": "Fr", "atomic_number": 87, "atomic_weight": 223, "category": ["s-block elements","Radioactive elements", "Alkali Metals (Group 1)","Solid Elements","Synthetic (Man-Made) element"]},
    {"name": "Radium", "symbol": "Ra", "atomic_number": 88, "atomic_weight": 226, "category": ["s-block elements","Radioactive elements", "Alkaline Earth Metals (Group 2)","Solid Elements"]},
    {"name": "Actinium", "symbol": "Ac", "atomic_number": 89, "atomic_weight": 227, "category": ["f-block elements","Radioactive elements","Solid Elements", "Actinides"]},
    {"name": "Thorium", "symbol": "Th", "atomic_number": 90, "atomic_weight": 232.04, "category": ["f-block elements","Radioactive elements","Solid Elements", "Actinides","Nuclear Fuel Potential"]},
    {"name": "Protactinium", "symbol": "Pa", "atomic_number": 91, "atomic_weight": 231.04, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides"]},
    {"name": "Uranium", "symbol": "U", "atomic_number": 92, "atomic_weight": 238.03, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides","Nuclear Fuel Potential"]},
    {"name": "Neptunium", "symbol": "Np", "atomic_number": 93, "atomic_weight": 237, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides","Synthetic (Man-Made) element","Nuclear Fuel Potential"]},
    {"name": "Plutonium", "symbol": "Pu", "atomic_number": 94, "atomic_weight": 244, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element","Nuclear Fuel Potential"]},
    {"name": "Americium", "symbol": "Am", "atomic_number": 95, "atomic_weight": 243, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element","Nuclear Fuel Potential"]},
    {"name": "Curium", "symbol": "Cm", "atomic_number": 96, "atomic_weight": 247, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element","Nuclear Fuel Potential"]},
    {"name": "Berkelium", "symbol": "Bk", "atomic_number": 97, "atomic_weight": 247, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element"]},
    {"name": "Californium", "symbol": "Cf", "atomic_number": 98, "atomic_weight": 251, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element"]},
    {"name": "Einsteinium", "symbol": "Es", "atomic_number": 99, "atomic_weight": 252, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element"]},
    {"name": "Fermium", "symbol": "Fm", "atomic_number": 100, "atomic_weight": 257, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element"]},
    {"name": "Mendelevium", "symbol": "Md", "atomic_number": 101, "atomic_weight": 258, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element"]},
    {"name": "Nobelium", "symbol": "No", "atomic_number": 102, "atomic_weight": 259, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element"]},
    {"name": "Lawrencium", "symbol": "Lr", "atomic_number": 103, "atomic_weight": 262, "category": ["f-block elements","Solid Elements","Radioactive elements", "Actinides", "Synthetic (Man-Made) element"]},
    {"name": "Rutherfordium", "symbol": "Rf", "atomic_number": 104, "atomic_weight": 267, "category": ["d-block elements", "Transition Metals","Radioactive elements", "Synthetic (Man-Made) element","Solid Elements"]},
    {"name": "Dubnium", "symbol": "Db", "atomic_number": 105, "atomic_weight": 270, "category": ["d-block elements", "Transition Metals","Radioactive elements", "Synthetic (Man-Made) element","Solid Elements"]},
    {"name": "Seaborgium", "symbol": "Sg", "atomic_number": 106, "atomic_weight": 271, "category": ["d-block elements", "Transition Metals","Radioactive elements","Synthetic (Man-Made) element","Solid Elements"]},
    {"name": "Bohrium", "symbol": "Bh", "atomic_number": 107, "atomic_weight": 270, "category": ["d-block elements", "Transition Metals","Radioactive elements", "Synthetic (Man-Made) element","Solid Elements"]},
    {"name": "Hassium", "symbol": "Hs", "atomic_number": 108, "atomic_weight": 277, "category": ["d-block elements", "Transition Metals","Radioactive elements", "Synthetic (Man-Made) element","Solid Elements"]},
    {"name": "Meitnerium", "symbol": "Mt", "atomic_number": 109, "atomic_weight": 278, "category": ["d-block elements", "Transition Metals","Radioactive elements", "Synthetic (Man-Made) element","Solid Elements"]},
    {"name": "Darmstadtium", "symbol": "Ds", "atomic_number": 110, "atomic_weight": 281, "category": ["d-block elements", "Transition Metals","Radioactive elements", "Synthetic (Man-Made) element","Solid Elements"]},
    {"name": "Roentgenium", "symbol": "Rg", "atomic_number": 111, "atomic_weight": 282, "category": ["d-block elements", "Transition Metals","Radioactive elements", "Synthetic (Man-Made) element","Solid Elements"]},
    {"name": "Copernicium", "symbol": "Cn", "atomic_number": 112, "atomic_weight": 285, "category": ["d-block elements", "Transition Metals","Radioactive elements", "Synthetic (Man-Made) element"]},
    {"name": "Nihonium", "symbol": "Nh", "atomic_number": 113, "atomic_weight": 286, "category": ["p-block elements", "Radioactive elements","Synthetic (Man-Made) element","Boron Family (Group 13)"]},
    {"name": "Flerovium", "symbol": "Fl", "atomic_number": 114, "atomic_weight": 289, "category": ["p-block elements","Radioactive elements", "Synthetic (Man-Made) element","Carbon Family (Group 14)"]},
    {"name": "Moscovium", "symbol": "Mc", "atomic_number": 115, "atomic_weight": 290, "category": ["p-block elements","Radioactive elements", "Synthetic (Man-Made) element","Nitrogen Family (Group 15)"]},
    {"name": "Livermorium", "symbol": "Lv", "atomic_number": 116, "atomic_weight": 293, "category": ["p-block elements","Radioactive elements", "Synthetic (Man-Made) element","Chalcogen (Group 16)"]},
    {"name": "Tennessine", "symbol": "Ts", "atomic_number": 117, "atomic_weight": 294, "category": ["p-block elements","Radioactive elements", "Halogen (Group 17)", "Synthetic (Man-Made) element"]},
    {"name": "Oganesson", "symbol": "Og", "atomic_number": 118, "atomic_weight": 294, "category": ["p-block elements","Radioactive elements", "Noble Gases (Group 18)", "Synthetic (Man-Made) element"]}

]

categories = [
    "s-block elements","p-block elements","d-block elements","f-block elements",
    "Alkali Metals (Group 1)","Alkaline Earth Metals (Group 2)","Transition Metals",
    "Post-Transition Metals","Boron Family (Group 13)","Carbon Family (Group 14)",
    "Nitrogen Family (Group 15)","Chalcogen (Group 16)","Halogen (Group 17)","Noble Gases (Group 18)",
    "Metalloids","Lanthanides","Actinides","Non-Metals","Gaseous Elements","Liquid Elements","Solid Elements",
    "Biologically Essential Elements","Synthetic (Man-Made) element","Radioactive elements",
    "Explosive Elements","Nuclear Fuel Potential","Combustible Elements","Strongest Magnetic Property",
    "Semiconductive Elements","Catalytic Elements",
]

def display_elements_by_category(category):
    filtered_elements=[
        (elem["name"], elem["symbol"], elem["atomic_number"], elem["atomic_weight"])
        for elem in elements
        if category in elem["category"]
    ]

    if filtered_elements:
        print(tabulate(filtered_elements, headers=["Name", "Symbol", "Atomic Number", "Atomic Weight"], tablefmt="pretty"))
    else:
        print("No elements found for this category.")

def main():
    while True:
        print("\nCategories:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}.{category}")

        choice = input("Please select a category by entering its serial number or type 'exit' to quit: ").strip()

        if choice.lower()=="exit":
            print("Exiting the program. Goodbye!")
            break
        try: 
            choice_idx=int(choice)-1
            if 0<= choice_idx < len(categories):
                selected_category = categories[choice_idx]
                print(f"\nDisplaying the Result for {selected_category}")
                display_elements_by_category(selected_category)
            else:
                print("Invalid Selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to a category.")
        
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont !="yes":
            print("Exiting the program. Goodbye!")
            break

if __name__=="__main__":
    main()
