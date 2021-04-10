
from flask import Flask
app= Flask(__name__)


@app.route('/')
def demo_app():
        return '"Hello Airbus"'

if __name__ == '__main__':
   app.run(host= '0.0.0.0',port= '80')

