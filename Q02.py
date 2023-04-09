# x = input()
# def calculate(ex_input):
#     list_num = ex_input.split(" ")
#     a, b = int(list_num[0]), int(list_num[1])
#
#     plus = a + b
#     minus = a - b
#     times = a * b
#     divide = a // b
#     remainder = a % b
#     print(f"{plus}\n{minus}\n{times}\n{divide}\n{remainder}")
#
# calculate(x)

x = input().split()
a,b = int(x[0]), int(x[1])
print(f"{a + b}\n{a - b}\n{a * b}\n{a // b}\n{a % b}")