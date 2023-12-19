import re

with open("input.txt") as f:
    data = [i.strip() for i in f.readlines()]
f.close()

#part 1
numbers=[]
for line in data:
    #find all the numbers in line using regex
    result=re.findall(r'\d+', line)
    num=result[0][0]+result[-1][-1]
    numbers.append(int(num))
    
print("Output 1: ",sum(numbers))

#part 2

num_dict={'one':1,
          'two':2,
          'three':3,
          'four':4,
          'five':5,
          'six':6,
          'seven':7,
          'eight':8,
          'nine':9,}

num_all=[]

for i in data:
    numbers_found=[]

    #find the numbers in words
    for j in num_dict.keys():
        if j in i:
            for m in re.finditer(j,i):
                numbers_found.append([m.start(),num_dict[j]])

    #find numeric numbers
    for j in num_dict.values():
        if str(j) in i:
            for m in re.finditer(str(j),i):
                numbers_found.append([m.start(),j])


    #return a sorted list of the numbers found 
    numbers_found.sort(key=lambda x: x[0])
    num_all.append(int(f"{numbers_found[0][1]}{numbers_found[-1][1]}"))

print("Output 2: ",sum(num_all))