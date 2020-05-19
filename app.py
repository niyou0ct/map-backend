from flask import Flask
from controller import auth, hoge

app = Flask(__name__)
app.register_blueprint(auth.app, url_prefix='/api')
app.register_blueprint(hoge.app, url_prefix='/api')

if __name__ == '__main__':
  app.run(debug = True)