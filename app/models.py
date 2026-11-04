from app import db
from datetime import datetime

class Medico(db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    
    # Relación: un médico tiene muchas citas
    citas = db.relationship('Cita', backref='medico', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Medico {self.nombre}>'

class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    
    # Relación: un paciente tiene muchas citas
    citas = db.relationship('Cita', backref='paciente', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Paciente {self.nombre}>'

class Cita(db.Model):
    __tablename__ = 'cita'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    
    def __repr__(self):
        return f'<Cita: {self.fecha} {self.hora}>'