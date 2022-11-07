import topcv
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/my-link')
def my_link():
   topcv.topcvTotal("ha noi", "reactjs")
   return render_template('index.html')
   

if __name__ == '__main__':
   app.run(debug = True)