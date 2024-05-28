import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


titles = Blueprint('titles' , __name__ , url_prefix='/titulos')



@titles.route('/', methods = ['GET','POST'])
def index():

    return "<h3>Legumes Selecionados</h3>"






@titles.route('/listar', methods = ['GET','POST'])
def list():
    

    data = model.get_titles_default()

    return render_template('titles/list.html' , data=data)





@titles.route('/adicionar', methods = ['GET','POST'])
def add():

    
    
    #data = False
    """
    data = model.add_titles_default(usuario_id)
    
    if data:
        return redirect(url_for('titles.list'))
    """

    if request.method == 'POST':
        code = request.form['code']
        quantity = request.form['quantity']
        price = request.form['price']
        person_id = request.form['person_id']

        
        
        
        asd = model.add_title_default(code, quantity,price,person_id)
        if asd:
            return redirect(url_for('titles.list'))
        

    return render_template('titles/add.html')


@titles.route('/ver/<id>', methods = ['GET','POST'])
def view(id):



    data=model.get_title_id(id)
    
    return render_template('titles/view.html' , data=data)
  



@titles.route('/editar/<id>', methods = ['GET','POST'])
def edit(id):

    return render_template('titles/edit.html')







def configure(app):
	app.register_blueprint(titles)






