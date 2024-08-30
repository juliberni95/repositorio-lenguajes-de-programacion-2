class Parte:
    def __init__(self, serial, nombre, marca, modelo, descripcion, fechaCompra, garantia, equipoid, proveedorid, id=None):
        self.__serial = serial
        self.__nombre =  nombre
        self.__marca =  marca
        self.__modelo =  modelo
        self.__descripcion = descripcion
        self.__fechaCompra = fechaCompra
        self.__garantia = garantia
        self.__equipoid = equipoid
        self.__proveedorid = proveedorid
        self.__id=id


    @property
    def serial(self):
        return self.__serial
    
    @serial.setter
    def serial(self, serial):
       self.__serial = serial

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
       self.__nombre =  nombre

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
       self.__marca =  marca


    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
       self.__modelo =  modelo


    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion):
       self.__descripcion = descripcion

    @property
    def fechaCompra(self):
        return self.__fechaCompra
    
    @fechaCompra.setter
    def fechaCompra(self, fechaCompra):
       self.__fechaCompra = fechaCompra

    @property
    def garantia(self):
        return self.__garantia
    
    @garantia.setter
    def garantia(self, garantia):
       self.__garantia = garantia

    @property
    def equipoid(self):
        return self.__equipoid
    
    @equipoid.setter
    def equipoid(self, equipoid):
        self.__equipoid = equipoid

    @property
    def proveedorid(self):
        return self.__proveedorid 
    
    @proveedorid.setter
    def proveedorid(self, proveedorid):
        self.__proveedorid = proveedorid

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id