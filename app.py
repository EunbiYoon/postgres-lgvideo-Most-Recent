# CREATE TABLE surveytab3 (
# 	id serial PRIMARY KEY,
# 	product VARCHAR ( 200 ) NOT NULL,
# 	dealer VARCHAR ( 200 ) NOT NULL,
# 	rating INTEGER NOT NULL,
# 	review TEXT NULL
# );

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Ella135!@localhost/surveydb'
db = SQLAlchemy(app)

class addsurvey(db.Model):
    __tablename__ = 'surveytab3'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(200))
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    review = db.Column(db.Text())

    def __init__(self, product, dealer, rating, review):
        self.product = product
        self.dealer = dealer
        self.rating = rating
        self.review = review

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    product = request.form['product']
    dealer = request.form['dealer']
    rating = request.form['rating']
    review = request.form['review']
    print(product, dealer, rating, review)
    
    data = addsurvey(product, dealer, rating, review)
    db.session.add(data)
    db.session.commit()
    return render_template('success.html')

# top loader template render
@app.route('/topnoise', methods=['POST'])
def topnoise():
    return render_template('tl/noise.html') # do something

@app.route('/topcloth', methods=['POST'])
def topcloth():  
    return render_template('tl/clothing.html') # do something

@app.route('/topcycle', methods=['POST'])
def topcycle():         
    return render_template('tl/cycle.html') # do something

@app.route('/topleak', methods=['POST'])
def topleak():  
    return render_template('tl/leak.html') # do something

@app.route('/toperror', methods=['POST'])
def toperror():  
    return render_template('tl/error.html') # do something'

@app.route('/topfill', methods=['POST'])
def topfill():  
    return render_template('tl/filling.html') # do something

@app.route('/topdrain', methods=['POST'])
def topdrain():  
    return render_template('tl/drainage.html') # do something

@app.route('/topdispense', methods=['POST'])
def topdispense():  
    return render_template('tl/dispenser.html') # do something

@app.route('/topdoor', methods=['POST'])
def topdoor():  
    return render_template('tl/door.html') # do something

@app.route('/toppower', methods=['POST'])
def toppower():  
    return render_template('tl/power.html') # do something

@app.route('/topsmell', methods=['POST'])
def topsmell():  
    return render_template('tl/smell.html') # do something

@app.route('/topthinq', methods=['POST'])
def topthinq():      
    return render_template('tl/thinq.html') # do something


#front loader template render
@app.route('/frontnoise', methods=['POST'])
def frontnoise():
    return render_template('fl/noise.html') # do something

@app.route('/frontcloth', methods=['POST'])
def frontcloth():   
    return render_template('fl/clothing.html') # do something

@app.route('/frontcycle', methods=['POST'])
def frontcycle():         
    return render_template('fl/cycle.html') # do something

@app.route('/fronfleak', methods=['POST'])
def fronfleak():  
    return render_template('fl/leak.html') # do something

@app.route('/fronterror', methods=['POST'])
def fronterror():  
    return render_template('fl/error.html') # do something'

@app.route('/frontfill', methods=['POST'])
def frontfill():  
    return render_template('fl/filling.html') # do something

@app.route('/frontdrain', methods=['POST'])
def frontdrain():  
    return render_template('fl/drainage.html') # do something

@app.route('/frontdispense', methods=['POST'])
def frontdispense():  
    return render_template('fl/dispenser.html') # do something

@app.route('/frontdoor', methods=['POST'])
def frontdoor():  
    return render_template('fl/door.html') # do something

@app.route('/frontpower', methods=['POST'])
def frontpower():  
    return render_template('fl/power.html') # do something

@app.route('/frontsmell', methods=['POST'])
def frontsmell():  
    return render_template('fl/smell.html') # do something

@app.route('/frontthinq', methods=['POST'])
def frontthinq():      
    return render_template('fl/thinq.html') # do something

@app.route('/home', methods=['POST'])
def home():      
    return render_template('index.html') # do something


if __name__ == "__main__":
    app.run(debug=True)
