from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home")
def home():
    return render_template('main.html')


@app.route("/Games")
def games():
    return render_template('Games.html')


@app.route("/Champ")
def champ():
    return render_template('Champ.html')

@app.route("/Clothes")
def clothes():
    return render_template('clothesl.html')

@app.route("/Fortnite Champ")
def fortnite_champ():
    return render_template('champ_fortnite.html')

@app.route("/Minecraft Champ")
def minecraft_champ():
    return render_template('champ_mimecraft.html')

if __name__ == '__main__':
    app.run(debug=True)
