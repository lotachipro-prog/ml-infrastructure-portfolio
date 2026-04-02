def get_result(years):
    
        if years >= 3:
            return "Strong application"
        elif years >= 1:
            return "Promising application"
        else:
            return "Need more experience"
    


applications = [
    {"name": "Lota", "role": "ML Engineer", "years": 2},
    {"name": "Sarah", "role": "Data Engineer", "years": 4},
    {"name": "James", "role": "MLOps Engineer", "years": 0}
]
for app in applications:
    print(app["name"], "-", app["role"], "-", get_result(app["years"]))

with open("results.txt", "w") as file:
    for app in applications:
        result = get_result(app["years"])
        file.write(app["name"] + " - " + app["role"] + " - " + result + "\n")

with open("results.txt", "r") as file:
    content = file.read()
    print(content)