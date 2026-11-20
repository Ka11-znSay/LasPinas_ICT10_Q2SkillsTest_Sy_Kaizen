from pyscript import display, document

non_metals = {
    'Hydrogen': ('H', 1, 1.008),
    'Helium': ('He', 2, 4.003),
    'Carbon': ('C', 6, 12.011),
    'Nitrogen': ('N', 7, 14.007),
    'Oxygen': ('O', 8, 15.999),
    'Fluorine': ('F', 9, 18.998),
    'Neon': ('Ne', 10, 20.180),
    'Phosphorus': ('P', 15, 30.974),
    'Sulfur': ('S', 16, 32.06),
    'Chlorine': ('Cl', 17, 35.45),
    'Argon': ('Ar', 18, 39.948),
    'Selenium': ('Se', 34, 78.971),
    'Bromine': ('Br', 35, 79.904),
    'Krypton': ('Kr', 36, 83.798),
    'Iodine': ('I', 53, 126.904),
    'Xenon': ('Xe', 54, 131.293),
    'Radon': ('Rn', 86, 222)
}

def search_element(e):
    document.getElementById.innerHTML = " "
    element1 = document.getElementById('element').value.strip().title()

    #Using .get()  - no if statement
    data = non_metals.get(
        element1,
        ("Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {data[0]} <br>
    <b>Element:</b> {element1} <br>
    <b>Atomic Number:</b> {data[1]} <br>
    <b>Atomic Mass:</b> {data[2]} <br>
    """