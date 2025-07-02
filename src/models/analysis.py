from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Analysis(db.Model):
    __tablename__ = 'analyses'
    
    id = db.Column(db.Integer, primary_key=True)
    nicho = db.Column(db.String(255), nullable=False)
    produto = db.Column(db.String(255))
    descricao = db.Column(db.Text)
    preco = db.Column(db.Float)
    publico = db.Column(db.String(255))
    concorrentes = db.Column(db.Text)
    dados_adicionais = db.Column(db.Text)
    
    # Analysis results stored as JSON
    avatar_data = db.Column(db.JSON)
    positioning_data = db.Column(db.JSON)
    competition_data = db.Column(db.JSON)
    marketing_data = db.Column(db.JSON)
    metrics_data = db.Column(db.JSON)
    funnel_data = db.Column(db.JSON)
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.String(50), default='completed')  # pending, processing, completed, error
    
    def __init__(self, **kwargs):
        super(Analysis, self).__init__(**kwargs)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nicho': self.nicho,
            'produto': self.produto,
            'descricao': self.descricao,
            'preco': self.preco,
            'publico': self.publico,
            'concorrentes': self.concorrentes,
            'dados_adicionais': self.dados_adicionais,
            'avatar': self.avatar_data,
            'positioning': self.positioning_data,
            'competition': self.competition_data,
            'marketing': self.marketing_data,
            'metrics': self.metrics_data,
            'funnel': self.funnel_data,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'status': self.status
        }
    
    def save_analysis_result(self, analysis_result):
        """Save the complete analysis result to the database"""
        self.avatar_data = analysis_result.get('avatar', {})
        self.positioning_data = analysis_result.get('positioning', {})
        self.competition_data = analysis_result.get('competition', {})
        self.marketing_data = analysis_result.get('marketing', {})
        self.metrics_data = analysis_result.get('metrics', {})
        self.funnel_data = analysis_result.get('funnel', {})
        self.status = 'completed'
        self.updated_at = datetime.utcnow()
        
        db.session.commit()
    
    @classmethod
    def create_from_form_data(cls, form_data):
        """Create a new analysis from form data"""
        analysis = cls(
            nicho=form_data.get('nicho', ''),
            produto=form_data.get('produto', ''),
            descricao=form_data.get('descricao', ''),
            preco=float(form_data.get('preco', 0)) if form_data.get('preco') else None,
            publico=form_data.get('publico', ''),
            concorrentes=form_data.get('concorrentes', ''),
            dados_adicionais=form_data.get('dadosAdicionais', ''),
            status='processing'
        )
        
        db.session.add(analysis)
        db.session.commit()
        
        return analysis
    
    @classmethod
    def get_recent_analyses(cls, limit=10):
        """Get recent analyses"""
        return cls.query.order_by(cls.created_at.desc()).limit(limit).all()
    
    @classmethod
    def get_by_nicho(cls, nicho):
        """Get analyses by niche"""
        return cls.query.filter_by(nicho=nicho).order_by(cls.created_at.desc()).all()

class AnalysisTemplate(db.Model):
    __tablename__ = 'analysis_templates'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    nicho = db.Column(db.String(255), nullable=False)
    template_data = db.Column(db.JSON)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nicho': self.nicho,
            'template_data': self.template_data,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

