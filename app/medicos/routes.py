from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Medico

bp_medicos = Blueprint('medicos', __name__)

@bp_medicos.route('/')
def listar():
    medicos = Medico.query.all()
    return render_template('medicos/listar.html', medicos=medicos)

@bp_medicos.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        med = Medico(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad']
        )
        db.session.add(med)
        db.session.commit()
        return redirect(url_for('medicos.listar'))
    return render_template('medicos/agregar.html')

@bp_medicos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    med = Medico.query.get_or_404(id)
    if request.method == 'POST':
        med.nombre = request.form['nombre']
        med.especialidad = request.form['especialidad']
        db.session.commit()
        return redirect(url_for('medicos.listar'))
    return render_template('medicos/editar.html', medico=med)

@bp_medicos.route('/eliminar/<int:id>')
def eliminar(id):
    med = Medico.query.get_or_404(id)
    db.session.delete(med)
    db.session.commit()
    return redirect(url_for('medicos.listar'))