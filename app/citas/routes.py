from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Cita, Medico, Paciente
from datetime import datetime

bp_citas = Blueprint('citas', __name__)

@bp_citas.route('/')
def listar():
    citas = Cita.query.order_by(Cita.fecha.desc(), Cita.hora.desc()).all()
    return render_template('citas/listar.html', citas=citas)

@bp_citas.route('/agregar', methods=['GET', 'POST'])
def agregar():
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        hora_str = request.form['hora']
        cita = Cita(
            fecha=datetime.strptime(fecha_str, '%Y-%m-%d').date(),
            hora=datetime.strptime(hora_str, '%H:%M').time(),
            medico_id=int(request.form['medico_id']),
            paciente_id=int(request.form['paciente_id'])
        )
        db.session.add(cita)
        db.session.commit()
        return redirect(url_for('citas.listar'))
    return render_template('citas/agregar.html', medicos=medicos, pacientes=pacientes)

@bp_citas.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cita = Cita.query.get_or_404(id)
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    if request.method == 'POST':
        cita.fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d').date()
        cita.hora = datetime.strptime(request.form['hora'], '%H:%M').time()
        cita.medico_id = int(request.form['medico_id'])
        cita.paciente_id = int(request.form['paciente_id'])
        db.session.commit()
        return redirect(url_for('citas.listar'))
    return render_template('citas/editar.html', cita=cita, medicos=medicos, pacientes=pacientes)

@bp_citas.route('/eliminar/<int:id>')
def eliminar(id):
    cita = Cita.query.get_or_404(id)
    db.session.delete(cita)
    db.session.commit()
    return redirect(url_for('citas.listar'))