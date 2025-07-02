import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from src.models.user import db
from src.routes.user import user_bp
from src.routes.analysis import analysis_bp

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Configure CORS
CORS(app, origins=os.getenv('CORS_ORIGINS', '*'))

# App configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'asdf#FGSgvasgf$5$WGT')

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(analysis_bp, url_prefix='/api')

# Database configuration - only initialize if DATABASE_URL is properly configured
database_url = os.getenv('DATABASE_URL')
if database_url and database_url.startswith('postgresql') and 'your-db-password' not in database_url:
    # Use PostgreSQL (Supabase) only if properly configured
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully!")
        except Exception as e:
            print(f"Database connection failed: {e}")
            print("Running without database functionality...")
else:
    # Run without database for testing
    print("Running in test mode without database...")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

