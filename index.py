from flask import Flask, jsonify, request
import base64
# from scraping import *
import json
import requests

app = Flask("__name__")

# import scraping as fl


@app.route('/ping/<string:url>')
def pingg(url):
    v = url
    url_api1 = 'https://api.cuevana3.io/uptobox/api.php'
    myobj = {'h': v}
    x = requests.post(url_api1, data = myobj).text
    xx = json.loads(x)
    # print(data)
    return jsonify({"message": xx})


@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's List"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product["name"] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "product not found!"})


@app.route('/products', methods=["POST"])
def addProduct():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def editPoduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json["name"]
        productFound[0]['price'] = request.json["price"]
        productFound[0]["quantity"] = request.json["quantity"]
        
        return jsonify({
            "message": "Product Update!",
            "product": productFound[0]
        })
    return jsonify({"message": "Product No Found"})


@app.route('/products/<string:product_name>', methods=["DELETE"])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({"message": "Product Deleted", "product": products})
    return jsonify({"message": "Product No Found!"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)