from random import shuffle


def get_secret_friend(students):
    result = {}
    friends = list(students)
    shuffle(friends)
    for i in range(len(students)):
        if students[i] == friends[i]:
            friends[i], friends[-1] = friends[-1], friends[i]
        result[students[i]] = friends[i]
    return result
