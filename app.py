from flask import Flask, request
import events
app = Flask(__name__)

ACCOUNTS_DATA = {}


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


if __name__ == '__main__':
    app.run(port=8001)