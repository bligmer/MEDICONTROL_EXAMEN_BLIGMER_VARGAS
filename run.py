from app import create_app, db
from app.models import Medico, Paciente, Cita

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Medico': Medico, 'Paciente': Paciente, 'Cita': Cita}

if __name__ == '__main__':
    app.run(debug=True)