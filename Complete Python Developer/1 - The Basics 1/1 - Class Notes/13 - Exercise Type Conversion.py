from datetime import date
name = "Lukas Rozado"
relationship_status = "Dating"
birth_year = int(input("What year were you born?"))
current_year = date.today().year
age = int(current_year) - birth_year
print(f"Your name is: {name}")
print(f"Your relationship status: {relationship_status}")
print(f"your age is: {age}")


