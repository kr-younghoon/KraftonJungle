pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

count = 0

# def put():
#     for j in range(8):
#         for i in range(8):
#             print('ㅁ' if pos[i] == j else 'ㅇ', end="")
#         print()
#     print()

def set(i):
    global count
    for j in range(8):
        if (    not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + 7]):
            pos[i] = j
            if i == 7:
                count += 1
                # put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False
    return count

N = int(input())

set(0)
print(count)