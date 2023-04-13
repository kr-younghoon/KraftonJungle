#문자열 횟수 입력
times = int(input())
text_input = []

for i in range(times):
    text_input.append(input().split())
    # print(text_input)
    
    
for i in text_input:
    for j in range(len(i[1])):
        # print(f"\nfor {j} in {range(len(i[1]))}\n")
        print(f"{i[1][j] * int(i[0])}", end="")
    print("")