candidates = [{"name":"AAA", "age": 30, "language": 'Python', "position": "lead"},
              {"name":"BBB", "age": 28, "language": 'Java', "position": "senior"}]

def get_employees(candidates_list):
    employees = []
    for candidate in candidates:
        if candidate["language"] == "Python":
            employees.append(candidate)
    return employees