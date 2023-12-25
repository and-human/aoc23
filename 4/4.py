import numpy as np

with open("input.txt") as f:
    data = [lines.split('|') for lines in [lines.strip()[9:] for lines in f.readlines()]]
f.close()

#part 1 
sum_list = []
total_sum = 0
for i in range(len(data)):
    ini_list = [int(j) for j in data[i][0].split()]
    comp_list = [int(j) for j in data[i][1].split()]
    sum_list.append(len(np.intersect1d(ini_list, comp_list)))

    if sum_list[i]==1:
        total_sum+=1
    elif sum_list[i]>1:
       total_sum+=(2**(sum_list[i]-1))
    else:
        total_sum+=0

print("Output 1: ",total_sum)

# #part 2

arr = np.zeros(len(data),dtype=int)

for i in range(len(sum_list)):
    arr[i+1:sum_list[i]+i+1]+=1 if sum_list[i]>0 else 0

    if arr[i]>0:
        for j in range(arr[i]) :
            arr[i+1:sum_list[i]+i+1]+=1

arr[:]+=1 
print("Output 2: ", sum(arr))