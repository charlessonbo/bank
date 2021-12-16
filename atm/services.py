from .models import Balance


def get_balance_by_user(user):
    user_balance = None

    try:
        user_balance = Balance.objects.get(user=user)
    except Balance.DoesNotExist:
        pass

    return user_balance


def create_new_balance_deposit(user, deposit_amount):
    user_balance = Balance(user=user, balance=float(deposit_amount))
    user_balance.save()


def update_balance_by_deposit(user_balance, deposit_amount):
    user_balance.balance = float(user_balance.balance) + float(deposit_amount)
    user_balance.save()


def deposit(user, deposit_amount):
    user_balance = get_balance_by_user(user)

    if not user_balance:
        create_new_balance_deposit(user, deposit_amount)
    else:
        update_balance_by_deposit(user_balance, deposit_amount)


def withdraw_validation(user_balance, withdraw_amount):
    if withdraw_amount <= user_balance.balance:
        return True
    return False


def update_balance_by_withdraw(user_balance, withdraw_amount):
    user_balance.balance = float(user_balance.balance) - float(withdraw_amount)
    user_balance.save()
    return user_balance.balance


def withdraw(user, withdraw_amount):
    user_balance = get_balance_by_user(user)

    if withdraw_validation(user_balance, withdraw_amount):
        new_balance = update_balance_by_withdraw(user_balance, withdraw_amount)
        return f'successful transaction. new balance is {new_balance}'

    return 'insufficient balance.'


def count_bill_in_withdraw_amount(withdraw_amount, amount):
    count = 0
    
    while withdraw_amount >= amount:
        count += 1
        withdraw_amount -= amount
        
    return [count, withdraw_amount]


def break_down_of_bills(withdraw_amount):
    count_bill_per_amount = [
      {'count':0, 'amount':1000}, 
      {'count':0, 'amount':500}, 
      {'count':0, 'amount':200}, 
      {'count':0, 'amount':100}, 
      {'count':0, 'amount':50}, 
      {'count':0, 'amount':20}
    ]

    for value in count_bill_per_amount:
        result = count_bill_in_withdraw_amount(withdraw_amount, value['amount'])
        value['count'] = result[0]
        withdraw_amount = result[1]
    
    if  withdraw_amount > 0:
        return None
    else: 
        return count_bill_per_amount

