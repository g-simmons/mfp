import csv
import json


def prune():

    with open("mfp-diaries.tsv", "r") as f:
        reader = csv.reader(f, delimiter='\t')
        rows = [row for row in reader]
    f.close()
    print("Size of the database:")
    print(len(rows))
    users = {}
    for row in rows:
        id = row[0]
        date = row[1]
        meals_temp = eval(row[2])
        temp = eval(row[3])
        if len(temp["total"]) == 0 or len(temp["goal"]) == 0:
            continue
        total_temp = temp["total"][0]
        goal_temp = temp["goal"][0]
        if goal_temp["name"] == "Calories" and goal_temp["value"] != 0:
            goal = goal_temp["value"]
        else:
            continue
        if total_temp["name"] == "Calories" and total_temp["value"] >= 100:
            total = total_temp["value"]
        else:
            continue
        if float(goal-total)/goal > 0.2:
            label = 'below'
        elif total > goal:
            label = 'above'
        else:
            label = 'target'
        meals = []
        for meal_temp in meals_temp:
            for dish_temp in meal_temp["dishes"]:
                dish = [dish_temp["name"], int(dish_temp["nutritions"][0]["value"].replace(',', '')),
                        int(dish_temp["nutritions"][1]["value"].replace(',', '')),
                        int(dish_temp["nutritions"][2]["value"].replace(',', '')),
                        int(dish_temp["nutritions"][3]["value"].replace(',', '')),
                        int(dish_temp["nutritions"][4]["value"].replace(',', '')),
                        int(dish_temp["nutritions"][5]["value"].replace(',', ''))]
                meals.append(dish)
        if id in users:
            users[id].append({"meals": meals, "label": label})
        else:
            users[id] = []
            users[id].append({"meals": meals, "label": label})
        #print(meals.keys())
    print(len(users))
    del rows
    nutrition = []
    token_dict = {}
    tokenized_users = {}
    for id in list(users.keys()):
        if len(users[id]) < 30:
            del users[id]
        else:
            count = {"above": 0, "below": 0, "target": 0}
            lst = []
            for pair in users[id]:
                count[pair["label"]] += 1
                for dish in pair["meals"]:
                    nutrition.append({"name": dish[0].replace('-', ' ').replace(',', ' ').replace('/', ' '),
                                      "nutrition": dish[1:]})
                    tokens = dish[0].replace('-', ' ').replace(',', ' ').replace('/', ' ').split(' ')
                    for token in tokens:
                        token = token.strip('_')
                        token = token.lower()
                        if token.isalpha() and len(token) >= 3:
                            if token in token_dict and token not in lst:
                                token_dict[token] += 1
                            elif token not in token_dict:
                                token_dict[token] = 1
                            lst.append(token)
                count[pair["label"]] += 1
            user_label = max(count, key=count.get)
            tokenized_users[id] = {"label": user_label, "tokens": lst}
    print "8829:", tokenized_users["8829"]
    for token in list(token_dict.keys()):
        if token_dict[token] < 500:
            del token_dict[token]
    for id in tokenized_users:
        tokenized_users[id]["tokens"] = [token for token in tokenized_users[id]["tokens"] if token in token_dict]
    print(len(users))
    print(len(token_dict))
    '''
    with open('users.json', 'w') as f:
        json.dump(tokenized_users, f)
    del tokenized_users
    with open('token_dict.json', 'w') as f:
        json.dump(token_dict, f)
    token_list = []
    for token in token_dict:
        token_list.append(token)
    with open('token_list.json', 'w') as f:
        json.dump(token_list, f)
    with open('nutrition.json', 'w') as f:
        json.dump(nutrition, f)
    f.close()
    print(nutrition[0])
    print(nutrition[1])
    '''

if __name__ == '__main__':
    prune()
