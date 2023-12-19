import re

with open("input.txt") as f:
    data = [i.strip() for i in f.readlines()]
f.close()

for i in data:
    data[data.index(i)] = re.split(r':|;',i)

#definition for part 1
allowed_balls = {'red':12,'green':13,'blue':14}
allowed_games=[]

#part 1
for i in data:
    score=0
    for j in i[1:]:
        res = j.strip().replace(',','').split()
        #iterating through different sets in each game and making the comparision using a score variable
        for k in range(1,len(res),2):
            if allowed_balls[res[k]] < int(res[k-1]):
                score-=1
        score+=1
    
    #if score is equal to the number of sets in the game, then the game id is appended to the allowed_games list
    if score == len(i)-1:
        allowed_games.append(data.index(i)+1)

print("Output 1: ",sum(allowed_games))

allowed_cubes=[]
# part 2
for i in data:
    allowed_balls = {'red':1,'green':1,'blue':1}
    for j in i[1:]:
        res = j.strip().replace(',','').split()
        #iterating through different sets in each game and making the comparision using a score variable
        for k in range(1,len(res),2):
            if allowed_balls[res[k]] < int(res[k-1]):
                allowed_balls[res[k]] = int(res[k-1])
        

    allowed_cubes.append(allowed_balls['red']*allowed_balls['green']*allowed_balls['blue'])


print("Output 2: ",sum(allowed_cubes))   