N = int(input())
counting = 0

for i in range(1,int(N)+1):
    if (1 <= i <= 99):
        counting += 1
    if (100 <= i <= 999):
        a = str(i)
        if (int(a[1]) - int(a[0])) == (int(a[2]) - int(a[1])):
            counting += 1

print(counting)            
    
    