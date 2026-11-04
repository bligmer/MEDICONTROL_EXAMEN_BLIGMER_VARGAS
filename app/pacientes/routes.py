from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Paciente

bp_pacientes = Blueprint('pacientes', __name__)

@bp_pacientes.route('/')
def listar():
    pacientes = Paciente.query.all()
    return render_template('pacientes/listar.html', pacientes=pacientes)

@bp_pacientes.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        pac = Paciente(
            nombre=request.form['nombre'],
            telefono=request.form['telefono']
        )
        db.session.add(pac)
        db.session.commit()
        return redirect(url_for('pacientes.listar'))
    return render_template('pacientes/agregar.html')

@bp_pacientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    pac = Paciente.query.get_or_404(id)
    if request.method == 'POST':
        pac.nombre = request.form['nombre']
        pac.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('pacientes.listar'))
    return render_template('pacientes/editar.html', paciente=pac)

@bp_pacientes.route('/eliminar/<int:id>')
def eliminar(id):
    pac = Paciente.query.get_or_404(id)
    db.session.delete(pac)
    db.session.commit()
    return redirect(url_for('pacientes.listar'))