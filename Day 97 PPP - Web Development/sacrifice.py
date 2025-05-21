from app import db, app
from models import Product

with app.app_context():
    db.create_all()
    db.session.add(Product(name="T-Shirt", price=1999, image="", description="Cool shirt!"))
    db.session.add(Product(name="Mug", price=999, image="", description="Nice mug"))
    db.session.commit()
