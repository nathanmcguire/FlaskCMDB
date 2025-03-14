# app/models/control_frameworks.py
from app import db
from sqlalchemy import func

class ControlFramework(db.Model):
    __tablename__ = 'control_frameworks'  # Explicitly define the table name
    
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=True)  # Control framework number as a string
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    
    # Use func.now() for both created and updated to automatically set timestamps
    created = db.Column(db.DateTime, default=func.now(), nullable=False)
    updated = db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=False)  # Default func.now()

    def __repr__(self):
        return f'<ControlFramework {self.name}>'