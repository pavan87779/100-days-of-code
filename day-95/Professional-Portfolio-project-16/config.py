import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Using SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STRIPE_PUBLIC_KEY = 'your-stripe-public-key'
    STRIPE_SECRET_KEY = 'your-stripe-secret-key'
