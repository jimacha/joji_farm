from app import db, create_app
from models.product import Product

#first product
jamieson_omega = Product(
    name="Potatoes",
    category="Dry",
    m_category="vitamins",
    created_at ='2023-09-06 10:34:23',
    short_description="5/150MG TABS 60'S",
    long_description='',
    image_url="static/img/products/skin care/cleansers/hazellic soap 75mg.jpg",
    price=2169)

#second product
# jamieson_omega_complete = Product(
#     name="Jamieson Metalonin Sleep Spray",
#     category="Vitamins and Supplements",
#     m_category="vitamins",
#     created_at ='2023-09-06 10:34:23',
#     short_description="58ml",
#     long_description='',
#     image_url="static/img/jamieson cold fighter chewable tabs 30's.webp",
#     price=3025)

# #third product
# jamieson_cold_fighter = Product(
#     name="Jamieson Calcium Magnesium +D3",
#     category="Vitamins and Supplements ",
#     m_category="vitamins",
#     created_at ='2023-09-06 10:34:23',
#     short_description="caps 200's",
#     long_description='',
#     image_url="static/img/jamieson cold fighter chewable tabs 30's.webp",
#     price=1710)

# #fourth product
# jamieson_metalonin = Product(
#     name="amieson Calcium Magnesium + Zink",
#     category="Vitamins and Supplements",
#     m_category="vitamins",
#     created_at ='2023-09-06 10:34:23',
#     short_description="Caplets 200's ",
#     long_description='',
#     image_url="static/img/jamieson cold fighter chewable tabs 30's.webp",
#     price=2667)



app = create_app()
with app.app_context():
    db.session.add(jamieson_omega)
    # db.session.add(jamieson_metalonin)
    # db.session.add(jamieson_cold_fighter)
    # db.session.add(jamieson_omega_complete)
    db.session.commit()
# app.run(debug=True)

