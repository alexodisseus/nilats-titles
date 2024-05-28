import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


person = Blueprint('person' , __name__ , url_prefix='/cotistas')



@person.route('/', methods = ['GET','POST'])
def index():

    return "<h3>Legumes Selecionados</h3>"



@person.route('/listar', methods = ['GET','POST'])
def list():
    
    data = model.get_person_default()

    return render_template('person/list.html', data=data)


@person.route('/adicionar', methods = ['GET','POST'])
def add():
    
    
    if request.method == 'POST':
        name = request.form['name']
        doc = request.form['doc']
        doc_number = request.form['doc_number']
        adress = request.form['adress']
        contact = request.form['contact']

        
        asd = model.add_person_default(name ,doc, doc_number, adress , contact)
        if asd:
            return redirect(url_for('person.list'))
        


    return render_template('person/add.html')


@person.route('/ver/<id>', methods = ['GET','POST'])
def view(id):
    
    return render_template('person/view.html')
  






@person.route('/editar', methods = ['GET','POST'])
def edit():

    return "<h3>Legumes Selecionados</h3><p>editar</p>"



@person.route('/apagar', methods = ['GET','POST'])
def delete():

    return "<h3>Legumes Selecionados</h3><p>apagar</p>"




def configure(app):
	app.register_blueprint(person)






