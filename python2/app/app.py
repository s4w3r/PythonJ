from flask import Flask,render_template,request,redirect,url_for,session
import mysql.connector
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)
#configurar la conexion a bd
app.secret_key= '12345'
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "GestionTarea"

)

cursor=db.cursor(dictionary=True)

#Listar usuarios
@app.route('/lista',methods=['GET','POST'])
def lista():
    cursor.execute("SELECT * FROM usuario WHERE Rol='usuario'")
    usuario=cursor.fetchall()

    return render_template('principal.html',usuarios=usuario)


#Listar tareas
@app.route('/tare',methods=['GET','POST'])
def tare():
    cursor.execute("SELECT * FROM tareas")
    tarea=cursor.fetchall()

    return render_template('principalusu.html',tareas=tarea)

@app.route('/',methods=['GET','POST'])
def login():
    #verficacion de credenciales
    usuario = request.form.get('Usuario')
    contrasena = request.form.get('Contraseña')

    cursor = db.cursor(dictionary=True)
    query = "SELECT Usuario,Contraseña,Rol FROM usuario WHERE Usuario = %s"
    cursor.execute(query,(usuario,))
    usuarios = cursor.fetchone()

    if(usuarios and check_password_hash(usuarios['Contraseña'],contrasena)):
        #Crear la sesion
        session['usuario'] = usuarios['Usuario'] 
        session['rol'] = usuarios['Rol']
        if usuarios['Rol'] == 'Administrador':
            return render_template('principal.html')
        else:
            return render_template('principalusu.html')
    else:
        print("Credenciales incorrectas, intentar nuevamente")
        return render_template("index.html")
    

@app.route('/salir')
def salir():
    session.pop('usuario',None)
    return redirect(url_for('login'))

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache,no-store,must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = 0

    return response

#crear una ruta
@app.route('/RegistroUsuario',methods=['GET','POST'])
def registrousuario():
    if request.method == 'POST':
        NombreUsuario =request.form.get('Nombre')
        ApellidoUsuario =request.form.get('Apellido')
        EmailUsuario =request.form.get('Email')
        Usuarionom =request.form.get('Usuario')
        contraseña =request.form.get('Contraseña')
        Rol =request.form.get('Rol')

        encriptar = generate_password_hash(contraseña)

        #verificar el nombre y email si ya existe
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuario WHERE usuario=%s OR Email =%s",(Usuarionom,EmailUsuario))
        resultado = cursor .fetchone()
        if resultado:
            print("Usuario o Email ya registrado")
            render_template('registrousuario.html')
            #Insertar los usuarios a la bd
        else:
            cursor.execute("INSERT INTO usuario(Nombre, Apellido, Email, Usuario, Contraseña, Rol) VALUES(%s,%s,%s,%s,%s,%s)",(NombreUsuario,ApellidoUsuario,EmailUsuario,Usuarionom,encriptar,Rol))
            db.commit()
            print("usuario registrado")
            return redirect(url_for('registrousuario'))
        
    return render_template('registrousuario.html')


#Crear las rutas 
@app.route('/registrotarea',methods=['GET','POST'])
def registrartarea():
    if request.method == 'POST':
        Nombretarea = request.form.get('nombre_tar')
        FechaInicio = request.form.get('fechaInicio')
        FechaFinal = request.form.get('fechaFin')
        EstadoT = request.form.get('estado')

        #Verificar el nombre de la tarea no este regisrtado
        
        cursor.execute("SELECT * FROM tareas WHERE nombre_tar = %s",(Nombretarea,))
        Existe =cursor.fetchone()

        if Existe:
            (print("La tarea ya existe idiota"))
            return render_template("registrotarea.html")
        else:
        #insetar las tarea a la tabala tareas
            cursor.execute("INSERT INTO tareas(nombre_tar,fechaInicio,fechaFin,estado) VALUES(%s,%s,%s,%s)",(Nombretarea,FechaInicio,FechaFinal,EstadoT))
            db.commit()
            print("Tarea registrada")
    return render_template('registrotarea.html')
    

if __name__ == '__main__':
    app.run(debug=True)
    app.add_url_rule('/',view_func=registrousuario) 