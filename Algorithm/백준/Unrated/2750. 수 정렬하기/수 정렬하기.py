import sys
input = sys.stdin.readline

times = int(input())

#    ascending order : 오름차순    #
def IN(times: int):
    num_list = []
    
    for i in range(times):
        append_num = int(input())
        num_list.append(append_num)
    
    num_list.sort()
    
    for i in num_list:
        print(i)

IN(times)