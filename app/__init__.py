from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    # Configuración de la base de datos SQLite
    app.config['SECRET_KEY'] = 'Medicontrol_Clave_Secreta_2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicontrol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    Bootstrap(app)
    
    # Registrar Blueprints con prefijos
    from .medicos.routes import bp_medicos
    from .pacientes.routes import bp_pacientes
    from .citas.routes import bp_citas
    
    app.register_blueprint(bp_medicos, url_prefix='/medicos')
    app.register_blueprint(bp_pacientes, url_prefix='/pacientes')
    app.register_blueprint(bp_citas, url_prefix='/citas')
    
    # Página de inicio
    @app.route('/')
    def index():
        from flask import render_template
        return render_template('base.html')
    
    return app