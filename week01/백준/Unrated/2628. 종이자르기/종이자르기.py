
#가로로 자르는 점선은 0과 점선 번호
#세로로 자르는 점선은 1과 점선 번호
width_length = [0]
height_length = [0]
max = 0

#height 세로 / width 가로
height_max_length, width_max_length = map(int, input().split())
height_length.append(height_max_length)
width_length.append(width_max_length)
run_count = int(input())

for i in range(run_count):
    line_point, cut_location = map(int, input().split())
    #뭔가 여기에 큰 종이를 자르는 영역을 계산해야할꺼 같다.
    if line_point == 0:
        width_length.append(cut_location)
    elif line_point == 1:
        height_length.append(cut_location)
        

height_length.sort()
width_length.sort()
    
# print(height_length)
# print(width_length)

#계산하는 프로그램
for i in range(len(height_length)):
    for j in range(len(width_length)):
        # print(f"i:{i}\tj:{j}\theight_length[{i}]:{height_length[i]}\twidth_length[{j}]:{width_length[j]}")
        # print(f"height_length[{i}] - height_length[{i-1}]: {height_length[i] - height_length[i-1]}")
        # print(f"width_length[{j}] - width_length[{j-1}]: {width_length[j] - width_length[j-1]}\n")
        # 두 값이 0보다 클때의 if 문
        if (height_length[i] - height_length[i-1]) > 0 and (width_length[j] - width_length[j-1]) > 0:
            if_max = (height_length[i] - height_length[i-1]) * (width_length[j] - width_length[j-1])
        # print(if_max)
            # 넓이의 값 중 제일 큰 값을 구하는 if 문
            if if_max > max:
                max = if_max

print(max)   