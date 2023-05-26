n1 = input()
n2 = input()

for i in range(2, -1, -1):
    print(f"{int(n1) * int(n2[i])}")

print(int(n1) * int(n2))