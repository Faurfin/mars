import os
from flask import Flask, send_file, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'POST':
        nickname = request.form.get('name', 'Незнакомец')

        return redirect(f'/results/{nickname}/1/99.9')

    return f'''<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <title>Отбор астронавтов</title>
  </head>
  <body>
    <h2 class="text-center mt-3">Анкета претендента</h2>
    <h4 class="text-center">на участие в миссии</h4>
    <div class="container mt-4" style="max-width: 500px; background-color: #fcdcb6; padding: 20px; border-radius: 5px; border: 1px solid #e0c2a0;">
        <form method="post">
            <div class="mb-3">
                <input type="text" class="form-control" placeholder="Введите фамилию" name="surname">
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" placeholder="Введите имя" name="name">
            </div>
            <div class="mb-3">
                <input type="email" class="form-control" placeholder="Введите адрес почты" name="email">
            </div>

            <div class="mb-3">
                <label>Какое у Вас образование?</label>
                <select class="form-select" name="education">
                    <option>Начальное</option>
                    <option>Среднее</option>
                    <option>Высшее</option>
                </select>
            </div>

            <div class="mb-3">
                <label>Какие у Вас есть профессии?</label>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="prof" value="1">
                    <label class="form-check-label">Инженер-исследователь</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="prof" value="2">
                    <label class="form-check-label">Инженер-строитель</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="prof" value="3">
                    <label class="form-check-label">Пилот</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="prof" value="4">
                    <label class="form-check-label">Метеоролог</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="prof" value="5">
                    <label class="form-check-label">Инженер по жизнеобеспечению</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="prof" value="6">
                    <label class="form-check-label">Инженер по радиационной защите</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="prof" value="7">
                    <label class="form-check-label">Врач</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="prof" value="8">
                    <label class="form-check-label">Экзобиолог</label>
                </div>
            </div>

            <div class="mb-3">
                <label>Укажите пол</label>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                    <label class="form-check-label" for="male">Мужской</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                    <label class="form-check-label" for="female">Женский</label>
                </div>
            </div>

            <div class="mb-3">
                <label>Почему Вы хотите принять участие в миссии?</label>
                <textarea class="form-control" name="motivation" rows="3"></textarea>
            </div>

            <div class="mb-3">
                <label class="form-label d-block">Приложите фотографию</label>
                <input type="file" class="form-control-file" name="photo">
            </div>

            <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="stay" name="stay">
                <label class="form-check-label" for="stay">Готовы остаться на Марсе?</label>
            </div>

            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
    </div>
  </body>
</html>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <title>Варианты выбора</title>
  </head>
  <body>
    <div class="container mt-3">
      <h1>Мое предложение: {planet_name}</h1>
      <h2>Эта планета близка к Земле;</h2>

      <div class="alert alert-success" role="alert">
        <h3>На ней много необходимых ресурсов;</h3>
      </div>

      <div class="alert alert-secondary" role="alert">
        <h4>На ней есть вода и атмосфера;</h4>
      </div>

      <div class="alert alert-warning" role="alert">
        <h5>На ней есть небольшое магнитное поле;</h5>
      </div>

      <div class="alert alert-danger" role="alert">
        <h6>Наконец, она просто красива!</h6>
      </div>
    </div>
  </body>
</html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <title>Результаты</title>
  </head>
  <body>
    <div class="container mt-3">
      <h1>Результаты отбора</h1>
      <h2>Претендента на участие в миссии {nickname}:</h2>

      <div class="alert alert-success" role="alert">
        <h4>Поздравляем! Ваш рейтинг после {level} этапа отбора</h4>
      </div>

      <h3>составляет {rating}!</h3>

      <div class="alert alert-warning" role="alert">
        <h3>Желаем удачи!</h3>
      </div>
    </div>
  </body>
</html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    upload_folder = 'static/img'

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, 'uploaded_photo.png')

    if request.method == 'POST':
        f = request.files.get('file')
        if f:
            f.save(file_path)

    img_tag = ""
    if os.path.exists(file_path):
        img_tag = f'<img src="{url_for("static", filename="img/uploaded_photo.png")}" class="img-fluid mt-3" alt="Фотография">'

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
    <title>Отбор астронавтов</title>
  </head>
  <body>
    <h2 class="text-center mt-3">Загрузка фотографии</h2>
    <h4 class="text-center">для участия в миссии</h4>

    <div class="container mt-4" style="max-width: 500px; background-color: #fcdcb6; padding: 20px; border-radius: 5px; border: 1px solid #e0c2a0;">
        <form method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label class="form-label d-block">Приложите фотографию</label>
                <input type="file" class="form-control-file" name="file">
            </div>

            {img_tag}

            <div class="mt-3">
                <button type="submit" class="btn btn-primary">Отправить</button>
            </div>
        </form>
    </div>
  </body>
</html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Пейзажи Марса</title>
  </head>
  <body>
    <div class="container mt-5" style="max-width: 800px;">
        <h1 class="text-center mb-4">Пейзажи Марса</h1>

        <div id="marsCarousel" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">

            <div class="carousel-item active">
              <img src="{url_for('static', filename='img/mars1.jpg')}" class="d-block w-100" alt="Марс 1">
            </div>

            <div class="carousel-item">
              <img src="{url_for('static', filename='img/mars2.jpg')}" class="d-block w-100" alt="Марс 2">
            </div>

            <div class="carousel-item">
              <img src="{url_for('static', filename='img/mars3.jpg')}" class="d-block w-100" alt="Марс 3">
            </div>

          </div>

          <button class="carousel-control-prev" type="button" data-bs-target="#marsCarousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Предыдущий</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#marsCarousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Следующий</span>
          </button>
        </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
</html>'''
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
