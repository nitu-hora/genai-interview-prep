students = []

with open("python/students.csv", "r") as f:
    first_line = True
    for line in f:
        if first_line:
            first_line = False
            continue
        line = line.strip()
        parts = line.split(",")
        name = parts[0]
        scores = [int(x) for x in parts[1:] if x!= ""]
        if len(scores) == 0:
           avg = 0
           result = "No Data"
        else:
            avg = round(sum(scores)/len(scores), 2)
            if avg >= 80:
                result = "Pass"
            elif avg >= 50:
                result = "Average"
            else:
                result = "Fail"
        students.append((name, avg, result))

with open("python/results.csv", "w") as f:
    f.write("name,average,result\n")
    for name, avg, result in students:
        f.write(f"{name},{avg},{result}\n")







