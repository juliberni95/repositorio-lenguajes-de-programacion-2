import mysql.connector
#from mysql.connector.errors import Error
from mysql.connector import Error
from tkinter import messagebox
from Modelo.owner import *
from Modelo.location import *
from Modelo.supplier import *
from Modelo.team import *
from Modelo.software import *
from Modelo.part import *


class Dao:
    def __init__(self,db):
        self.db=db
    
    #CRUD Cuentadante
    
    def crear_cuentadante(self,obj:Cuentadante):
        val=(obj.documento,obj.nombres,obj.apellidos,obj.correo,obj.celular)
        insert='insert into cuentadante(documento,nombres,apellidos,correo,celular) values (%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','El cuentadante ha sido almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)
    
    def buscar_cuentadante(self,doc):
        criterio=(doc,)
        select='select * from cuentadante where documento= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_cue= self.db.cursor.fetchone()
            return obj_cue
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def buscar_cuentadante_1(self,nom,ape):
        val=(nom,ape)
        select='select * from cuentadante where nombres= %s and apellidos=%s'
        try:
            self.db.cursor.execute(select,val)
            obj_cue= self.db.cursor.fetchone()
            return obj_cue
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def modificar_cuentadante(self,obj:Cuentadante):
        val=(obj.documento,obj.nombres,obj.apellidos,obj.correo,obj.celular,obj.id)
        update='update cuentadante set documento= %s, nombres= %s, apellidos=%s, correo=%s, celular=%s where id= %s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)
        
    def eliminar_cuentadante(self,obj:Cuentadante):
        mensaje='Esta seguro de eliminar el registro?'
        valor= messagebox.askquestion('Eliminar',mensaje)
        if valor == 'yes':
            delete='delete from cuentadante where id= %s'
            try:
                self.db.cursor.execute(delete,(obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado...')
                return True
            except mysql.connector.Error as e:
                messagebox.showinfo('Eliminar',e)
                return False
    
    #CRUD Ubicacion
    
    def crear_ubicacion(self,obj:Ubicacion):
        val=(obj.nombre,obj.descripcion)
        insert='insert into ubicacion(nombre,descripcion) values (%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','La ubicación de ha almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)
    
    def buscar_ubicacion(self,nom):
        criterio=(nom,)
        select='select * from ubicacion where nombre= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_ubi= self.db.cursor.fetchone()
            return obj_ubi
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def modificar_ubicacion(self,obj:Ubicacion):
        val=(obj.nombre,obj.descripcion,obj.id)
        update='update ubicacion set nombre= %s, descripcion=%s where id= %s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)
        
    def eliminar_ubicacion(self,obj:Ubicacion):
        mensaje='Esta seguro de eliminar el registro?'
        valor= messagebox.askquestion('Eliminar',mensaje)
        if valor == 'yes':
            delete='delete from ubicacion where id= %s'
            try:
                self.db.cursor.execute(delete,(obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado...')
                return True
            except mysql.connector.Error as e:
                messagebox.showinfo('Eliminar',e)
                return False
    
    #CRUD Proveedor
    
    def crear_proveedor(self,obj:Proveedor):
        val=(obj.nit,obj.razon_social,obj.direccion,obj.telefono,obj.email)
        insert='insert into proveedor(nit,razon_social,direccion,telefono,email) values (%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','El proveedor ha sido almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)
    
    def buscar_proveedor(self,nit):
        criterio=(nit,)
        select='select * from proveedor where nit= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_pro= self.db.cursor.fetchone()
            return obj_pro
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
        
    def buscar_proveedor_1(self,rz):
        criterio=(rz,)
        select='select * from proveedor where razon_social= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_pro= self.db.cursor.fetchone()
            return obj_pro
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def modificar_proveedor(self,obj:Proveedor):
        val=(obj.nit,obj.razon_social,obj.direccion,obj.telefono,obj.email,obj.id)
        update='update proveedor set nit= %s, razon_social= %s, direccion=%s, telefono=%s, email=%s where id= %s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)
        
    def eliminar_proveedor(self,obj:Proveedor):
        mensaje='Esta seguro de eliminar el registro?'
        valor= messagebox.askquestion('Eliminar',mensaje)
        if valor == 'yes':
            delete='delete from proveedor where id= %s'
            try:
                self.db.cursor.execute(delete,(obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado...')
                return True
            except mysql.connector.Error as e:
                messagebox.showinfo('Eliminar',e)
                return False
    
    def listar_proveedores(self):
        select='select * from proveedor'
        try:
            self.db.cursor.execute(select)
            proveedores= self.db.cursor.fetchall()
            return proveedores
        except mysql.connector.Error as e:
            messagebox.showwarning('Listar',e)
            return None
    
    def listar_ubicaciones(self):
        select='select * from ubicacion'
        try:
            self.db.cursor.execute(select)
            ubicaciones= self.db.cursor.fetchall()
            return ubicaciones
        except mysql.connector.Error as e:
            messagebox.showwarning('Listar',e)
            return None
    
    def listar_cuentadantes(self):
        select='select * from cuentadante'
        try:
            self.db.cursor.execute(select)
            cuentadantes= self.db.cursor.fetchall()
            return cuentadantes
        except mysql.connector.Error as e:
            messagebox.showwarning('Listar',e)
            return None
    
    #Metodos CRUD de equipo
    def crear_equipo(self, obj:Equipo):
        param=obj.id_cuentadante.split('_')
        cue= self.buscar_cuentadante_1(param[0],param[1])        
        ubi=self.buscar_ubicacion(obj.id_ubicacion)       
        pro=self.buscar_proveedor_1(obj.id_proveedor)        
        val=(obj.serial,obj.marca,obj.modelo,obj.tipo,obj.fecha_compra,obj.garantia,obj.clasificacion,cue[0],ubi[0],pro[0])
        insert='insert into equipo(serial,marca,modelo,tipo,fecha_compra,garantia,clasificacion,cuentadante_id,ubicacion_id,proveedor_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','El equipo ha sido almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)

    def buscar_equipo_serial(self, serial):
        criterio = (str(serial),)
        select = 'select * from equipo where serial = %s'
        try:
            self.db.cursor.execute(select, criterio)
            obj_pro= self.db.cursor.fetchone()
            return obj_pro
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
        
    def listar_equipos(self):
        select = 'select * from equipo'
        try:
            self.db.cursor.execute(select)
            equipos = self.db.cursor.fetchall()
            return equipos
        except mysql.connector.Error as e:
            messagebox.showwarning('Listar',e)
            return None
    
    #Metodos CRUD DE SOFTWARE
    def crear_software(self, obj:Software):
        equipo = self.buscar_equipo_serial(obj.equipoid)
        proveedor = self.buscar_proveedor_1(obj.proveedorid)
          
        val = (obj.nombre, obj.version ,obj.llave_instalacion , obj.cantidad_lincencias, obj.vigencia, equipo[0], proveedor[0])
        insert='insert into software(nombre,version,llave_instalacion,cantidad_lincencias,vigencia,equipoid,proveedorid) values (%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','El Software ha sido almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)

    def buscar_software(self, nombre):
        criterio=(nombre,)
        select='select * from software where nombre = %s'
        try:
            self.db.cursor.execute(select, criterio)
            obj_pro= self.db.cursor.fetchone()
            return obj_pro
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
        
    def buscar_equipo_id(self, id):
        print('id equipo:', id)
        criterio = (id,)
        select = 'select * from equipo where id = %s'
        try:
            print('starting query ...')
            
            self.db.cursor.execute(select, criterio)
            obj_pro = self.db.cursor.fetchone()
            print('equipo:', obj_pro)
            return obj_pro
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
        
    def buscar_proveedor_id(self, id):
        print('id proveedor:', id)
        criterio = (id,)
        select = 'select * from proveedor where id = %s'
        try:
            self.db.cursor.execute(select, criterio)
            obj_pro= self.db.cursor.fetchone()
            return obj_pro
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
        
    def modificar_software(self,obj:Software):
        val = (obj.nombre, obj.version, obj.llave_instalacion, obj.cantidad_lincencias, obj.vigencia, obj.id)
        update='update software set nombre = %s, version = %s, llave_instalacion = %s, cantidad_lincencias = %s, vigencia = %s  where id= %s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)

    def eliminar_software(self, obj:Software):
        mensaje = 'Esta seguro de eliminar el registro?'
        valor = messagebox.askquestion('Eliminar', mensaje)
        if valor == 'yes':
            delete='delete from software where id= %s'
            try:
                self.db.cursor.execute(delete, (obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado...')
                return True
            except mysql.connector.Error as e:
                messagebox.showinfo('Eliminar',e)
                return False
    
    # CRUD PARTE

    def crear_parte(self, obj:Parte):
        equipo = self.buscar_equipo_serial(obj.equipoid)
        proveedor = self.buscar_proveedor_1(obj.proveedorid)
            
        val = (obj.serial, obj.nombre, obj.marca, obj.modelo , obj.descripcion, obj.fechaCompra, obj.garantia, equipo[0], proveedor[0])
        insert='insert into parte(serial,nombre,marca,modelo,descripcion,fechaCompra,garantia,equipoid,proveedorid) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro', 'La Parte ha sido almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)


    def buscar_parte(self, nombre):
        criterio = (nombre,)
        select = 'select * from parte where nombre = %s'
        try:
            self.db.cursor.execute(select, criterio)
            obj_pro= self.db.cursor.fetchone()
            return obj_pro
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
        
    def modificar_parte(self,obj:Parte):
        val = (obj.serial, obj.nombre, obj.marca, obj.modelo, obj.descripcion, obj.fechaCompra, obj.garantia , obj.id)
        update='update parte set serial = %s, nombre = %s, marca = %s, modelo = %s, descripcion = %s, fechaCompra = %s, garantia = %s   where id= %s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)

    def eliminar_parte(self, obj:Parte):
        mensaje = 'Esta seguro de eliminar el registro?'
        valor = messagebox.askquestion('Eliminar', mensaje)
        if valor == 'yes':
            delete='delete from parte where id= %s'
            try:
                self.db.cursor.execute(delete, (obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado...')
                return True
            except mysql.connector.Error as e:
                messagebox.showinfo('Eliminar',e)
                return False