from flask import Flask, render_template, url_for
from markupsafe import escape

# 从 flask 包导入 Flask 类，通过实例化这个类，创建一个程序对象 app：
app = Flask(__name__)

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

# 注册一个处理函数，这个函数是处理某个请求的处理函数，Flask 官方把它叫做视图函数（view funciton），可以理解为“请求处理函数”。
# “注册”，就是给这个函数戴上一个装饰器帽子。使用 app.route() 装饰器来为这个函数绑定对应的 URL，当用户在浏览器访问这个 URL 的时候，就会触发这个函数，获取返回值，并把返回值显示到浏览器窗口：
# 一个视图函数也可以绑定多个 URL，这通过附加多个装饰器实现
@app.route('/')
def index():
    # 相对于 templates 根目录的文件路径
    return render_template('index.html', name=name, movies=movies)
# 可以把 Web 程序看作是一堆这样的视图函数的集合：编写不同的函数处理对应 URL 的请求。
# 填入 app.route() 装饰器的第一个参数是 URL 规则字符串，这里的 /指的是根地址。
# 我们只需要写出相对地址，主机地址、端口号等都不需要写出。所以说，这里的 / 对应的是主机名后面的路径部分，完整 URL 就是 http://localhost:5000/。如果我们这里定义的 URL 规则是 /hello，那么完整 URL 就是 http://localhost:5000/hello。

# 整个请求的处理过程如下所示：
    # 当用户在浏览器地址栏访问这个地址，在这里即 http://localhost:5000/
    # 服务器解析请求，发现请求 URL 匹配的 URL 规则是 /，因此调用对应的处理函数 hello()
    # 获取 hello() 函数的返回值，处理后返回给客户端（浏览器）
    # 浏览器接受响应，将其显示在窗口上
@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

@app.route('/test')
def test_url_for():
    #  url_for() 函数的用法，传入端点值（视图函数的名称）和参数，它会返回对应的 URL
    print(url_for('static'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'

# TODO:
# https://tutorial.helloflask.com/static/