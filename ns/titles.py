import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


titles = Blueprint('titles' , __name__ , url_prefix='/titulos')



@titles.route('/', methods = ['GET','POST'])
def index():

    return "<h3>Legumes Selecionados</h3>"






@titles.route('/listar', methods = ['GET','POST'])
def list():
    

    

    return render_template('titles/list.html')





@titles.route('/adicionar', methods = ['GET','POST'])
def add():

    
    
    #data = False
    data = model.add_titles_default(usuario_id)
    
    if data:
        return redirect(url_for('titles.list'))

    return render_template('titles/add.html')


@titles.route('/ver/<id>', methods = ['GET','POST'])
def view(id):
    
    return render_template('titles/view.html')
  






@titles.route('/editar', methods = ['GET','POST'])
def edit():

    return "<h3>Legumes Selecionados</h3><p>editar</p>"



@titles.route('/apagar', methods = ['GET','POST'])
def delete():

    return "<h3>Legumes Selecionados</h3><p>apagar</p>"




def configure(app):
	app.register_blueprint(titles)






