import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

import pymysql

activeforeground = "green"
activebackground = "dodger blue"
disabledforeground = "red"

def mensaje():
    answer = messagebox.askyesno("Salir", "¿Desesa salir del sistema?, Confirme...")
    if(answer):
    	ventana.destroy()

class appcorpicecream:
    def __init__(self,inicio):
        foreground = "red"
        background = "blue"
        activeforeground = "green"
        activebackground = "dodger blue"
        disabledforeground = "red"
        

      
        self.inicio=inicio
        
        
        self.inicio.geometry("650x400")
        self.inicio.title("Bienvenido")
        self.inicio.config(bg="azure3")

        iniciof=Frame(inicio, width="650", height="850",bd=3,relief="groove")
        iniciof.pack(fill= "y", expand="true")

        imgl=PhotoImage(file="img/FondoP.png")
        Label(inicio, image=imgl).place(x=0,y=0)

  
        Button(text="INICIAR",width="20",height="3",command=self.loginP,overrelief="raised",activeforeground="red", cursor="hand2", relief="groove",bg="orange", borderwidth=3,activebackground=activebackground,disabledforeground=disabledforeground).place(x=250, y=250)


        inicio.mainloop()

    def loginP(self):


        inicio.withdraw()
        global login
        login =Toplevel(inicio)
        login.geometry("350x500")
        login.title("LOGIN")
        login.config(bg="azure3")
   

        global usuario_validar
        global contrasena_validar

        usuario_validar=StringVar()
        contrasena_validar=StringVar()

        loginf=Frame(login, width="450", height="700",bd=3,relief="groove")
        loginf.place(x=15,y=10,width=320,height=450)

        global usuario
        global contrasena

        imglogin=PhotoImage(file="img/lg.png")
        Label(loginf, image=imglogin).place(x=0,y=0)
        
        Label(loginf,text="Usuario: ").place(x=130,y=230)
        usuario=Entry(loginf, textvariable=usuario_validar)
        usuario_validar.trace_add('write', lambda *args: usuario_validar.set(usuario_validar.get().upper()))

        usuario.place(x=100,y=250)

        
        Label(loginf,text="Contraseña: ").place(x=125,y=280)
        contrasena=Entry(loginf, show="*", textvariable=contrasena_validar)
        contrasena.place(x=100,y=300)


        Button(loginf, text="Iniciar Sesión",width="20",height="3",command=self.Validacion_login,overrelief="raised",activeforeground="red", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3,activebackground=activebackground,disabledforeground=disabledforeground).place(x=85,y=340)

        login.mainloop()


    def regis(self):
        bd=pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='corpicecream'
        )
        
        pass_1=contrasena.get()
        pass_2=contrasena2.get()

        pass1=len(pass_1)
        pass2=len(pass_2)
        if pass1!=pass2:
            messagebox.showinfo(message="La contraseña no Coinciden",title="Aviso")            
        else:

            if pass1<=7:
                print(pass1)  
                messagebox.showinfo(message="La contraseña debe ser Mayor a 8 Caracteres",title="Aviso")    
                    
            else:

                fcursor=bd.cursor()
                sql="INSERT INTO administrador(usuario_adm ,password_adm) VALUES ('{0}','{1}')".format(usuario.get(),contrasena.get())
                try:
                    fcursor.execute(sql)
                    bd.commit()
                    messagebox.showinfo(message="Usuario registrado Correctamente",title="Aviso")
                except:
                    bd.rollback()
                    messagebox.showinfo(message="Usuario no registrado",title="Aviso")




        bd.close()

    def Validacion_login(self):
        bd=pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='corpicecream'
        )


        fcursor=bd.cursor()
        fcursor.execute("SELECT  password_adm FROM administrador WHERE usuario_adm='"+usuario_validar.get()+"'and  password_adm='"+contrasena_validar.get()+"'")

        if fcursor.fetchall():
            self.pantalla1P()
            
            
        else:
            
            messagebox.showinfo(title="Inicio de sesión Incorrecto", message="Usuario o Contraseña Incorrecto")

        bd.close()





    
    def pantalla1P(self):
        login.withdraw()
    
        global pantalla1
        self.pantalla1=Toplevel(login)
    # pantalla1=Tk()
        self.pantalla1.geometry("850x500")
        self.pantalla1.title("SISTEMA DE GESTION DE ACTIVOS FIJOS")

        pantalla1frame=Frame(self.pantalla1, width="830", height="850",bd=3,relief="groove")
        pantalla1frame.pack(fill= "y", expand="true")
        fd=PhotoImage(file="img/Fondo.png")
        Label(pantalla1frame, image=fd).place(x=0, y=0)
    
        
        Label(pantalla1frame,text="ELIJA UNA OPCIÓN", font=("Arial",18)).place(x=280, y=20)
        gd=PhotoImage(file="img/GD.png")
        Label(pantalla1frame, image=gd).place(x=25,y=60)
        Button(pantalla1frame,text="Gestion de Datos",width="20",height="3",command=self.GestionDatos,overrelief="raised",activeforeground="red", cursor="hand2", relief="groove",bg="orange", borderwidth=3,activebackground=activebackground,disabledforeground=disabledforeground).place(x=10, y=160)
        ct=PhotoImage(file="img/CT.png")
        Label(pantalla1frame, image=ct).place(x=215,y=60)
        Button(pantalla1frame,text="Control",width="20",height="3",command=self.Control,overrelief="raised",activeforeground="red", cursor="hand2", relief="groove",bg="orange", borderwidth=3,activebackground=activebackground,disabledforeground=disabledforeground).place(x=220, y=160)
        cc=PhotoImage(file="img/CC.png")
        Label(pantalla1frame, image=cc).place(x=425,y=60)
        Button(pantalla1frame,text="Calculo Contable",width="20",height="3",command=self.CalculoContable,overrelief="raised",activeforeground="red", cursor="hand2", relief="groove",bg="orange", borderwidth=3,activebackground=activebackground,disabledforeground=disabledforeground).place(x=420, y=160)
        rp=PhotoImage(file="img/RP.png")
        Label(pantalla1frame, image=rp).place(x=625,y=60)
        Button(pantalla1frame,text="Reportes",width="20",height="3",command=self.Reportes,overrelief="raised",activeforeground="red", cursor="hand2", relief="groove",bg="orange", borderwidth=3,activebackground=activebackground,disabledforeground=disabledforeground).place(x=620, y=160)
        Button(pantalla1frame,text="CERRAR SESIÓN",width="20",height="3",command=self.iniciof5,overrelief="raised",activeforeground="red", cursor="hand2", relief="groove",bg="orange red", borderwidth=3,activebackground=activebackground,disabledforeground=disabledforeground).place(x=320, y=260)
        Button(pantalla1frame, text="Registrar Usuario",width="20",height="3",command=self.registrousu,overrelief="raised",activeforeground="red", cursor="hand2", relief="groove",bg="orange", borderwidth=3,activebackground=activebackground,disabledforeground=disabledforeground).place(x=320, y=360)
        Button(pantalla1frame,text="Salir",width="10",height="1",command=self.pantalla1.destroy,overrelief="raised",activeforeground="red", cursor="hand2", relief="groove",bg="red2", borderwidth=3,activebackground=activebackground,disabledforeground=disabledforeground).place(x=355, y=450)

        self.pantalla1.mainloop()

    def GestionDatos(self):
        self.pantalla1.withdraw()
        global gestiond
        gestiond=Toplevel(self.pantalla1)
        gestiond.geometry("1000x540")
        gestiond.title("GESTION DE DATOS")

        global codificacion
        global cantidad
        global modelo
        global proveedor
        global descripcion
        global vida_util
        global edad_trab
        global porcentaje_residual
        global costo_historico
        global edad_pro
        global fecha_comprad
        global fecha_compram
        global fecha_compraa
        global descripcionaf
        global factura
        global fecha_compradepa
        global fecha_compradepm

        global codificacion_entre
        global cantidad_entre
        global modelo_entre
        global proveedor_entre
        global descripcion_entre
        global vida_util_entre
        global edad_trab_entre
        global porcentaje_residual_entre
        global costo_historico_entre
        global fecha_comprad_entre  
        global fecha_compram_entre
        global fecha_compraa_entre
        global fecha_compra_entre
        global descripcionaf_entre
        global factura_entre
        global fecha_compradepa_entre
        global fecha_compradepm_entre
        global edad_pro_entre
        
        self.codificacion_entre=StringVar()
        self.cantidad_entre=StringVar()
        self.modelo_entre=StringVar()
        self.descripcion_entre=StringVar()
        self.vida_util_entre=StringVar()
        self.edad_trab_entre=StringVar()
        self.porcentaje_residual_entre=StringVar()
        self.costo_historico_entre=StringVar()
        self.edad_pro_entre=StringVar()
        self.fecha_comprad_entre=StringVar()
        self.fecha_compram_entre=StringVar()
        self.fecha_compraa_entre=StringVar()
        self.fecha_compradepa_entre=StringVar()
        self.fecha_compradepm_entre=StringVar()
        self.descripcionaf_entre=StringVar()
        self.factura_entre=StringVar()
        self.proveedor_entre=StringVar()

        
        gestionf=Frame(gestiond, width="650", height="850",bd=3,relief="groove")
        gestionf.pack(fill= "y", expand="true")
        fd=PhotoImage(file="img/Fondo1.png")
        Label(gestionf, image=fd).place(x=0, y=0)

        Label(gestionf,text="Descripcio de Activo Fijo:", font=("Arial",12)).grid(padx=2,pady=2,ipadx=2, row=0,column=3)
        descripcionaf=Entry(gestionf, textvariable=self.descripcionaf_entre)
        self.descripcionaf_entre.trace_add('write', lambda *args: self.descripcionaf_entre.set(self.descripcionaf_entre.get().upper()))

        descripcionaf.grid(padx=2,pady=2,ipadx=2, row=1,column=3) 
        
        Label(gestionf,text="Codificación: ").grid( row=2,column=0)
        codificacion=Entry(gestionf, textvariable=self.codificacion_entre)
        codificacion.grid( row=2,column=1)
        
        Label(gestionf,text="Cantidad: ").grid( row=2,column=2)
        cantidad=Entry(gestionf, textvariable=self.cantidad_entre)
        cantidad.grid( row=2,column=3)

        Label(gestionf,text="Modelo: ").grid( row=2,column=4)
        modelo=Entry(gestionf, textvariable=self.modelo_entre)
        modelo.grid( row=2,column=5)

        
        Label(gestionf,text="").grid( row=3,column=0)

        Label(gestionf,text="Descripción: ").grid( padx=5,pady=5,ipadx=5,row=4,column=1)
        descripcion=Entry(gestionf, textvariable=self.descripcion_entre)
        descripcion.place(x=210,y=90,width=550,height=50)
        Label(gestionf,text="").grid( row=5,column=0)
        Label(gestionf,text="").grid( row=6,column=0)
        

        Label(gestionf,text="Proveedor: ").grid( row=7,column=1)
        proveedor=Entry(gestionf, textvariable=self.proveedor_entre )
        proveedor.grid( row=7,column=2)
        
        Label(gestionf,text="Factura: ").grid( row=7,column=3)
        factura=Entry(gestionf, textvariable=self.factura_entre)
        factura.grid( row=7,column=4)

        
        Label(gestionf,text="").grid( row=8,column=3)
        Label(gestionf,text="BIENES-AUMENTO DE CAPITAL",font=('Helvetica', 12, 'bold')).grid( row=9,column=3)
        Label(gestionf,text="").grid( row=10,column=3)
        Label(gestionf,text="").grid( row=11,column=3)


        Label(gestionf,text="Vida\nutil: ").grid( row=12,column=0)
        vida_util=Entry(gestionf, textvariable=self.vida_util_entre)
        vida_util.grid( row=12,column=1)

        Label(gestionf,text="Edad de\ntrabajo: ").grid( row=12,column=2)
        edad_trab=Entry(gestionf, textvariable=self.edad_trab_entre)
        edad_trab.grid( row=12,column=3)
        

        Label(gestionf,text="Porcentaje \nResidual: ").grid( row=12,column=4)
        porcentaje_residual=Entry(gestionf, textvariable=self.porcentaje_residual_entre)
        porcentaje_residual.grid(padx=20, row=12,column=5)

        Label(gestionf,text="Edad Recidual: ").grid( row=14,column=0)
        edad_pro=Entry(gestionf, textvariable=self.edad_pro_entre)
        edad_pro.grid( padx=20,row=14,column=1)

        Label(gestionf,text="Fecha de Compra: ").grid( row=14,column=2)
        Label(gestionf,text="Año").place( x=400, y=311)
        fecha_compraa=Entry(gestionf, textvariable=self.fecha_compraa_entre)
        fecha_compraa.grid( padx=20,row=14,column=3)
        Label(gestionf,text="Mes").place( x=400, y=330)
        fecha_compram=Entry(gestionf, textvariable=self.fecha_compram_entre)
        fecha_compram.grid( padx=20,row=15,column=3)
        Label(gestionf,text="Dia").place( x=400, y=350)
        fecha_comprad=Entry(gestionf, textvariable=self.fecha_comprad_entre)
        fecha_comprad.grid( padx=20,row=16,column=3)

    
        Label(gestionf,text="Año a Depreciar:  ").grid( row=14,column=4)
        Label(gestionf,text="Año").place( x=740, y=311)
        fecha_compradepa=Entry(gestionf, textvariable=self.fecha_compradepa_entre)
        fecha_compradepa.grid( padx=20,row=14,column=5)
        Label(gestionf,text="Mes").place( x=740, y=331)
        fecha_compradepm=Entry(gestionf, textvariable=self.fecha_compradepm_entre)
        fecha_compradepm.grid( padx=20,row=15,column=5)

        Label(gestionf,text="Costo Historico:").grid( row=15,column=0)
        costo_historico=Entry(gestionf, textvariable=self.costo_historico_entre)
        costo_historico.grid( row=15,column=1)
        
        Label(gestionf,text="").grid( row=17,column=3)
        Label(gestionf,text="").grid( row=18,column=5)

        Button(gestionf,text="LIMPIAR",width="9",height="1",command=self.clear,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).grid( row=19,column=1)
        Button(gestionf,text="MODIFICAR",width="10",height="1",command=self.GestionDatosCrud,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).grid( row=19,column=2)
        Button(gestionf,text="INGRESAR",width="9",height="1",command=self.regisgestiond,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).grid( row=19,column=3)
        Button(gestionf,text="INICIO",width="7",height="1",command=self.iniciof2,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).grid( row=19,column=4)
        Button(gestionf,text="SALIR",width="6",height="1",command=gestiond.destroy,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="red3", borderwidth=3).grid( row=19,column=5)

        
        gestiond.mainloop()

    def regisgestiond(self):
        
        bd=pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='corpicecream'
        )
        


        global mesa
        mesa=float()
        
        if self.descripcion_entre.get() =="EDIFICIOS":
            ch=float(self.costo_historico_entre.get()) 
            pr=float(self.porcentaje_residual_entre.get() )
            fe1= float(self.fecha_compradepa_entre.get() )
            fe2=float(self.fecha_compraa_entre.get())
            fe3=float(self.fecha_compram_entre.get())
            fe4=float(self.fecha_compradepm_entre.get())         
            valorresidual=pr*ch 
            costovigentel=pr-valorresidual
            pd1=(1/(pd/12))     
            mesa=((( (fe1+1)-fe2)*12)-(fe3))-fe5
            dep=(ch*pd1/12)*mesa
            
            z=v+x
        
        if self.edad_pro_entre.get() ==""  or self.fecha_compradepa_entre.get()==""or self.fecha_compraa_entre.get() =="" or self.fecha_compram_entre.get()==""or self.fecha_compradepm_entre.get()=="" or self.costo_historico_entre.get()=="":
            pd=1
            if pd==1:

                pr=float(self.porcentaje_residual_entre.get() )
                fe1= float(self.fecha_compradepa_entre.get() )
                fe2=float(self.fecha_compraa_entre.get())
                fe3=float(self.fecha_compram_entre.get())
                fe4=float(self.fecha_compradepm_entre.get()) 
                ch=float(self.costo_historico_entre.get()) 
                fe5=12-fe4 
                pd1=pr/100
                mesa=((( (fe1+1)-fe2)*12)-(fe3))-fe5
                dep=(ch*pd1/12)*mesa

        else:
            pd=float(self.edad_pro_entre.get())
            fe1= float(self.fecha_compradepa_entre.get() )
            fe2=float(self.fecha_compraa_entre.get())
            fe3=float(self.fecha_compram_entre.get())
            fe4=float(self.fecha_compradepm_entre.get()) 
            ch=float(self.costo_historico_entre.get()) 
            fe5=12-fe4 
            pd1=(1/(pd/12))     
            mesa=((( (fe1+1)-fe2)*12)-(fe3))-fe5
            dep=(ch*pd1/12)*mesa     
                    
            

            
        
        
        
        des1=descripcionaf.get()
        codif=codificacion.get()
           

        
        fcursor=bd.cursor()

        sql="INSERT INTO control(depreciacion,tipo,mes_acumulado,fkcodif_ges) VALUES ('{0}','{1}','{2}','{3}')".format(dep,des1,mesa,codif)
        try:
            fcursor.execute(sql)
            bd.commit()

        except:
            bd.rollback()

        sql="INSERT INTO gestiondatos(nombregru_ges,codif_ges,cantidad_ges,descripcionDelBien_ges,modelo_ges,proveedor_ges,factura_ges,vidaUtil_ges,edad_ges,edadPro_ges,residual_ges,\
        costoHistorico_ges,fechaCompraa_ges,fechaCompram_ges,fechaComprad_ges,fecha_Compradepa_ges,fecha_Compradepm_ges) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}',\
        '{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}')".format(descripcionaf.get(),codificacion.get(),cantidad.get(),descripcion.get(),modelo.get(),proveedor.get(),factura.get(),\
            vida_util.get(),edad_trab.get(),edad_pro.get(),porcentaje_residual.get(),costo_historico.get(),fecha_compraa.get(),fecha_compram.get(),fecha_comprad.get(),\
            fecha_compradepa.get(),fecha_compradepm.get())

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Datos registrados Correctamente",title="Aviso")
        except:
            bd.rollback()
            messagebox.showinfo(message="Datos no registrado",title="Aviso")


            

        bd.close()

    def GestionDatosCrud(self):
        
        
        gestiond.withdraw()
       
        global gestiondcrud
        global inmueblecb
        self.gestiondcrud=Toplevel(gestiond)
        self.gestiondcrud.geometry("1370x700+00+0")
        self.gestiondcrud.title("MODIFICAR DATOS")
        self.gestiondcrud.resizable(False,False)


        
        self.codificacion_entre=StringVar()
        self.cantidad_entre=StringVar()
        self.modelo_entre=StringVar()
        self.descripcion_entre=StringVar()
        self.vida_util_entre=StringVar()
        self.edad_trab_entre=StringVar()
        self.porcentaje_residual_entre=StringVar()
        self.costo_historico_entre=StringVar()
        self.edad_pro_entre=StringVar()
        self.fecha_comprad_entre=StringVar()
        self.fecha_compram_entre=StringVar()
        self.fecha_compraa_entre=StringVar()
        self.fecha_compradepa_entre=StringVar()
        self.fecha_compradepm_entre=StringVar()
        self.descripcionaf_entre=StringVar()
        self.factura_entre=StringVar()
        self.proveedor_entre=StringVar()
        self.buscar_por=StringVar()
        self.buscar_txt=StringVar()

        gestionfcrud=Frame(self.gestiondcrud ,bd=4,relief=RIDGE)
        gestionfcrud.place(x=20,y=20,width=520,height=650)
        fd=PhotoImage(file="img/Fondo2.png")
        Label(gestionfcrud, image=fd).place(x=0, y=0)



        Label(gestionfcrud,text="Descripcio de Activo Fijo:", font=("Arial",12)).grid(row=0,column=0)
        descripcionaf=Entry(gestionfcrud, textvariable=self.descripcionaf_entre)
        self.descripcionaf_entre.trace_add('write', lambda *args: self.descripcionaf_entre.set(self.descripcionaf_entre.get().upper()))
        descripcionaf.grid( row=0,column=1) 
        
        Label(gestionfcrud,text="Codificación: ").grid( row=1,column=0)
        codificacion=Entry(gestionfcrud, textvariable=self.codificacion_entre)
        codificacion.grid( row=1,column=1)
        
        Label(gestionfcrud,text="Cantidad: ").grid( row=2,column=0)
        cantidad=Entry(gestionfcrud, textvariable=self.cantidad_entre)
        cantidad.grid( row=2,column=1)

        Label(gestionfcrud,text="Modelo: ").grid( row=3,column=0)
        modelo=Entry(gestionfcrud, textvariable=self.modelo_entre)
        modelo.grid( row=3,column=1)

        
        Label(gestionfcrud,text="").grid( row=4,column=0)

        Label(gestionfcrud,text="Descripción: ").grid( row=5,column=0)
        descripcion=Entry(gestionfcrud, textvariable=self.descripcion_entre)
        descripcion.place(x=275,y=90,width=125,height=50)
        Label(gestionfcrud,text="").grid( row=6,column=0)

        Label(gestionfcrud,text="Proveedor: ").grid( row=7,column=0)
        proveedor=Entry(gestionfcrud, textvariable=self.proveedor_entre )
        proveedor.grid( row=7,column=1)
        
        Label(gestionfcrud,text="Factura: ").grid( row=8,column=0)
        factura=Entry(gestionfcrud, textvariable=self.factura_entre)
        factura.grid( row=8,column=1)

        
        Label(gestionfcrud,text="").grid( row=9,column=0)
        Label(gestionfcrud,text="BIENES-AUMENTO DE CAPITAL",font=('Helvetica', 12, 'bold')).grid( row=10,column=0)
        Label(gestionfcrud,text="").grid( row=11,column=0)
    


        Label(gestionfcrud,text="Vida\nutil: ").grid( row=12,column=0)
        vida_util=Entry(gestionfcrud, textvariable=self.vida_util_entre)
        vida_util.grid( row=12,column=1)

        Label(gestionfcrud,text="Edad de\ntrabajo: ").grid( row=13,column=0)
        edad_trab=Entry(gestionfcrud, textvariable=self.edad_trab_entre)
        edad_trab.grid( row=13,column=1)
        

        Label(gestionfcrud,text="Porcentaje \nResidual: ").grid( row=14,column=0)
        porcentaje_residual=Entry(gestionfcrud, textvariable=self.porcentaje_residual_entre)
        porcentaje_residual.grid(padx=20, row=14,column=1)

        Label(gestionfcrud,text="Edad Recidual: ").grid( row=15,column=0)
        edad_pro=Entry(gestionfcrud, textvariable=self.edad_pro_entre)
        edad_pro.grid( padx=20,row=15,column=1)

        Label(gestionfcrud,text="Fecha de Compra: ").grid( row=16,column=0)
        Label(gestionfcrud,text="Año").grid( row=17,column=0)
        fecha_compraa=Entry(gestionfcrud, textvariable=self.fecha_compraa_entre)
        fecha_compraa.grid( padx=20,row=17,column=1)
        Label(gestionfcrud,text="Mes").grid( row=18,column=0)
        fecha_compram=Entry(gestionfcrud, textvariable=self.fecha_compram_entre)
        fecha_compram.grid( padx=20,row=18,column=1)
        Label(gestionfcrud,text="Dia").grid( row=19,column=0)
        fecha_comprad=Entry(gestionfcrud, textvariable=self.fecha_comprad_entre)
        fecha_comprad.grid( padx=20,row=19,column=1)

    
        Label(gestionfcrud,text="Año a Depreciar:  ").grid( row=20,column=0)
        Label(gestionfcrud,text="Año").grid( row=21,column=0)
        fecha_compradepa=Entry(gestionfcrud, textvariable=self.fecha_compradepa_entre)
        fecha_compradepa.grid( padx=20,row=21,column=1)
        Label(gestionfcrud,text="Mes").grid( row=22,column=0)
        fecha_compradepm=Entry(gestionfcrud, textvariable=self.fecha_compradepm_entre)
        fecha_compradepm.grid( padx=20,row=22,column=1)

        Label(gestionfcrud,text="Costo Historico:").grid( row=23,column=0)
        costo_historico=Entry(gestionfcrud, textvariable=self.costo_historico_entre)
        costo_historico.grid( row=23,column=1)

        btn_Frame=Frame(gestionfcrud,bd=2,relief=RIDGE)
	    
        btn_Frame.place(x=12,y=580,width=480)


		
        Add_btn=Button(btn_Frame,text="INICIO", width=10, command=self.iniciof4,relief="groove",bg="SteelBlue2")
		
        Add_btn.grid(row=0, column=0, padx=10, pady=10)

		
        Update_btn=Button(btn_Frame, command=self.update_data, text="ACTUALIZAR", width=10, relief="groove",bg="SteelBlue2")
		
        Update_btn.grid(row=0, column=1, padx=10, pady=10)

		
        Delete_btn=Button(btn_Frame,text="BORRAR", width=10, command=self.delete_data,relief="groove",bg="SteelBlue2")
		
        Delete_btn.grid(row=0, column=2, padx=10, pady=10)

		
        Clear_btn=Button(btn_Frame,text="LIMPIAR", width=10, command=self.clear,relief="groove",bg="SteelBlue2")
		
        Clear_btn.grid(row=0, column=3, padx=10, pady=10)


        exit_btn=Button(btn_Frame,text="SALIR", width=7,command= self.gestiondcrud.destroy , bg="red")
        exit_btn.grid(row=0, column=4, padx=10, pady=10)
        

        Label(gestionfcrud,text="").grid( row=24,column=3)
        Detail_Frame=Frame(self.gestiondcrud,bd=4,relief=RIDGE)
        Detail_Frame.place(x=550,y=20,width=800,height=650)

        lbl_search=Label(Detail_Frame,text="Buscar:", font=("Arial",15,"bold"),relief="groove")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        inmueblecb=ttk.Combobox(Detail_Frame,textvariable=self.buscar_por, width=10, font=("Arial",15,"bold"),state='readonly')
        inmueblecb["values"] = ["","TIPO","CODIFICACIÓN","MODELO"]
        inmueblecb.grid(row = 0, column = 3, pady=2)
        inmueblecb.grid(row=0, column=2,padx=20,pady=10)

        txt_search=Entry(Detail_Frame,textvariable=self.buscar_txt, width=20, font=("Arial",11,"bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0,column=3,pady=10,padx=20,sticky="w")

        search_btn=Button(Detail_Frame,text="Buscar", width=7,command=self.buscar, bg="SteelBlue2")
        search_btn.grid(row=0, column=4, padx=10, pady=10)
        


        showall_btn=Button(Detail_Frame, text="Mostrar Todo", font=("Arial", 9) ,width=15,command=self.fetch_data,relief="groove",bg="SteelBlue3")
        showall_btn.grid(row=0, column=5, padx=10, pady=10)

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10,y=70,width=780,height=550)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        self.gescrud_table=ttk.Treeview(Table_Frame,columns=("nombregru_ges","codif_ges","cantidad_ges","modelo_ges","descripcionDelBien_ges","proveedor_ges","factura_ges","vidaUtil_ges","edad_ges","edadPro_ges","residual_ges","fechaCompraa_ges","fechaCompram_ges","fechaComprad_ges","fecha_Compradepa_ges","fecha_Compradepm_ges","costoHistorico_ges"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.gescrud_table.xview)
        scroll_y.config(command=self.gescrud_table.yview)
        self.gescrud_table.heading("nombregru_ges", text="Tipo")
        self.gescrud_table.heading("codif_ges", text="Codificación")
        self.gescrud_table.heading("cantidad_ges", text="Cantidad")
        self.gescrud_table.heading("modelo_ges", text="Modelo")
        self.gescrud_table.heading("descripcionDelBien_ges", text="Descripción")
        self.gescrud_table.heading("proveedor_ges", text="Proveedor")
        self.gescrud_table.heading("factura_ges", text="Factura")
        self.gescrud_table.heading("vidaUtil_ges", text="Vida Util")
        self.gescrud_table.heading("edad_ges", text="Edad")
        self.gescrud_table.heading("edadPro_ges", text="Edad Promedio")
        self.gescrud_table.heading("residual_ges", text="Edada Residual")
        self.gescrud_table.heading("fechaCompraa_ges", text="FCompra_AÑO")
        self.gescrud_table.heading("fechaCompram_ges", text="FCompra_MES")   
        self.gescrud_table.heading("fechaComprad_ges", text="FCompra_DIA")
        self.gescrud_table.heading("fecha_Compradepa_ges", text="FDepreciar_AÑO")
        self.gescrud_table.heading("fecha_Compradepm_ges", text="FDepreciar_MES")
        self.gescrud_table.heading("costoHistorico_ges", text="Costo Historico")     
        self.gescrud_table['show']= 'headings'
        self.gescrud_table.column("nombregru_ges", width=200)
        self.gescrud_table.column("codif_ges", width=100)
        self.gescrud_table.column("cantidad_ges", width=80)
        self.gescrud_table.column("modelo_ges", width=80)        
        self.gescrud_table.column("descripcionDelBien_ges", width=120)
        self.gescrud_table.column("proveedor_ges", width=200)
        self.gescrud_table.column("factura_ges", width=100)
        self.gescrud_table.column("vidaUtil_ges", width=60)
        self.gescrud_table.column("edad_ges", width=20)
        self.gescrud_table.column("edadPro_ges", width=80)
        self.gescrud_table.column("residual_ges", width=90)
        self.gescrud_table.column("fechaCompraa_ges", width=100)
        self.gescrud_table.column("fechaCompram_ges", width=100)
        self.gescrud_table.column("fechaComprad_ges", width=100)
        self.gescrud_table.column("fecha_Compradepa_ges", width=100)
        self.gescrud_table.column("fecha_Compradepm_ges", width=100)
        self.gescrud_table.column("costoHistorico_ges", width=100)

        self.gescrud_table.pack(fill=BOTH,expand=1)

        self.gescrud_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
        self.gestiondcrud.mainloop()

    def fetch_data(self):
        
        bd=pymysql.connect(host="localhost", user="root",password="",database="corpicecream")
        cur=bd.cursor()
        cur.execute("SELECT nombregru_ges,codif_ges,cantidad_ges,modelo_ges,descripcionDelBien_ges,proveedor_ges,factura_ges,vidaUtil_ges,edad_ges,edadPro_ges,residual_ges,fechaCompraa_ges,fechaCompram_ges,fechaComprad_ges,fecha_Compradepa_ges,fecha_Compradepm_ges,costoHistorico_ges FROM gestiondatos  ORDER BY id_ges DESC ")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.gescrud_table.delete(*self.gescrud_table.get_children())
            for row in rows:
                self.gescrud_table.insert('',END,values=row)
            bd.commit()
        
        bd.close()

    def clear(self):
        self.descripcionaf_entre.set("")
        self.codificacion_entre.set("")
        self.cantidad_entre.set("")
        self.modelo_entre.set("")
        self.descripcion_entre.set("")
        self.proveedor_entre.set("")
        self.factura_entre.set("")
        self.vida_util_entre.set("")
        self.edad_trab_entre.set("")
        self.porcentaje_residual_entre.set("")
        self.edad_pro_entre.set("")
        self.fecha_compraa_entre.set("")
        self.fecha_compram_entre.set("")
        self.fecha_comprad_entre.set("")
        self.fecha_compradepa_entre.set("")
        self.fecha_compradepm_entre.set("")
        self.costo_historico_entre.set("")


    def get_cursor(self,ev):
        cursor_row=self.gescrud_table.focus()
        contents=self.gescrud_table.item(cursor_row)
        row=contents['values']
        self.descripcionaf_entre.set(row[0])           
        self.codificacion_entre.set(row[1])
        self.cantidad_entre.set(row[2])
        self.modelo_entre.set(row[3])
        self.descripcion_entre.set(row[4])
        self.proveedor_entre.set(row[5])        
        self.factura_entre.set(row[6])   
        self.vida_util_entre.set(row[7])
        self.edad_trab_entre.set(row[8])
        self.porcentaje_residual_entre.set(row[9])
        self.edad_pro_entre.set(row[10])        
        self.fecha_compraa_entre.set(row[11])
        self.fecha_compram_entre.set(row[12])
        self.fecha_comprad_entre.set(row[13])
        self.fecha_compradepa_entre.set(row[14])
        self.fecha_compradepm_entre.set(row[15])
        self.costo_historico_entre.set(row[16])

    def update_data(self):
        if self.descripcionaf_entre.get()=="":
            messagebox.showerror("Error", "Seleccione el registro a actualizar")
        else:
            bd=pymysql.connect(host="localhost", user="root",password="",database="corpicecream")
            cur=bd.cursor()
            cur.execute("update gestiondatos set nombregru_ges =%s ,cantidad_ges=%s ,modelo_ges=%s ,descripcionDelBien_ges=%s ,proveedor_ges=%s ,factura_ges=%s ,vidaUtil_ges=%s ,edad_ges=%s ,edadPro_ges=%s ,residual_ges=%s ,fechaCompraa_ges=%s ,fechaCompram_ges=%s ,fechaComprad_ges=%s ,fecha_Compradepa_ges=%s ,fecha_Compradepm_ges=%s ,costoHistorico_ges=%s WHERE codif_ges=%s",(

                self.descripcionaf_entre.get(),                
                self.cantidad_entre.get(),
                self.modelo_entre.get(),
                self.descripcion_entre.get(),
                self.proveedor_entre.get(),
                self.factura_entre.get(),                
                self.vida_util_entre.get(),
                self.edad_trab_entre.get(),
                self.porcentaje_residual_entre.get(),
                self.edad_pro_entre.get(),
                self.fecha_compraa_entre.get(),
                self.fecha_compram_entre.get(),
                self.fecha_comprad_entre.get(),
                self.fecha_compradepa_entre.get(),
                self.fecha_compradepm_entre.get(),
                self.costo_historico_entre.get(),
                self.codificacion_entre.get()
                ))
            bd.commit()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Actualizando", "Se actualizó correctamente el registro")
            bd.close()
    def delete_data(self):
        if self.descripcionaf_entre.get()=="":
            messagebox.showerror("Error", "Seleccione el registro a eliminar")
        else:
            bd=pymysql.connect(host="localhost", user="root",password="",database="corpicecream")
            cur=bd.cursor()
            cur.execute("delete from gestiondatos where codif_ges=%s",self.codificacion_entre.get())
            bd.commit()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Eliminar", "Se eliminó correctamente el registro")
            bd.close()

    
    def buscar(self):
        bd=pymysql.connect(host="localhost", user="root",password="",database="corpicecream")
        cur=bd.cursor()
        if self.buscar_por.get()=="TIPO":
            a="nombregru_ges"
            print( a)
            cur.execute("SELECT nombregru_ges,codif_ges,cantidad_ges,modelo_ges,descripcionDelBien_ges,proveedor_ges,factura_ges,vidaUtil_ges,edad_ges,edadPro_ges,residual_ges,fechaCompraa_ges,fechaCompram_ges,fechaComprad_ges,fecha_Compradepa_ges,fecha_Compradepm_ges,costoHistorico_ges FROM gestiondatos  where "+str(a)+" LIKE '%"+str(self.buscar_txt.get())+"%'")
        if self.buscar_por.get()=="CODIFICACIÓN":
            a="codif_ges"
            print( a)
            cur.execute("SELECT nombregru_ges,codif_ges,cantidad_ges,modelo_ges,descripcionDelBien_ges,proveedor_ges,factura_ges,vidaUtil_ges,edad_ges,edadPro_ges,residual_ges,fechaCompraa_ges,fechaCompram_ges,fechaComprad_ges,fecha_Compradepa_ges,fecha_Compradepm_ges,costoHistorico_ges FROM gestiondatos  where "+str(a)+" LIKE '%"+str(self.buscar_txt.get())+"%'")
        if self.buscar_por.get()=="MODELO":
            a="modelo_ges"
            print( a)
            print(self.buscar_txt.get())
            cur.execute("SELECT nombregru_ges,codif_ges,cantidad_ges,descripcionDelBien_ges,modelo_ges,proveedor_ges,factura_ges,vidaUtil_ges,edad_ges,edadPro_ges,residual_ges,fechaCompraa_ges,fechaCompram_ges,fechaComprad_ges,fecha_Compradepa_ges,fecha_Compradepm_ges,costoHistorico_ges FROM gestiondatos  where "+str(a)+" LIKE '%"+str(self.buscar_txt.get())+"%'")

        
        rows=cur.fetchall()
        if len(rows)!=0:
            self.gescrud_table.delete(*self.gescrud_table.get_children())
            for row in rows:
                self.gescrud_table.insert('',END,values=row)
            bd.commit()
        bd.close()	
        
    def Control(self):
        self.pantalla1.withdraw()
        global controlp
        controlp=Toplevel(self.pantalla1)

        global controlf
        global inmueblecbx

        main_frame = Frame(controlp)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas)

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")




        controlp.geometry("900x660")
        controlp.title("CONTROL CONTABLE DE ACTIVOS FIJOS")

        controlf=Frame(my_canvas, width="800", height="700",bd=3,relief="groove")
        controlf.pack()



        Label(controlf,text="Tipo de \nBien Inmueble:", font=("Arial",12)).grid(padx=2,pady=2,ipadx=2, row=0,column=2)
        inmueblecbx=ttk.Combobox(controlf)
        inmueblecbx.grid(padx=2,pady=2,ipadx=2, row=0,column=3) 
        inmueblecbx["values"] = ["TERRENOS","EDIFICIOS","CONSTRUCCIONES EN CURSO","INSTALACIONES","MUEBLES Y ENSERES","MAQUINARIA Y EQUIPO","EQUIPOS DE COMPUTACION",
        "OTRAS PROPIEDADES,PLANTA Y EQUIPO","REPUESTOS Y HERRAMIENTAS","EQUIPO DE OFICINA AF","CONGELADORES AF","ALARMAS AF"]
        inmueblecbx.grid(row = 0, column = 3, pady=2)
        inmueblecbx.current(0)

        
        
        Button(controlf,text="GENERAR",width="9",height="3",command=self.inmueblecbxP,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).grid(padx=2,pady=2,ipadx=2, row=0,column=4)
        Label(controlf,text="CONTROL GENERAL:", font=("Arial",12)).grid(padx=2,pady=2,ipadx=2, row=1,column=2)
        Button(controlf,text="GENERAR",width="9",height="3",command=self.inmuebleGP , overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).grid(padx=2,pady=2,ipadx=2, row=1,column=3)
        botonhome= Button(controlf,text="INICIO",width="7",height="1",command=self.iniciof,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).grid(padx=2,pady=2,ipadx=2, row=1,column=4)

        controlp.mainloop()

    """def controlgeneral(self):


        bd=pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='corpicecream'
        )
        
    
        fcursor=bd.cursor()
        fcursor.execute("SELECT  * FROM gestiondatos")
        row=fcursor.fetchall()

        if len(row)!=0:
            control_table.delete(*control_table.get_children())
            for row in rows:
                control_table.insert('',END,values=row)
            bd.commit()
            
        bd.close()"""
        

    def inmueblecbxP(self):
        bd=pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='corpicecream'
        )
        

        controlf=Frame(controlp, width="760", height="510",bd=3,relief="groove")
        controlf.place(x=100,y=140,width=750,height=500)
    
        Table_frame=Frame(controlf)
        Table_frame.place(x=30,y=70,width=700,height=400)

        scrollx=Scrollbar(Table_frame, orient=HORIZONTAL)
        scrolly=Scrollbar(Table_frame, orient=VERTICAL)  


        control_table=ttk.Treeview(Table_frame,columns=("descripcionaf","costo_historico","depreciacion","edad_pro","porcentaje_residual"),
            xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=control_table.xview)
        scrolly.config(command=control_table.yview)
        control_table.heading("descripcionaf" , text="Tipo")
        control_table.heading("costo_historico",text="Costo Historico")
        control_table.heading("depreciacion",text="Depreciación")
        control_table.heading("porcentaje_residual",text="Edad Residual")
        control_table.heading("edad_pro",text="Meses Aculados")
        control_table['show']='headings'
        
        control_table.column("descripcionaf" ,width=150)
        control_table.column("costo_historico", width=100)
        control_table.column("depreciacion",width=100)
        control_table.column("porcentaje_residual",width=100)
        control_table.column("edad_pro", width=80)
        
        inmueblecbx1=inmueblecbx.get()
        
        fcursor=bd.cursor()
        fcursor.execute("SELECT DISTINCT gestiondatos.nombregru_ges ,gestiondatos.costoHistorico_ges ,control.depreciacion,control.mes_acumulado ,gestiondatos.edadPro_ges FROM gestiondatos INNER JOIN control ON gestiondatos.codif_ges = control.fkcodif_ges WHERE gestiondatos.nombregru_ges=%s ",(inmueblecbx1,) )
        """FROM gestiondatos INNER JOIN control WHERE  gestiondatos.nombregru_ges=%s ",(inmueblecbx1,))    """  
        row=fcursor.fetchall()

        if len(row)!=0:
            control_table.delete(*control_table.get_children())
            for row in row:
                control_table.insert('',END,values=row)
            bd.commit()
            
        bd.close()
        print(inmueblecbx.get())
        control_table.pack(fill=BOTH,expand=1)
        botonimprimir= Button(controlf,text="IMPRIMIR",width="7",height="1",command=self.iniciof1,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2",
        borderwidth=3).place(x=250,y=10)
        Button(controlf,text="SALIR",width="6",height="1",command=controlf.destroy,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="red3",
        borderwidth=3).place(x=450,y=10)
        controlf.mainloop()

    def inmuebleGP(self):

        bd=pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='corpicecream'
        )
        
            
        controlf=Frame(controlp, width="760", height="500",bd=3,relief="groove")
        controlf.place(x=100,y=140,width=750,height=580)
    
    
        Table_frame=Frame(controlf)
        Table_frame.place(x=30,y=70,width=700,height=400)

        scrollx=Scrollbar(Table_frame, orient=HORIZONTAL)
        scrolly=Scrollbar(Table_frame, orient=VERTICAL)

        control_table=ttk.Treeview(Table_frame,columns=("descripcionaf","costo_historico","depreciacion","edad_pro","porcentaje_residual"),
            xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=control_table.xview)
        scrolly.config(command=control_table.yview)
        control_table.heading("descripcionaf" , text="Tipo")
        control_table.heading("costo_historico",text="Costo Historico")
        control_table.heading("depreciacion",text="Depreciación")
        control_table.heading("porcentaje_residual",text="Edad Residual")
        control_table.heading("edad_pro",text="Meses Aculados")
        control_table['show']='headings'
        
        control_table.column("descripcionaf" ,width=150)
        control_table.column("costo_historico", width=100)
        control_table.column("depreciacion",width=100)
        control_table.column("edad_pro",width=100)
        control_table.column("edad_pro", width=100)


        fcursor=bd.cursor()
        fcursor.execute("SELECT DISTINCT gestiondatos.nombregru_ges ,gestiondatos.costoHistorico_ges ,\
            control.depreciacion,control.mes_acumulado ,gestiondatos.edadPro_ges  \
                FROM gestiondatos INNER JOIN control ON gestiondatos.codif_ges = control.fkcodif_ges")

        row=fcursor.fetchall()

        if len(row)!=0:
            control_table.delete(*control_table.get_children())
            for row in row:
                control_table.insert('',END,values=row)
            bd.commit()
            
        bd.close()
        control_table.pack(fill=BOTH,expand=1)
        botonimprimir= Button(controlf,text="IMPRIMIR",width="7",height="1",command=self.iniciof1,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2",
        borderwidth=3).place(x=250,y=10)
        Button(controlf,text="SALIR",width="6",height="1",command=controlf.destroy,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="red3",
        borderwidth=3).place(x=450,y=10)
        controlf.mainloop()
        

    def CalculoContable(self):
        bd=pymysql.connect( host='localhost', user='root', passwd='', db='corpicecream' )
        self.pantalla1.withdraw()
        global ccontable

        self.descripcionaf_entre1=StringVar()
        self.libro_entre=StringVar()
        self.auxiliar_entre=StringVar()

        self.ccontable =Toplevel(self.pantalla1)
        self.ccontable.geometry("1100x540")
        self.ccontable.title("CALCULO CONTABLE")
        self.ccontable.config(bg="azure3")
        calculoCf=Frame(self.ccontable, width="650", height="540",bd=3,relief="groove")

        
        calculoCf=Frame(self.ccontable, width="960", height="540",bd=3,relief="groove")
        calculoCf.pack(fill= "y", expand="true")
    




        calculoCf1=Frame(calculoCf ,bd=4,relief=RIDGE)
        calculoCf1.place(x=10,y=70,width=320,height=650)
        fd=PhotoImage(file="img/Fondo2.png")
        Label(calculoCf1, image=fd).place(x=0, y=0)



        Label(calculoCf1,text="", font=("Arial",20)).grid(row=0,column=3)
        Label(calculoCf1,text="Descripcio de Activo Fijo:", font=("Arial",12)).grid(row=1,column=0)
        descripcionaf=Entry(calculoCf1, textvariable=self.descripcionaf_entre1)
        self.descripcionaf_entre1.trace_add('write', lambda *args: self.descripcionaf_entre1.set(self.descripcionaf_entre1.get().upper()))
        descripcionaf.grid( row=1,column=1) 
        Label(calculoCf1,text="Auxiliar").grid( row=2,column=0)
        libro=Entry(calculoCf1, textvariable=self.auxiliar_entre)
        libro.grid( row=2,column=1)
        Label(calculoCf1,text="Libros").grid( row=3,column=0)
        libro=Entry(calculoCf1, textvariable=self.libro_entre)
        libro.grid( row=3,column=1)
        

        btn_Frame=Frame(calculoCf1,bd=2,relief=RIDGE)
	    
        btn_Frame.place(x=12,y=200,width=480)

        Add_btn=Button(btn_Frame,text="INICIO", width=10, command=self.iniciof4,relief="groove",bg="SteelBlue2")
		
        Add_btn.grid(row=0, column=0, padx=10, pady=10)

		
        Update_btn=Button(btn_Frame, command=self.update_datacontrol, text="ACTUALIZAR", width=10, relief="groove",bg="SteelBlue2")
		
        Update_btn.grid(row=0, column=1, padx=10, pady=10)



		
        Clear_btn=Button(btn_Frame,text="LIMPIAR", width=10, command=self.clearcontrol,relief="groove",bg="SteelBlue2")
		
        Clear_btn.grid(row=1, column=1, padx=10, pady=10)

        Add_btn1=Button(btn_Frame,text="AGREGAR", width=10, command=self.addcc,relief="groove",bg="SteelBlue2")
		
        Add_btn1.grid(row=0, column=3, padx=10, pady=10)

        salir=Button(btn_Frame,text="SALIR",width="6",height="1",command=self.ccontable.destroy ,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="red3",
        borderwidth=3)
        salir.grid(row=1, column=3, padx=10, pady=10)


        Table_frame=Frame(calculoCf)
        Table_frame.place(x=340,y=70,width=550,height=400)

        scrollx=Scrollbar(Table_frame, orient=HORIZONTAL)
        scrolly=Scrollbar(Table_frame, orient=VERTICAL)

        self.control_table=ttk.Treeview(Table_frame,columns=("descripcionaf","auxiliar","libros","diferencia"),
            xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.control_table.xview)
        scrolly.config(command=self.control_table.yview)
        self.control_table.heading("descripcionaf" , text="Tipo de Activo Fijo")
        self.control_table.heading("auxiliar",text="Auxiliar")
        self.control_table.heading("libros",text="Libros")
        self.control_table.heading("diferencia",text="Diferencia")
        self.control_table['show']='headings'
        
        
        self.control_table.column("descripcionaf" ,width=100)
        self.control_table.column("auxiliar", width=100)
        self.control_table.column("libros", width=100)
        self.control_table.column("diferencia", width=100)



        self.control_table.pack(fill=BOTH,expand=1)

        self.control_table.bind("<ButtonRelease-1>", self.get_cursorcontrol)

        self.fetch_datacontrol()


        bd.close()

        """botonhome= Button(calculoCf,text="INICIO",width="7",height="1",command=self.iniciof3,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).grid(padx=2,pady=2,ipadx=2, row=1,column=4)
        botonhome= Button(calculoCf,text="INICIO",width="7",height="1",command=self.iniciof3,overrelief="raised",activeforeground="cyan4", cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).grid(padx=2,pady=2,ipadx=2, row=1,column=4)
        """
        self.ccontable.mainloop()

    def addcc(self):
        if self.descripcionaf_entre1.get()=="":
            messagebox.showerror("Error", "Todos los campos son requeridos!!!")
        
        else:

            con=pymysql.connect(host="localhost", user="root",password="",database="corpicecream")
            cur=con.cursor()
            cur.execute("insert into calculoc (activo,auxiliar,libro)values(%s,%s,%s)",(self.descripcionaf_entre1.get(),self.auxiliar_entre.get(),self.libro_entre.get()))
            con.commit()
            self.fetch_datacontrol()
            self.clearcontrol()
            con.close()
            messagebox.showinfo("Adelante...", "Se agregó correctamente el registro")


    def fetch_datacontrol(self):
        
        
        bd=pymysql.connect(host="localhost", user="root",password="",database="corpicecream")
        cur=bd.cursor()
        cur.execute("SELECT DISTINCT  g.nombregru_ges ,g.costoHistorico_ges,c.libro FROM gestiondatos g, calculoc c  where g.nombregru_ges = c.activo group by nombregru_ges" )
        rows=cur.fetchall()
        if len(rows)!=0:
            self.control_table.delete(*self.control_table.get_children())
            for row in rows:
                self.control_table.insert('',END,values=row)
            bd.commit()
        
        bd.close()


			
    
    def clearcontrol(self):
        self.descripcionaf_entre1.set("")
        self.auxiliar_entre.set("")
        self.libro_entre.set("")
        


    def get_cursorcontrol(self,ev):
        cursor_row=self.control_table.focus()
        contents=self.control_table.item(cursor_row)
        row=contents['values']
        self.descripcionaf_entre1.set(row[0])           
        self.auxiliar_entre.set(row[1])
        self.libro_entre.set(row[2])  
        

    def update_datacontrol(self):
        if self.descripcionaf_entre1.get()=="":
            messagebox.showerror("Error", "Seleccione el registro a actualizar")
        else:
            bd=pymysql.connect(host="localhost", user="root",password="",database="corpicecream")
            cur=bd.cursor()
            cur.execute("update calculoc set auxiliar=%s, libro=%s WHERE activo=%s",(                       
                self.auxiliar_entre.get(),
                self.libro_entre.get(),
                self.descripcionaf_entre1.get()))
            bd.commit()
            self.fetch_datacontrol()
            self.clearcontrol()
            messagebox.showinfo("Actualizando", "Se actualizó correctamente el registro")
            bd.close()


        


        

    def sumacc(self):
        
        suma=0
        for tabla in lista:
            suma+= tabla
    

 

    def Reportes(self):
        gestionf=Frame(self.pantalla1, width="650", height="850",bd=3,relief="groove")
        gestionf.pack(fill= "y", expand="true")
        Label(self.pantalla1,text="REPORTES", font=("Arial",18)).place(x=80, y=10)

    def registrousu(self):
        self.pantalla1.withdraw()
        global registro
        registro =Toplevel(inicio)
        registro.geometry("350x525")
        registro.title("REGISTRO")
        registro.config(bg="azure3")

    
        global usuario_validar
        global contrasena_validar
        global contrasena_validar2
        global usuario
        global contrasena
        global contrasena2
        usuario_validar=StringVar()
        contrasena_validar=StringVar()
        contrasena_validar2=StringVar()
        registrof=Frame(registro, width="600", height="550",bd=3,relief="groove")
        registrof.place(x=15,y=10,width=320,height=500)
        imgregistro=PhotoImage(file="img/nusu.png")
        Label(registrof, image=imgregistro).pack()
        
        Label(registrof,text="Usuario: ").place(x=130,y=210)
        usuario=Entry(registrof, textvariable=usuario_validar.get())
        usuario.place(x=100,y=230)


        Label(registrof,text="Contraseña: ").place(x=125,y=270)
        contrasena=Entry(registrof, show="*", textvariable=contrasena_validar.get())
        contrasena.place(x=100,y=290)
        Label(registrof,text="Se recomineda combinar letras y caracteres",fg="salmon").place(x=50,y=310)
        
        Label(registrof,text="Repita su contraseña:").place(x=100,y=335)
        contrasena2=Entry(registrof, show="*", textvariable=contrasena_validar2.get())
        contrasena2.place(x=100,y=355)


    

        Button(registrof, text="REGISTRAR USUARIO",width="20",height="3",command=self.regis,overrelief="raised",activeforeground="cyan4",
                            cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).place(x=85,y=390)
        botonhome= Button(registrof,text="INICIO",width="7",height="1",command=self.iniciof1,overrelief="raised",activeforeground="cyan4", 
                            cursor="hand2", relief="groove",bg="SteelBlue2", borderwidth=3).place(x=130,y=460)

        registro.mainloop()








    def registrof(self):
        gestiond.withdraw() 
    def iniciof(self):
        controlp.withdraw() 
        
        self.pantalla1P()
    def iniciof1(self):
        registro.withdraw() 
        
        self.pantalla1P()
    def iniciof2(self):
        gestiond.withdraw() 
        
        self.pantalla1P()
    def iniciof3(self):
        self.ccontable.withdraw() 
        self.pantalla1P()
    
    def iniciof4(self):
        
        self.gestiondcrud.withdraw() 

        self.pantalla1P()

    def iniciof5(self):
        self.pantalla1.withdraw()
        self.loginP()
    

        





inicio=Tk()
ob=appcorpicecream(inicio)