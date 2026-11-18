import json

data = {
  "company": "TechCorp",
  "employees": [
    {"id": 1, "name": "Alice", "department": "Engineering", "skills": ["Python", "SQL", "Spark"], "salary": 95000},
    {"id": 2, "name": "Bob", "department": "Marketing", "skills": ["Excel", "PowerPoint"], "salary": 60000},
    {"id": 3, "name": "Charlie", "department": "Engineering", "skills": ["Java", "Docker", "Kubernetes"], "salary": 110000},
    {"id": 4, "name": "Diana", "department": "HR", "skills": ["Communication"], "salary": 55000}
  ]
}

# Step 1: Write to file
with open("employees.json", "w") as f:
    json.dump(data, f)

# Step 2: Read back
with open("employees.json", "r") as f:
    data = json.load(f)

# Step 3: Process
total_salary = 0
engineering_team = []

for emp in data["employees"]:
    total_salary += emp["salary"]
    if emp["department"] == "Engineering":
        engineering_team.append(emp["name"])
    if emp["salary"] >= 90000:
        emp["salary_grade"] = "High"
    else:
        emp["salary_grade"] = "Standard"

avg_salary = total_salary / len(data["employees"])

# Step 4: Write updated file
with open("employees_updated.json", "w") as f:
    json.dump(data, f, indent=2)

# Step 5: Build summary dict and print it first
summary = {
    "company": data["company"],
    "total_employees": len(data["employees"]),
    "avg_salary": avg_salary,
    "engineering_team": engineering_team
}

print("Summary before writing to file:")
print(summary)

# Step 6: Write summary to its own file
with open("summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("Done. Files written: employees_updated.json, summary.json")