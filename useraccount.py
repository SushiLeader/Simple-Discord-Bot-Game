import json
import time
import random


def register_account(user):
    with open("datas.json", "r") as bank:
        users = json.load(bank)

        if str(user) in users:
            return f'You have registered an account before'

    users[str(user)] = {}
    users[str(user)]["wallet"] = 0
    users[str(user)]["register_date"] = time.time()

    with open("datas.json", "w") as bank:
        json.dump(users, bank)
    return 'Your account has been successfully registered!'


def beg_money(user):
    with open("datas.json", "r") as bank:
        users = json.load(bank)
        if str(user) in users:
            got_money = random.randrange(500)
            users[str(user)]["wallet"] = users[str(user)]["wallet"] + got_money
            with open("datas.json", "w") as bank:
                json.dump(users, bank)
                return f'You got {got_money}'

        else:
            return f'Please do /register to register an account before playing!'


def check_balance(user):
    with open("datas.json", "r") as bank:
        users = json.load(bank)
        if str(user) in users:
            return f'You have {users[str(user)]["wallet"]} coins'

        else:
            return f'Please do /register to register an account before playing!'