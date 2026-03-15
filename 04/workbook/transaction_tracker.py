# Transaction tracker - workbook chapter 4 p.30


def after_transaction(balance, transaction):
    """Returns the amount of money in an account after a transaction

    Args:
        balance (int): Solde du compte
        transaction (int): montant de la transaction
    """
    if balance + transaction < 0:
        return balance
    else:
        return balance + transaction
