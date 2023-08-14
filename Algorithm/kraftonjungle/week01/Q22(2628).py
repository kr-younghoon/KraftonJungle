# 문제
# 아래 <그림 1>과 같이 직사각형 모양의 종이가 있다. 이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다. 
# 가로 점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고, 세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.



# <그림 1>

# 점선을 따라 이 종이를 칼로 자르려고 한다. 가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지, 
# 세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다. 
# 예를 들어, <그림 1>의 가로 길이 10㎝이고 세로 길이 8㎝인 종이를 3번 가로 점선, 4번 세로 점선, 
# 그리고 2번 가로 점선을 따라 자르면 <그림 2>와 같이 여러 개의 종이 조각으로 나뉘게 된다. 이때 가장 큰 종이 조각의 넓이는 30㎠이다.



# <그림 2>

# 입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.

# 입력
# 첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. 가로와 세로의 길이는 최대 100㎝이다. 
# 둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 
# 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 세로로 자르는 점선은 1과 점선 번호가 주어진다. 
# 입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.

# 출력
# 첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.

# 예제 입력 1 복사
# 10 8
# 3
# 0 3
# 1 4
# 0 2
# 예제 출력 1 복사
# 30



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