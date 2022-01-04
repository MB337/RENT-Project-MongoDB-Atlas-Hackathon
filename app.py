from flask import Flask, render_template, redirect, request, session, url_for, send_from_directory
from flask_session import Session
import datetime
import pymongo
from bson.objectid import ObjectId
import json
import os

# Flask config
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# MongoDB config
client = pymongo.MongoClient(os.environ['MONGODB_URI'])
db = client.ecommerce
prod_collection = db.products
stats_collection = db.stats
report_collection = db.report


@app.before_first_request
def set_session_var():
    session['cart'] = []
    session['activity'] = []

@app.route('/')
def home():
    cursor = prod_collection
    categories = []
    for product in cursor.find({}):
        if product['category'] not in categories:
            categories.append(product['category'])

    return render_template("home.html.jinja", cursor=cursor, categories=categories)

@app.route('/<id>', methods = ['POST', 'GET'])
def product(id):
    if request.method == "POST":
        cursor = prod_collection
        session['cart'].append(id)
        activity = "You added to cart this item: <b>" + cursor.find({"_id":ObjectId(str(id))})[0]['prodName'] + "</b>\t" + str(datetime.datetime.now().strftime("%H:%M - %y/%m/%d"))
        session['activity'].append(activity)
        return redirect("/my-cart")
    elif request.method == "GET":
        cursor = prod_collection
        activity = "You watched this item: <b>" + cursor.find({"_id":ObjectId(str(id))})[0]['prodName'] + "</b>\t" + str(datetime.datetime.now().strftime("%H:%M - %y/%m/%d"))
        session['activity'].append(activity)
        for props in cursor.find({"_id":ObjectId(str(id))}):
            product_map = {
                "id":id,
                "category":props['category'],
                "prodName":props['prodName'],
                "desc":props['desc'],
                "price":props['price'],
                "image":props['image'],
            }
    return render_template("product.html.jinja", id=id, cursor=cursor, product_map=product_map)

@app.route('/products/<prod>')
def products(prod):
    if prod == "Smartphones Tablets PCs":
        prod = prod.replace(" ", "/")
    cursor = prod_collection
    categories = []
    for product in cursor.find({"category":prod}):
        if product['category'] not in categories:
            categories.append(product['category'])
    return render_template("products.html.jinja", cursor=cursor, categories=categories, prod=prod)


@app.route('/account', methods = ['GET'])
def account():
    activities = [activity for activity in session['activity']]
    return render_template("account.html.jinja", activities=activities)

@app.route('/my-cart', methods = ['POST','GET'])
def cart():
    if request.method == "POST":
        session['cart'] = []
        prods = request.form['ids'].split(" ")
        days = request.form['days']
        prods.pop()
        for prod in prods:
            stats_collection.insert_one({"date":str(datetime.datetime.now().strftime("%H:%M - %y/%m/%d")), "id":prod, "days":days})
            activity = "You purchased this item: <b>" + prod_collection.find_one({"_id":ObjectId(str(prod))})['prodName'] + "</b>\t" + str(datetime.datetime.now().strftime("%H:%M - %y/%m/%d"))
            session['activity'].append(activity)

        return redirect("/my-cart")
    elif request.method == "GET":
        products = []
        sum_of_prices = 0
        if session['cart']:
            cursor = prod_collection 
            for item in session['cart']:
                for props in cursor.find({"_id":ObjectId(str(item))}):
                    sum_of_prices += props['price']
                    product_map = {
                        "id":item,
                        "category":props['category'],
                        "prodName":props['prodName'],
                        "desc":props['desc'],
                        "price":props['price'],
                        "image":props['image'],
                    }
                    products.append(product_map)
    return render_template("cart.html.jinja", products=products, sum_of_prices=sum_of_prices)

@app.route('/admin')
def admin():
    stats = stats_collection.find({})
    reports = report_collection.find({}) 
    sold_items = {}
    c = 0
    for item in stats:
        sold_items[c] = {"date":item['date'], "days":item['days'], "item":prod_collection.find_one({"_id":ObjectId(str(item['id']))}) }
        c+=1
    return render_template("admin.html.jinja", sold_items=sold_items, reports=reports)

@app.route('/admin/add-product', methods = ['POST','GET'])
def addprod():
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render_template("add-product.html.jinja")

@app.route('/admin/modify-product')
def modifyprod():
    all_prods = prod_collection.find({})
    return render_template("modify-products.html.jinja", all_prods=all_prods)

@app.route('/modify/<id>')
def modifyprodid(id):
    prod = prod_collection.find_one({"_id":ObjectId(str(id))})
    return render_template("modify-product.html.jinja", prod=prod)

@app.route('/report', methods = ['POST','GET'])
def report():
    if request.method == "POST":
        prodID = request.form['id']
        prodName = request.form['prodName']
        prodWebsite = request.form['link']
        price = request.form['price']
        report_collection.insert_one({'price':price, 'prodWebsite':prodWebsite, 'prodName':prodName, 'prodID':prodID})
        return redirect("/")
    else:
        return render_template("report.html.jinja")

@app.route('/search/<query>')
def search(query):
    result = prod_collection.aggregate([
    {
        '$search': {
        'index': 'default',
        'text': {
            'query': query,
            'path': {
            'wildcard': '*'
            }
        }
        }
    }
    ])
    results = []
    for i in result:
        results.append(i)
    return render_template("search.html.jinja", results=results)

# API
@app.route('/api/add-product', methods = ['POST'])
def add_prod_to_db():
    product = json.loads((request.data).decode('utf-8'))
    prod_collection.insert_one(product)
    return {"success":"true"}

@app.route('/api/delete-cart/<id>', methods = ['POST'])
def delete_cart(id):
    session['cart'].remove(id)
    return redirect("/my-cart")

@app.route('/api/delete-product/<id>', methods = ['POST'])
def delete_product(id):
    prod_collection.delete_one({"_id":ObjectId(str(id))})
    print(id)
    return redirect("/admin")

@app.route('/api/modify-product/<id>', methods = ['POST'])
def modifyproductbyid(id):
    updates = { "$set":{
            "prodName":request.form['name'],
            "category":request.form['category'],
            "desc":request.form['description'],
            "price":request.form['price'],
        }
    }
    prod_collection.update_one({"_id":ObjectId(str(id))}, updates)
    return redirect("/admin")

@app.route('/api/chartdata', methods = ['GET'])
def chartdata():
    data = stats_collection.find({})
    chart_data = {'x_values': [], 'y_values':[]}
    for x in data:
        item = prod_collection.find_one({"_id":ObjectId(str(x['id']))})
        chart_data['x_values'] += [(x['date']).split("-")[1]]
        chart_data['y_values'] += [item['price'] * float(x['days'])]
    return chart_data

if __name__ == '__main__':
    app.run(debug=True)
