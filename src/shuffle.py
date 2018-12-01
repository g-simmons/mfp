import json
import random


def data_shuffle():
    with open("users.json", 'r') as f:
        temp = json.load(f)
    f.close()
    users = [temp[user] for user in temp]
    random.shuffle(users)
    with open('users_shuffled.json', 'w') as f:
        json.dump(users, f)

if __name__ == '__main__':
    data_shuffle()
