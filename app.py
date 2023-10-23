from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Flask!"


app.run(host='0.0.0.0', port=5050, debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5050, debug=True)
