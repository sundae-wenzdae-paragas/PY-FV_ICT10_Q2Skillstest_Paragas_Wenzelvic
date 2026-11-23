#Pyscript Coding on Dicts
#Example Code: metalloids = { "g":("Boron", 5, 10.8811)}

from pyscript import document, display

#This Dict is Composed of Non-Metal Elements that are arranged in a sequence based on Atomic Number
Non_Elements20 = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "At": ("Astatine", 85, 210),
    "Rn": ("Radon", 86, 222),
    "Ts": ("Tennessine", 117, 294),
    "Og": ("Oganesson", 118, 294)
}

def search_element(event):
    Element1 = document.getElementById("Element_Symbol").value

    result = Non_Elements20.get(Element1, ("Element not found", "-", "-"))

    display(f"""
Symbol: {Element1}
Element: {result[0]}
Atomic Number: {result[1]}
Atomic Mass: {result[2]}
""", target="output1", append=False)




#SOME REFERENCE CODES FROM MA'AM EVANGELISTA
#def name (e) output1 format display code
#document.getElementById("result").innerHTML = f"""
#<b> Symbol: <b> {element1} <br>
#<b> Element: <b> {element_display[0]}<br>
#<b> Atomic Number: <b> {element_display[1]}<br>
#<b> Atomic Mass: <b> {element_display[2]}<br>
#"""