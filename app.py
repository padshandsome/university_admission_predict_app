from flask import Flask, request, render_template,redirect,url_for

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('recommendation'))
    return render_template('index.html')

@app.route('/recommendation',methods = ['GET','POST'])
def recommendation():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('recommendation.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)