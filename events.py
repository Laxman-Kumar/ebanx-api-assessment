def return_response(id_, balance):
    return {
        'id': id_,
        'balance': balance
    }


def is_negative(balance, amount):
    return bool((balance - amount) < 0)


def getCreateAccount(account, destination):
    account[destination] = account.get(destination, 0)
    return account[destination]


def depositArgs(request):
    destination = request['destination']
    amount = request['amount']

    return destination, amount


def withdrawArgs(request):
    origin = request['origin']
    amount = request['amount']

    return origin, amount


def depositMoney(account, destination, amount):
    amount = float(amount)
    prevBalance = getCreateAccount(account, destination)
    newBalance = prevBalance + amount
    account[destination] = newBalance
    response = {
        'destination': return_response(destination, newBalance)
    }
    return response, 201


def withdrawMoney(accounts, origin, amount):
    amount = float(amount)
    try:
        if is_negative(accounts[origin], amount):
            raise ValueError

        accounts[origin] -= amount
        newbalance = accounts[origin]
        status = 201
        response = {
            'origin': return_response(origin, newbalance)
        }
    except (KeyError, ValueError):
        status = 404
        response = '0'

    return response, status


def transferArgs(request):
    destination, amount = depositArgs(request)
    origin, _ = withdrawArgs(request)

    return origin, destination, amount


def transferMoney(account, origin, destination, amount):
    amount = float(amount)
    try:
        if is_negative(account[origin], amount):raise ValueError

        account[origin] -= amount
        destination_balance = getCreateAccount(account, destination)

        account[destination] = destination_balance + amount

        status = 201
        response = {
            'origin': return_response(origin, account[origin]),
            'destination': return_response(destination, account[destination])
        }
    except (KeyError, ValueError):
        status = 404
        response = '0'

    return response, status