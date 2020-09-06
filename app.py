from flask import Flask, request
import events
app = Flask(__name__)

ACCOUNTS_DATA = {}

EVENT_ARGUMENT_TYPES = {
    'deposit': events.depositArgs,
    'withdraw': events.withdrawArgs,
    'transfer': events.transferArgs
}

EVENT_TYPE_FUNCTIONS = {
    'deposit': events.depositMoney,
    'withdraw': events.withdrawMoney,
    'transfer': events.transferMoney
}


@app.route('/reset', methods=['POST'])
def reset():
    global ACCOUNTS_DATA
    res = 'OK'
    status = 200
    ACCOUNTS_DATA = {}
    return res, status


@app.route('/balance', methods=['GET'])
def get_balance():
    account_id = request.args.get('account_id')

    try:
        balance = str(ACCOUNTS_DATA[account_id])
        status = 200
    except KeyError:
        balance = '0'
        status = 404

    return balance, status


@app.route('/event', methods=['POST'])
def get_event():
    global ACCOUNTS_DATA
    request_data = request.get_json(force=True)
    type_ = request_data['type']
    data = EVENT_ARGUMENT_TYPES[type_](request_data)
    response = EVENT_TYPE_FUNCTIONS[type_](ACCOUNTS_DATA, *data)
    return response


if __name__ == '__main__':
    app.run(port=8001)