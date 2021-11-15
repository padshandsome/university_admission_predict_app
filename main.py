from flask import Flask, request, render_template,redirect,url_for

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index(b=''):
    if request.method == 'POST':
        return redirect(url_for('recommendation'))
    return render_template('index.html',data=b)

@app.route('/recommendation/<a>',methods = ['GET','POST'])
def recommendation(a):
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('recommendation.html',data=a)
@app.route('/login')
def loginpage():
    return render_template("login.html")

@app.route('/ChoosingProcess',methods=['POST','GET'])
def ChoosingProcess():
    if request.method=='POST':
        
        #Get parameter from user input
        GPA=float(request.values['GPA']) 
        TOEFL=int(request.values['TOEFL']) 
        GRE=int(request.values['GRE']) 
        university_rank=int(request.values['university'])
        recommendation_strength=int(request.values['ps_rl'])
        research_original=request.values['research_experience']
        research=-1
        if research_original=='Yes':
            research=1
        else:
            research=0
        
        #Predict the probability of admit
        chance_of_admit=GPA*10+TOEFL*5+research+university_rank+recommendation_strength
        
        #Return to the recommendation page
        return render_template("recommendation.html",data=chance_of_admit)   
        



if __name__ == '__main__':
    app.run(port=8080, debug=True)