import random
head = 0
tail = 0
sample_space = 0
while sample_space<=10000:
    n = random.random()
    match n:
        case 0.5:
            continue
        case n if n<0.5:
            tail+=1
            sample_space+=1
        case n if n>0.5:
            head+=1
            sample_space+=1
print("Probability of getting heads : ",head/sample_space)
print("Probability of getting tails : ",tail/sample_space)