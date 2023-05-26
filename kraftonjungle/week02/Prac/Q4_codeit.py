# # 두 요소의 위치를 바꿔주는 helper function
# def swap_elements(my_list, index1, index2):
#     my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
#     return my_list[index1], my_list[index2]


# # 퀵 정렬에서 사용되는 partition 함수
# def partition(my_list, start, end):
#     # 여기에 코드를 작성하세요
    
#     # end는 피벗(pivot), 기준점이다. p = end
    
#     p = end
#     b = i = 0
    
#     if (my_list[p] <= my_list[i]):
#         i += 1
#     elif (my_list[p] > my_list[i]):
#         swap_elements(my_list, my_list[i], my_list[b])
#         i += 1
#         b += 1
    
    
#     #small그룹과 big그룹, unknown그룹을 움직여야함 #b와 i를 활용
    


# # 테스트 코드 1
#  list1 = [4, 3, 6, 2, 7, 1, 5]
# pivot_index1 = partition(list1, 0, len(list1) - 1)
# print(list1)
# print(pivot_index1)

# # 테스트 코드 2
# list2 = [6, 1, 2, 6, 3, 5, 4]
# pivot_index2 = partition(list2, 0, len(list2) - 1)
# print(list2)
# print(pivot_index2)
