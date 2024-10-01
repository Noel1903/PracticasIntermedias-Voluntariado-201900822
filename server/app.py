from flask import Flask, request, jsonify
from sqlalchemy.orm import Session
from db.db import get_db
from models.models import Clientes, Productos, Ventas, DetalleVentas

app = Flask(__name__)



#rutas de la API
@app.route('/')
def index():
    return "Hola Mundo"


#Rutas de clientes
@app.route('/clientes',methods=['GET'])
def get_clientes():
    db: Session = next(get_db())
    clientes = db.query(Clientes).all()
    db.close()
    arr = []
    for cliente in clientes:
        arr.append({
            'id_cliente':cliente.id_cliente,
            'nombre_cliente':cliente.nombre_cliente,
            'direccion':cliente.direccion,
            'telefono':cliente.telefono
        })
    return jsonify(arr)


@app.route('/clientes',methods=['POST'])
def create_clientes():
    db: Session = next(get_db())
    try:
        data = request.json
        cliente = Clientes(
            id_cliente = data['id_cliente'],
            nombre_cliente = data['nombre_cliente'],
            direccion = data['direccion'],
            telefono = data['telefono']
        )
        db.add(cliente)
        db.commit()
        db.close()
        return jsonify({'message':'Cliente creado correctamente'})
    except Exception as e:
        db.close()
        return jsonify({'error':str(e)})
    
@app.route('/clientes/<int:id_cliente>',methods=['DELETE'])
def delete_clientes(id_cliente):
    db: Session = next(get_db())
    try:
        cliente = db.query(Clientes).get(id_cliente)
        if cliente:
            db.delete(cliente)
            db.commit()
            db.close()
            return jsonify({'message':'Cliente eliminado correctamente'})
        else:
            db.close()
            return jsonify({'error':'Cliente no encontrado'})
    except Exception as e:
        db.close()
        return jsonify({'error':str(e)})
    

#Rutas de productos
@app.route('/productos',methods=['GET'])
def get_productos():
    db: Session = next(get_db())
    productos = db.query(Productos).all()
    db.close()
    arr = []
    for producto in productos:
        arr.append({
            'id_producto':producto.id_producto,
            'nombre_producto':producto.nombre_producto,
            'precio':producto.precio,
            'stock':producto.stock
        })
    return jsonify(arr)

@app.route('/productos',methods=['POST'])
def create_productos():
    db: Session = next(get_db())
    try:
        data = request.json
        producto = Productos(
            id_producto = data['id_producto'],
            nombre_producto = data['nombre_producto'],
            precio = data['precio'],
            stock = data['stock']
        )
        db.add(producto)
        db.commit()
        db.close()
        return jsonify({'message':'Producto creado correctamente'})
    except Exception as e:
        db.close()
        return jsonify({'error':str(e)})
    
@app.route('/productos/<int:id_producto>',methods=['DELETE'])
def delete_productos(id_producto):
    db: Session = next(get_db())
    try:
        producto = db.query(Productos).get(id_producto)
        if producto:
            db.delete(producto)
            db.commit()
            db.close()
            return jsonify({'message':'Producto eliminado correctamente'})
        else:
            db.close()
            return jsonify({'error':'Producto no encontrado'})
    except Exception as e:
        db.close()
        return jsonify({'error':str(e)})
    

#Rutas de ventas
@app.route('/ventas',methods=['GET'])
def get_ventas():
    db: Session = next(get_db())
    ventas = db.query(Ventas).all()
    db.close()
    arr = []
    for venta in ventas:
        arr.append({
            'id_venta':venta.id_venta,
            'id_cliente':venta.id_cliente,
            'fecha_venta':venta.fecha_venta,
            'total_venta':venta.total_venta
        })

    return jsonify(arr)

@app.route('/ventas',methods=['POST'])
def create_ventas():
    db: Session = next(get_db())
    try:
        data = request.json
        venta = Ventas(
            id_cliente = data['id_cliente'],
            fecha_venta = data['fecha_venta'],
            total_venta = data['total_venta']
        )
        db.add(venta)
        db.commit()
        db.close()
        return jsonify({'message':'Venta creada correctamente'})
    except Exception as e:
        db.close()
        return jsonify({'error':str(e)})
    

#Rutas de detalle de ventas
@app.route('/detalle_ventas',methods=['GET'])
def get_detalle_ventas():
    db: Session = next(get_db())
    detalle_ventas = db.query(DetalleVentas).all()
    db.close()
    arr = []
    for detalle_venta in detalle_ventas:
        arr.append({
            'id_detalle':detalle_venta.id_detalle,
            'id_venta':detalle_venta.id_venta,
            'id_producto':detalle_venta.id_producto,
            'cantidad':detalle_venta.cantidad,
            'precio_unitario':detalle_venta.precio_unitario
        })

    return jsonify(arr)

@app.route('/detalle_ventas',methods=['POST'])
def create_detalle_ventas():
    db: Session = next(get_db())
    try:
        data = request.json
        detalle_venta = DetalleVentas(
            id_venta = data['id_venta'],
            id_producto = data['id_producto'],
            cantidad = data['cantidad'],
            precio_unitario = data['precio_unitario']
        )
        db.add(detalle_venta)
        db.commit()
        db.close()
        return jsonify({'message':'Detalle de venta creado correctamente'})
    except Exception as e:
        db.close()
        return jsonify({'error':str(e)})
    
#ver ventas segun un cliente
@app.route('/ventas/<int:id_cliente>',methods=['GET'])
def get_ventas_cliente(id_cliente):
    db: Session = next(get_db())
    ventas = db.query(Ventas).filter(Ventas.id_cliente == id_cliente).all()
    db.close()
    arr = []
    for venta in ventas:
        arr.append({
            'id_venta':venta.id_venta,
            'id_cliente':venta.id_cliente,
            'fecha_venta':venta.fecha_venta,
            'total_venta':venta.total_venta
        })
    return jsonify(arr)

#ver detalle de ventas segun una venta
@app.route('/detalle_ventas/<int:id_venta>',methods=['GET'])
def get_detalle_ventas_venta(id_venta):
    db: Session = next(get_db())
    detalle_ventas = db.query(DetalleVentas).filter(DetalleVentas.id_venta == id_venta).all()
    db.close()
    arr = []
    for detalle_venta in detalle_ventas:
        arr.append({
            'id_detalle':detalle_venta.id_detalle,
            'id_venta':detalle_venta.id_venta,
            'id_producto':detalle_venta.id_producto,
            'cantidad':detalle_venta.cantidad,
            'precio_unitario':detalle_venta.precio_unitario
        })
    return jsonify(arr)





if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')