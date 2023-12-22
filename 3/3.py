import sys

with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]
f.close()

special_char="""`~!@#$%^&*()_-+={[]}|\:;"'<,>?/"""

#part 1
numbers_found=[]

for i in range(len(data)):
    j=0
    while j!=len(data[i]):
        if data[i][j].isnumeric():
            num=''
            score=0
            l=j
            while data[i][l].isnumeric():
                num+=data[i][l]
                if l==len(data[i])-1:
                    break
                else:
                    l+=1
            
            k=0 if j-1<0 else j-1
            m=j+len(num) if j+len(num)+1>len(data[i]) else j+len(num)+1

            if (data[i][k] in special_char):
                score+=1   
            if j+len(num)!=len(data[i]) and (data[i][j+len(num)] in special_char):
                score+=1
            if (any(char in special_char for char in data[i-1][k:m])):
                score+=1
            if  i+1!=len(data) and (any(char in special_char for char in data[i+1][k:m])):
                score+=1
                         
            if score>0:
                numbers_found.append(int(num))

            j+=len(num)
        else:
            j+=1
            continue

print("Output 1: ",sum(numbers_found))

#part 2
