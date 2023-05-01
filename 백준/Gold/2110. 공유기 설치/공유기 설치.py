import sys
input = sys.stdin.readline

# input 값 setting
house_location = []

house, iptime = map(int, input().split())
for i in range(int(house)):
    house_location.append(int(input()))
house_location.sort()

# binary_search location setting / 정답 셋팅(-1)
left, right = 1, house_location[-1] - house_location[0]
answer = - 1

while(left <= right):
    mid = (left + right) // 2 # ? 왜 미드를 구하는지에 대한 ? 
    setting = 1 # 공유기 셋팅 대수 3이 꽉차면 한칸 줄임
    iptime_location = house_location[0] # 공유기 로케이션 셋 house_location[0] -> 1
    
    for i in range(1, house): #집의 개수 많큼 움직임 (ex:5) -> range(1, 5)
        distance = house_location[i] - iptime_location # 거리 측정으로 가장 인접한 공유기 사이의 최대 거리 출력.
        if distance >= mid: #거리가 미드의 값보다 많으면 공유기를 설치?
            iptime_location = house_location[i] 
            setting += 1
    if setting >= iptime:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(answer)