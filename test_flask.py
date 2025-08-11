from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print("✅ This print should appear in CMD")
    return "Hello, Flask!"

@app.route('/error')
def error():
    print("🔥 About to raise an exception")
    raise Exception("💥 Crash test")

if __name__ == '__main__':
    app.run(debug=True)
