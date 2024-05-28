import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user



admin = Blueprint('admin' , __name__ , url_prefix='/')





@admin.route('/', methods = ['GET','POST'])
def index():

    return render_template('admin/index.html')




@admin.route('/login', methods = ['GET','POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
       
        asd = model.get_login_default(email,password)
        print(asd)

        if asd:
            login_user(asd)
            return redirect(url_for('person.list'))
        

    
    

    return render_template('admin/login.html')








@admin.route('/painel', methods = ['GET','POST'])
def painel():

    return "<h3>Legumes Selecionados</h3><p>editar</p>"



@admin.route('/logout', methods = ['GET','POST'])
def logout():
           
    return redirect(url_for('admin.index'))

    



def configure(app):
	app.register_blueprint(admin)






