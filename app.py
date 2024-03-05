from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<html><head><style>body { color: darkblue; background-color: lightgrey; }</style></head><body><h1>Hello, World!</h1></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
