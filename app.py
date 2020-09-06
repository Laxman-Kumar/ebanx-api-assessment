from flask import Flask, request
import events
app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=8000)