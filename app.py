from flask import Flask  

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>which dog is cuter...</h1><p>meow meow meow meow meow meow meow</P>"

if __name__ == '__main__':
    app.run(debug=True)