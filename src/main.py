from flask import Flask

version = "1.0.0"
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    print("SHIFT Server " + version)
    app.run(debug=False, host='0.0.0.0')
    