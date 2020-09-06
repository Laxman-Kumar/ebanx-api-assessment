def depositArgs(request):
    destination = request['destination']
    amount = request['amount']

    return destination, amount


def depositMoney(account, destination, amount):
    amount = float(amount)
    account[destination] = account.get(destination, 0)
    preBalance = account[destination]
    newBalance = preBalance + amount
    account[destination] = newBalance
    response = {
        'destination': {'id': destination,'balance': newBalance}
    }
    return response, 201

