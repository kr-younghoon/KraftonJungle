# Divide and Conquer 방식으로 merge_sort 함수를 써 보세요. 
# merge_sort는 파라미터로 리스트 하나를 받고, 정렬된 새로운 리스트를 리턴합니다.

# merge 함수는 이전 과제에서 작성한 그대로 사용하면 됩니다!

def merge(list1, list2):
    # 여기에 코드를 작성하세요
    merged_list = []
    
    i = j = 0
    
    while (i < len(list1) and j < len(list2)):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1
            
    if i == len(list1):
        merged_list += list2[j:]
    elif j == len(list2):
        merged_list += list1[i:]
        
    return merged_list

# 합병 정렬
def merge_sort(my_list):
    #base_case
    if len(my_list) < 2:
        return my_list
    #divide
    mid = len(my_list) // 2
    left = my_list[mid:]
    right = my_list[:mid]
    
    return merge(merge_sort(left), merge_sort(right))
    
        

        
    
        
        
    

# 테스트 코드
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
