# ask user for name
name = input("what is your name? ") 

# greet user by name
print(f"hello {name}")

# ask what year they were born 
birth_year = int(input("what year were you born? "))

# give the user their approximate age in dog years
age = 2026 - {birth_year} 

print(f"you are {age} years old in human years" )
dog_age = age * 7