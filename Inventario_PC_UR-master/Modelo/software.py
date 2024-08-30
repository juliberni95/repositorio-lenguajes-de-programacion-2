class Software: 
    def __init__(self, nom, vers, llave_inst, cantidad_licen, vigencia, equipoid, proveedorid,id=None):
        self.__nombre=nom
        self.__version=vers
        self.__llave_instalacion = llave_inst
        self.__cantidad_lincencias = cantidad_licen
        self.__vigencia = vigencia
        self.__equipoid = equipoid
        self.__proveedorid = proveedorid
        self.__id=id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nom):
        self.__nombre=nom    
    
    @property
    def version(self):
        return self.__version
    
    @version.setter
    def version(self, vers):
        self.__version = vers

    @property
    def llave_instalacion(self):
        return self.__llave_instalacion
    
    @llave_instalacion.setter
    def llave_instalacion(self, llave_ins):
        self.__llave_instalacion = llave_ins

    @property
    def cantidad_lincencias(self):
        return self.__cantidad_lincencias
    
    @cantidad_lincencias.setter
    def cantidad_lincencias(self, cantidad_licen):
        self.__cantidad_lincencias = cantidad_licen


    @property
    def vigencia(self):
        self.__vigencia
    
    @vigencia.setter
    def vigencia(self, vigencia):
        self.__vigencia = vigencia

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
    def id(self,id):
        self.__id= id