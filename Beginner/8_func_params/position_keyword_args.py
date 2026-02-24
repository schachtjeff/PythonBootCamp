# Functions with more than 1 parameter

def greet_with(name, location) -> None:
    print(f"hello {name}")
    print(f"What is it like in {location}")

greet_with('Jeff', 'Atfalati')

greet_with(name="Jeff", location="Atfalati")
