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
            
        
        
    
    
# 테스트 코드
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))