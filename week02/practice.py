solution_list = [0, 1, 2, 3, 4, 5, 6]

for i in solution_list:
    for j in solution_list[:-1]:
        if i != j:
            print(f"{i} | {j}")