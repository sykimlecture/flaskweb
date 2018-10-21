from dao import mariadb_conn
from src import cifar10_example
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cnn')
def cnn():
    return render_template('cnn.html')

@app.route('/cifar', methods=["GET", "POST", "PUT", "DELETE"])
def cifar():
    # return "";
    return cifar10_example.get_result()

# schedule 처리 get/post로 접근가능
@app.route("/scheduler", methods=["GET", "POST", "PUT", "DELETE"])
def scheduler():
    # 요청이 get이면
    if request.method == 'GET':
        # fullCalendar 에서 start 와 end 를 yyyy-mm-dd 형식의 parameter 로 넘겨준다.
        start = request.args.get('start')
        end = request.args.get('end')
        # schedulerdao.getScheduler에 start와 end를 Dictoionary형식으로 넘겨준다.
        return mariadb_conn.get_scheduler({'start': start, 'end': end})

    # 요청이 post면
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        title = request.form['title']
        allDay = request.form['allDay']

        # Dictoionary 형식의 schedule 변수를 만든다. 추후 parameter를 받게 수정예정
        schedule = {'title' : title, 'start' : start, 'end' : end, 'allDay' : allDay}
        # schedule을 입력한다.
        return mariadb_conn.set_scheduler(schedule)

    # 요청이 delete면
    if request.method == 'DELETE':
        id = request.form['id']
        return mariadb_conn.del_scheduler(id)

    # 요청이 put이면
    if request.method == 'PUT':
        schedule = request.form
        return mariadb_conn.put_scheduler(schedule)


if __name__ == '__main__':
    app.run(debug=True)

    
# end of file
