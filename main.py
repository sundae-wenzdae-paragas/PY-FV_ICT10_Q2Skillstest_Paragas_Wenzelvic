#Pyscript Coding on Dicts
#Example Code: metalloids = { "g":("Boron", 5, 10.8811)}

from pyscript import document, display

#This Dict is Composed of Non-Metal Elements that are arranged in a sequence based on Atomic Number
Non_Elements20 = {
    "H":{
        "Type":"A Diatomic Nonmetal",
        "Name":"Hydrogen",
        "Atomic Number":"1",
        "Atomic Mass":"1.008"
    },
    
    "He":{
        "Type":"A Noble Gas",
        "Name":"Helium",
        "Atomic Number":"2",
        "Atomic Mass":"4.0026"
    },
    
    "C":{
        "Type":"A Polyatomic Nonmetal",
        "Name":"Carbon",
        "Atomic Number":"6",
        "Atomic Mass":"12.011"
    },
    
    "N":{
        "Type":"A Diatomic Nonmetal",
        "Name":"Nitrogen",
        "Atomic Number":"7",
        "Atomic Mass":"14.007"
    },
    
    "O":{
        "Type":"A Diatomic Nonmetal",
        "Name":"Oxygen",
        "Atomic Number":"8",
        "Atomic Mass":"15.999"
    },
    
    "F":{
        "Type":"A Diatomic Nonmetal",
        "Name":"Fluorine",
        "Atomic Number":"9",
        "Atomic Mass":"18.998"
    },
    
    "Ne":{
        "Type":"A Noble Gas",
        "Name":"Neon",
        "Atomic Number":"10",
        "Atomic Mass":"20.180"
    },
    
    "P":{
        "Type":"A Polyatomic Nonmetal",
        "Name":"Phosphorus",
        "Atomic Number":"15",
        "Atomic Mass":"30.974"
    },
    
    "S":{
        "Type":"A Polyatomic Nonmetal",
        "Name":"Sulfur",
        "Atomic Number":"16",
        "Atomic Mass":"32.06"
    },
    
    "Cl":{
        "Type":"A Diatomic Nonmetal",
        "Name":"Chlorine",
        "Atomic Number":"17",
        "Atomic Mass":"35.45"
    },
    
    "Ar":{
        "Type":"A Noble Gas",
        "Name":"Argon",
        "Atomic Number":"18",
        "Atomic Mass":"39.948"
    },
    
    "Se":{
        "Type":"A Polyatomic Nonmetal",
        "Name":"Selenium",
        "Atomic Number":"34",
        "Atomic Mass":"78.971"
    },
    
    "Br":{
        "Type":"A Diatomic Nonmetal",
        "Name":"Bromine",
        "Atomic Number":"35",
        "Atomic Mass":"79.904"
    },
    
    "Kr":{
        "Type":"A Noble Gas",
        "Name":"Krypton",
        "Atomic Number":"36",
        "Atomic Mass":"83.798"
    },
    
    "I":{
        "Type":"A Diatomic Nonmetal",
        "Name":"Iodine",
        "Atomic Number":"53",
        "Atomic Mass":"126.90"
    },
    
    "Xe":{
        "Type":"A Noble Gas",
        "Name":"Xenon",
        "Atomic Number":"54",
        "Atomic Mass":"131.29"
    },
    
    "At":{
        "Type":"A Halogen",
        "Name":"Astatine",
        "Atomic Number":"85",
        "Atomic Mass":"210"
    },
    
    "Rn":{
        "Type":"A Noble Gas",
        "Name":"Radon",
        "Atomic Number":"86",
        "Atomic Mass":"222"
    },
    
    "Ts":{
        "Type":"A Halogen",
        "Name":"Tennessine",
        "Atomic Number":"117",
        "Atomic Mass":"294"
    },
    
    "Og":{
        "Type":"A Noble Gas",
        "Name":"Oganesson",
        "Atomic Number":"118",
        "Atomic Mass":"294"
    }    
}

#SOME REFERENCE CODES FROM MA'AM EVANGELISTA
#def name (e) output1 format display code
#document.getElementById("result").innerHTML = f"""
#<b> Symbol: <b> {element1} <br>
#<b> Element: <b> {element_display[0]}<br>
#<b> Atomic Number: <b> {element_display[1]}<br>
#<b> Atomic Mass: <b> {element_display[2]}<br>
#"""

