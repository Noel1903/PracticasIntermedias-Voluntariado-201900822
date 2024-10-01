from sqlalchemy import Column, Integer, String, ForeignKey,Date
from models.base import Base

class Clientes(Base):
    __tablename__ = 'clientes'
    id_cliente = Column(Integer, primary_key=True)
    nombre_cliente = Column(String(100), nullable=False)
    direccion = Column(String(100), nullable=True)
    telefono = Column(String(100), nullable=False)

class Productos(Base):
    __tablename__ = 'productos'
    id_producto = Column(Integer, primary_key=True)
    nombre_producto = Column(String(100), nullable=False)
    precio = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

class Ventas(Base):
    __tablename__ = 'ventas'
    id_venta = Column(Integer, primary_key=True,autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'), nullable=False)
    fecha_venta = Column(Date, nullable=False)
    total_venta = Column(Integer, nullable=False)

class DetalleVentas(Base):
    __tablename__ = 'detalle_ventas'
    id_detalle = Column(Integer, primary_key=True, autoincrement=True)
    id_venta = Column(Integer, ForeignKey('ventas.id_venta'), nullable=False)
    id_producto = Column(Integer, ForeignKey('productos.id_producto'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Integer, nullable=False)