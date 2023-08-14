# 3190번 뱀

from collections import deque

# 보드의 크기 입력받기
n = int(input())

# 뱀이 이동할 보드 만들기
board = [([0] * n) for _ in range(n)]

# 사과의 위치 입력받기
apple = []
k = int(input())
for _ in range(k):
  input_row, input_col = map(int, input().split())
  # 문제에서 나온 맨위 맨 좌측 (1, 1)을 보드에서는 (0, 0)으로 위치 변환 
  apple_row, apple_col = input_row - 1, input_col - 1
  # 사과 위치를 나타내는 1을 보드에 표시
  board[apple_row][apple_col] = 1
  # 사과 리스트에 사과의 위치 좌표 추가
  apple.append((apple_row, apple_col))

# 뱀의 방향 회전 정보 입력받기
L = int(input())
change_snake = []
for _ in range(L):
  # 뱀의 방향 회전 정보를 리스트에 추가
  dis, direct = input().split()
  dis = int(dis)
  change_snake.append((dis, direct))

# 문제에서 주어진 시간은 10000초 이하로 해결
change_snake.append((10001, ''))

# 뱀의 북, 동, 남, 서 위치이동
change = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 뱀의 방향 전환
def turn_snake(direction):
  global turn_index
  # 왼쪽 방향으로 회전
  if direction == 'L':
    if turn_index != 0:
      turn_index -= 1
    else:
      turn_index = 3
  # 오른쪽 방향으로 회전
  else:
    if turn_index != 3:
      turn_index += 1
    else:
      turn_index = 0
  return

# 게임 전 뱀이 있는 위치
snake = deque()
snake.append((0, 0))

# 게임시작 시 뱀의 시작방향 동쪽
turn_index = 1

# 뱀의 머리 위치
x, y = 0, 0

# 게임 진행시간
cnt = 0
# 방향을 바꿀 때 출발 시간
start = 1

# 반복문 탈출 명령
breaker = False

# 뱀의 방향 정보를 입력받아
for i in range(len(change_snake)): 
  # 게임 시작
  start = cnt + 1
  for _ in range(start, change_snake[i][0]+ 1):
    # 이동할 좌표 설정
    nx = x + change[turn_index][0]
    ny = y + change[turn_index][1]
    # 이동할 좌표가 벽 또는 자기자신의 몸과 부딪힌다면 반복문 종료
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
      cnt += 1
      breaker = True
      break
    # 뱀이 이동할 다음 위치에 사과가 있다면
    if board[nx][ny] == 1:
    # 사과 먹기
      board[nx][ny] = 0
      x, y = nx, ny
      # 뱀의 위치 표시
      snake.append((x, y))
    # 다음 위치에 사과가 없다면
    else:
      x, y = nx, ny
      # 뱀의 위치 표시
      snake.popleft()
      snake.append((x, y))
    # 게임 1초씩 증가
    cnt += 1
  if breaker == True:
    break
  # 뱀 이동후 방향 전환
  turn_snake(change_snake[i][1])  

# 정답 출력
print(cnt)