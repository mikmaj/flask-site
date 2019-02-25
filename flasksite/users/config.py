import os

# Environment variables hold the sensitive data
class Config:
    SECRET_KEY = os.environ.get('FLASKSITE_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FLASKSITE_DB')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
