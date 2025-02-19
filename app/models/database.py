from app import db

def init_db():
     """Fungsi untuk membuat tabel di database."""
     from app.models import item #Import Model
     db.create_all()