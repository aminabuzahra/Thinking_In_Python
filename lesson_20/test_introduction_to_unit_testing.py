from introduction_to_unit_testing import reward_points

def test_reward_points():
    if reward_points(150,20,7) == 1000 and reward_points(90,8,4) == 750 and reward_points(40,5,2) == 10:
        return True
    else:
        return False

print ("Tests passed :)" if test_reward_points() else "Tests not passed :(")
