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


def withdraw(user, withdraw_amount):
    user_balance = get_balance_by_user(user)

    if withdraw_validation(user_balance, withdraw_amount):
        update_balance_by_withdraw(user_balance, withdraw_amount)
        return 'successful transaction.'

    return 'insufficient balance.'
