from flask import Flask, session,request
import random
app = Flask(__name__)

numeroRand = random.randint(1,10)

@app.route("/endevina", methods=['GET', 'POST'])
def result():

    if request.method=="POST":
        numeroN=request.form.get("numero")
        if int(numeroN)== int(numeroRand):
                return "<p>Felicidades, has adivinado el numero aleatorio que es el {}</p>".format(str(numeroRand))
        else:
                return "<p>Has fallado</p>"
    else:
        return '''<form action="/endevina" method="POST">
                
                <label>Escribe un numero del 1 al 10:</label></br>
                <input type="number" name="numero"/><br/><br/>
                <input type="submit" value=Adivinar>
                </form>'''