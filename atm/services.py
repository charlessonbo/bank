from .models import Balance


def get_balance_by_user(user):
    user_balance = None

    try:
        user_balance = Balance.objects.get(user=user)
    except Balance.DoesNotExist:
        pass

    return user_balance


def create_new_balance_deposit(user, balance):
    user_balance = Balance(user=user, balance=float(balance))
    user_balance.save()


def update_balance_by_deposit(user_balance, add_balance):
    user_balance.balance = float(user_balance.balance) + float(add_balance)
    user_balance.save()


def deposit_balance(user, add_balance):
    user_balance = get_balance_by_user(user)

    if not user_balance:
        create_new_balance_deposit(user, add_balance)
        return super().form_valid(form)

    update_balance_by_deposit(user_balance, add_balance)