import model
import titles


from flask import Flask
from flask_bootstrap import Bootstrap4

db = model


app = Flask(__name__)
app.config['TITLE'] = "nilatS - Titulos"
app.secret_key = b'guerra aos senhores'


#admin.configure(app)
#order.configure(app)
titles.configure(app)
db.configure(app)

Bootstrap4(app)