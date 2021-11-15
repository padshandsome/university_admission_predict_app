from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
# We need to save the result elsewhere, cannot send the result directly to the route.
chance_of_admit = 0

@app.route('/',methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('result'))
    return render_template('index.html')

@app.route('/result',methods = ['GET','POST'])
def result():
    # Push the back button
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
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
        
        chance_of_admit = ChoosingProcess(GPA,TOEFL,research,university_rank,recommendation_strength)
        return render_template('result.html', data = chance_of_admit)

@app.route('/login')
def loginpage():
    return render_template("login.html")

def ChoosingProcess(GPA,TOEFL,research,university_rank,recommendation_strength):
        #Predict the probability of admit
        chance_of_admit=GPA*10+TOEFL*5+research+university_rank+recommendation_strength
        return chance_of_admit
                 

if __name__ == '__main__':
    app.run(port=8080, debug=True)