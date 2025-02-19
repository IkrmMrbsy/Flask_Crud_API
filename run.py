from app import create_app, db
from app.models.database import init_db

app = create_app()

# Membuat tabel saat pertama kali aplikasi dijalankan
with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)
