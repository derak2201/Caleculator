from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home_page.html')
@app.route('/execution',methods=['POST'])
def caleculate():
    if request.method =='POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        opt = request.form['operation']
        if opt =='add':
            res = num1+num2
        elif opt =='sub':
            res = num1-num2
        return render_template('output.html',results=res)

if __name__ == '__main__':
    app.run(debug=True)