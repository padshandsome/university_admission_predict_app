from flask import Flask, request, render_template, redirect, url_for
from model import model

app = Flask(__name__)
# We need to save the result elsewhere, cannot send the result directly to the route.
chance_of_admit = 0

@app.route('/',methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('predict'))
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return render_template('predict.html')


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
        personal_statement_strength = int(request.values['ps'])
        recommendation_strength=int(request.values['rl'])
        research_original=request.values['research_experience']
        research=-1
        if research_original=='Yes':
            research=1
        else:
            research=0
        
        chance_of_admit = ChoosingProcess(GPA,TOEFL,GRE,research,university_rank,personal_statement_strength,recommendation_strength)
        return render_template('result.html', data = chance_of_admit)


def ChoosingProcess(GPA,TOEFL,GRE,research,university_rank,personal_statement_strength,recommendation_strength):
        #Predict the probability of admit
        model1 = model()
        model1.load_model()
        # no idea why here has eight features
        bias = 1
        chance_of_admit = model1.predict([[GPA,TOEFL,GRE,research,university_rank,personal_statement_strength,recommendation_strength,bias]])
        # chance_of_admit=GPA*10+TOEFL*5+research+university_rank+recommendation_strength
        return format(chance_of_admit[0]*100,'.2f')
                 
if __name__ == '__main__':
    app.run(port=8080, debug=True)