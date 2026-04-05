from flask import Flask, render_template#The end is what lets you serve HTML files from tempplates
import os
app = Flask(__name__)   #Creates flask instance and tells flask where to look for your html files

@app.route('/') #Route it tells flask to run the function below when someone visits the homepage
def home():
    return render_template('index.html')#returns the file index.html from template folder

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Gallery')
def Gallery():
    return render_template('Gallery.html')

@app.route('/Gallery/snake1em')
def snake1em():
    return render_template('snake1em.html')

@app.route('/Gallery/snake2em')
def snake2em():
    return render_template('snake2em.html')

@app.route('/Gallery/PinProj')
def PenProj():
    return render_template('PinProj.html')

@app.route('/Gallery/Movieposter')
def Movieposter():
    return render_template('Movieposter.html')

@app.route('/Gallery/Lightbulb')
def Lightbulb():
    return render_template('Lightbulb.html')

@app.route('/Gallery/sketches50')
def sketches50():
    return render_template('sketches50.html')

@app.route('/Gallery/Swirl')
def Swirl():
    return render_template('Swirl.html')

@app.route('/Gallery/Typodesignpos')
def Typodesignpos():
    return render_template('Typodesignpos.html')

@app.route('/Gallery/clairoproj')
def clairoproj():
    return render_template('clairoproj.html')

@app.route('/Gallery/snakeproj')
def snakeproj():
    return render_template('snakeproj.html')

@app.route('/Gallery/bookproj')
def bookproj():
    return render_template('bookproj.html')

@app.route('/Gallery/Motiongraph')
def Motionproj():
    return render_template('motionproj.html')

@app.route('/Gallery/Designhistory')
def Designhistory():
    return render_template('Designhistory.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
