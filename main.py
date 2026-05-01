from flask import Flask, send_file, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def motto():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    # Теперь в src мы просто указываем путь /images.png
    return """<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
  </head>
  <body>
    <h1>Жди нас, Марс!</h1>
    <img src="/images.png" alt="Марс">
    <p>Вот она какая, красная планета.</p>
  </body>
</html>"""

@app.route('/images.png')
def get_image():
    return send_file('static/img/images.png')



@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" 
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
          crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    <title>Колонизация</title>
  </head>
  <body>
    <div class="container">
      <h1 class="mt-3">Жди нас, Марс!</h1>

      <img src="{url_for('static', filename='img/images.png')}" alt="Марс" class="img-fluid mt-3 mb-3" style="width: 400px;">

      <div class="alert alert-secondary" role="alert">
        Человечество вырастает из детства.
      </div>
      <div class="alert alert-success" role="alert">
        Человечеству мала одна планета.
      </div>
      <div class="alert alert-secondary" role="alert">
        Мы сделаем обитаемыми безжизненные пока планеты.
      </div>
      <div class="alert alert-warning" role="alert">
        И начнем с Марса!
      </div>
      <div class="alert alert-danger" role="alert">
        Присоединяйся!
      </div>
    </div>
  </body>
</html>'''



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
