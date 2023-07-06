from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database

def connect_to_database():
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Aa@82548254'
    app.config['MYSQL_DB'] = 'zomato'
    app.mysql_connection = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

connect_to_database()



@app.route("/",methods=["GET","POST"])
def greet():
    cursor = app.mysql_connection.cursor()
    name = "aakash"
    insert_query = "INSERT INTO demo (name) VALUES (%s)"
    cursor.execute(insert_query, (name,))
    app.mysql_connection.commit()
    cursor.close()
    return 'User created successfully!'


@app.route("/menu",methods=["GET"])
def read():
    cursor = app.mysql_connection.cursor()
    insert_query = "select * from menus"
    cursor.execute(insert_query)
    data = cursor.fetchall()
    cursor.close()
    return data



@app.route("/menu",methods=["POST"])
def add():
    cursor = app.mysql_connection.cursor()
    image,title,price,available = dict(request.get_json()).values()
    insert_query = f"INSERT INTO menus (image,title,price,available) VALUES ('{image}','{title}','{price}','{available}')"
    cursor.execute(insert_query)
    app.mysql_connection.commit()
    cursor.close()
    return 'Menu created successfully!'



@app.route("/menu/",methods=["PATCH"])
def update():
    cursor = app.mysql_connection.cursor()
    image,title,price,available = dict(request.get_json()).values()
    insert_query = f"UPDATE menus SET image = '{image}',title = '{title}',price = '{price}',available = '{available}' WHERE title = '{title}'"
    cursor.execute(insert_query)
    app.mysql_connection.commit()
    cursor.close()
    return 'Menu updated successfully!'


@app.route("/menu/",methods=["DELETE"])
def delete():
    cursor = app.mysql_connection.cursor()
    image,title,price,available = dict(request.get_json()).values()
    insert_query = f"DELETE from menus WHERE title = '{title}'"
    cursor.execute(insert_query)
    app.mysql_connection.commit()
    cursor.close()
    return 'Menu deleted successfully!'


@app.route("/order",methods=["POST"])
def create_order():
    name,orders = dict(request.get_json()).values()
    # insert_query = f"INSERT INTO orders (name) VALUES ('{name},{orders}')"
    for x in orders:
        cursor = app.mysql_connection.cursor()
        insert_query = f"INSERT INTO orders (name,menuid) VALUES ('{name}','{x}')"
        cursor.execute(insert_query)
        app.mysql_connection.commit()
        cursor.close()
     
    return "Order updated succesfully"


@app.route("/get_orders",methods=["GET"])
def get_orders():
    cursor = app.mysql_connection.cursor()
    query = f"select * from orders as o join menus as m where o.menuid=m.id "
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data




if __name__ == '__main__' :
    app.run(debug=True) 