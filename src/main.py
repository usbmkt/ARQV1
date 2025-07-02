import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
# CORREÇÃO: As importações agora são relativas ao diretório 'src'
from models.user import db
from routes.user import user_bp
from routes.analysis import analysis_bp

# Carrega as variáveis de ambiente
load_dotenv()

# O caminho para a pasta 'static' é ajustado para funcionar corretamente
app = Flask(__name__, static_folder='static')

# Configura o CORS
CORS(app, origins=os.getenv('CORS_ORIGINS', '*'))

# Configuração da aplicação
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'a-default-secret-key-that-should-be-changed')

# Registra os blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(analysis_bp, url_prefix='/api')

# Configuração do banco de dados
database_url = os.getenv('DATABASE_URL')
if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        try:
            db.create_all()
            print("Tabelas do banco de dados verificadas/criadas com sucesso!")
        except Exception as e:
            print(f"Falha na conexão com o banco de dados: {e}")
else:
    print("DATABASE_URL não encontrada. Executando sem funcionalidades de banco de dados.")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
