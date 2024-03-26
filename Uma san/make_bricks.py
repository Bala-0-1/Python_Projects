def make_bricks(small, big, goal):
    remaining_length = goal - min(goal // 5, big) * 5
    if remaining_length <= small:
        return True
    else:
        return False
print(make_bricks(3,1,8))
print(make_bricks(3,2,9))
print(make_bricks(3,2,10))