import random
import math
def roll(sides, bias_list):
    assert len(bias_list) == sides
    number = random.uniform(0, sum(bias_list))
    current = 0
    for i, bias in enumerate(bias_list):
        current += bias
        if number <= current:
            return i + 1

number_of_attempts = int(input())

for z in range(number_of_attempts):
    bias_list = [float(x) for x in input().strip().split(",")]
    
    [n1,n2]=list(int(x) for x in input().strip().split(","))
    
    temp = list(input().strip().split())
    ladders=[]
    for i in temp:
        x=list(map(int,i.split(',')))
        ladders.append(x)
    
    temp = list(input().strip().split())
    snakes=[]
    for i in temp:
        x=list(map(int,i.split(',')))
        snakes.append(x)
    
    sum_attempts=0
    
    start_ladders = [i[0] for i in ladders]
    end_ladders  = [i[1] for i in ladders]
    snake_tails = [i[1] for i in snakes]
    snake_heads = [i[0] for i in snakes]
    
    for l in range(5000):
        pos=1
        attempts=0
        while(True):
            if(attempts>1000):
                attempts=0
                break
            if(pos in start_ladders):
                pos = end_ladders[start_ladders.index(pos)]
            elif(pos in snake_heads):
                pos = snake_tails[snake_heads.index(pos)]
            else:
                attempts+=1
                value = roll(6,bias_list)
                if(pos+value==100):
                    break
                elif(pos+value<100):
                    pos+=value
                
        sum_attempts+=attempts
    ans=math.ceil(sum_attempts/5000)
    print(ans)
    