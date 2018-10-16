from flask import Flask, render_template

# Flask的Web Server启动时候有一些参数是可以配置的，我们可以在app.run中传入这些参数，
# 假如我们不想改代码，只想在命令行执行的时候指定这些参数呢？
# 该部分会介绍如何使用Flask-Script用于加强命令行的功能，使命令行能携带参数。
# from flask.ext.script import Manager

from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

# app控制权交给manager
# manager = Manager(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/user/<name>')
def user(name):
  return render_template('user.html',name=name)

@app.route('/extends')
def extends():
  return render_template('child.html')

@app.route('/bootstrap/<name>')
def bootstrap(name):
  return render_template('bootstrap.html',name=name)

if __name__ == '__main__':
  app.run(debug=True)
  # manager.run()
  # 从命令行启动的时候可以加入参数{shell, runserver}
  # eg. (env)-->app.py runserver --host 0.0.0.0 修改host地址
  # 更多命令 -->app.py runserver --help
  


