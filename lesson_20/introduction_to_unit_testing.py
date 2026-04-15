def reward_points(coins, carrots, trees):
    if coins > 100 and carrots > 10 and trees > 5:
        return 1000
    elif coins > 50 and carrots > 7 and trees > 3:
        return 750
    else:
        return 10

print (reward_points(150,20,7))
print (reward_points(90,8,4))
print (reward_points(40,5,2))

        


    