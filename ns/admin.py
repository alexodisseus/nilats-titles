import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


admin = Blueprint('admin' , __name__ , url_prefix='/')



@admin.route('/', methods = ['GET','POST'])
def index():

    return "<h3>admin</h3>"




@admin.route('/login', methods = ['GET','POST'])
def login():
    
    

    return render_template('admin/add.html')







@admin.route('/painel', methods = ['GET','POST'])
def painel():

    return "<h3>Legumes Selecionados</h3><p>editar</p>"



@admin.route('/logout', methods = ['GET','POST'])
def logout():

    return "<h3>Legumes Selecionados</h3><p>apagar</p>"




def configure(app):
	app.register_blueprint(admin)






