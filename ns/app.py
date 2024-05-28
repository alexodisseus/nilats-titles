import model
import admin
import person
import titles


from flask import Flask
from flask_bootstrap import Bootstrap4

db = model


app = Flask(__name__)
app.config['TITLE'] = "nilatS - Titulos"
app.secret_key = b'guerra aos senhores'

#order.configure(app)

admin.configure(app)
person.configure(app)
titles.configure(app)
db.configure(app)

Bootstrap4(app)