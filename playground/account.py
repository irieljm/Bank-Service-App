user_data = {'Marie': [1234, 2000], 'Michelle': [2222, 3000], 'Charlotte': [3456, 4000]}

def display_balance(pin, user):
    if pin == user_data[user][0]:
        return 'This is your current amount of money: {}'.format(user_data[user][1])
    else:
        return 'Incorrect PIN!!!'

def withdraw_money(pin, user, amount):
    balance = user_data[user][1]
    if pin == user_data[user][0]:
        if amount <= balance:
            user_data[user][1] = balance - amount
            return 'You just withdrew {}. Your new balance is {}.'.format(amount, balance)
        else:
            return 'You are not allowed to withdraw more money than you have on your account!'
    else:
        return 'Incorrect PIN!!!'

def transfer(pin, sender, receiver,money):
    balance = user_data[sender][1]
    balance -= money
    return 'The amount 300 Euro were transferred to {}. Your current balance is {}.'.format(receiver,balance)