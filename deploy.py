from flask import Flask
from app import app
from flask import render_template, request
import psycopg2

app = Flask(__name__)

host = "ec2-50-17-234-234.compute-1.amazonaws.com"
port = 5432
user = "qiyhtghkmkqxnu"
passwd="8506c1a49894c677f66bfb214716d9a1818c61d6260c134e267261b44bb72811"
database = "d7o1lnvniub2ts"


conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s"%(host,database,user,passwd,port))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	return render_template('index.html',generos=generos,tipos=tipos)

@app.route('/animes')
def animes():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Animes"
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('index.html',animes=animes,generos=generos,tipos=tipos)

@app.route('/categorias')
def categorias():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	return render_template('categorias.html',generos=generos,tipos=tipos)

@app.route('/personajes')
def personajes():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Personajes"
	cur.execute(sql)
	personajes = cur.fetchall()
	return render_template('personajes.html',generos=generos,personajes=personajes,tipos=tipos)

@app.route('/autores')
def autores():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Autores"
	cur.execute(sql)
	autores = cur.fetchall()
	return render_template('autores.html',generos=generos,autores=autores,tipos=tipos)

@app.route('/estudios')
def estudios():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Estudios"
	cur.execute(sql)
	estudios = cur.fetchall()
	return render_template('estudios.html',generos=generos,estudios=estudios,tipos=tipos)

@app.route('/categorias/<int:id>')
def categorias_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select nombre from Generos where id = " + str(id)
	cur.execute(sql)
	resultado = cur.fetchall()
	sql = "select * from Animes, Generos, Animes_Generos where anime_id = Animes.id and genero_id = Generos.id and Generos.id = " + str(id)
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('categorias_id.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

@app.route('/animes/<int:id>')
def animes_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Animes where id = " + str(id)
	cur.execute(sql)
	anime = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select * from Personajes, Animes_Personajes where anime_id = " + str(id) + " and Personajes.id = personaje_id"
	cur.execute(sql)
	personajes = cur.fetchall()
	sql = "select * from Generos, Animes_Generos where anime_id = " + str(id) + " and Generos.id = genero_id"
	cur.execute(sql)
	categorias = cur.fetchall()
	sql = "select * from Estudios, Animes where Estudios.id = estudio_id and Animes.id = " + str(id) 
	cur.execute(sql)
	estudio = cur.fetchall()
	sql = "select * from Autores, Animes where Autores.id = autor_id and Animes.id = " + str(id)
	cur.execute(sql)
	autor = cur.fetchall()
	sql = "select * from Estados where anime_id = " + str(id)
	cur.execute(sql)
	estado = cur.fetchall()
	return render_template('animes_id.html',generos=generos,tipos=tipos,anime=anime,personajes=personajes,categorias=categorias,estudio=estudio,autor=autor,estado=estado)

@app.route('/buscar/results',methods=["GET"])
def buscar():
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	keyword = request.args.get('search')
	keyword = str(keyword)
	sql = "select id, nombre from Animes where lower(nombre) like lower('%%%s%%')" %(keyword)
	cur.execute(sql)
	resultados = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	return render_template('buscar.html',generos=generos,resultados=resultados,tipos=tipos)

@app.route('/estudios/<int:id>')
def estudios_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select nombre from Estudios where id = " + str(id)
	cur.execute(sql)
	resultado = cur.fetchall()
	sql = "select * from Animes, Estudios where Animes.estudio_id = Estudios.id and Estudios.id = " + str(id)
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('estudios_id.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

@app.route('/personajes/<int:id>')
def personajes_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select nombre from Personajes where id = " + str(id)
	cur.execute(sql)
	resultado = cur.fetchall()
	sql = "select * from Animes, Personajes, Animes_Personajes where Animes.id = anime_id and Personajes.id = personaje_id and Personajes.id = " + str(id)
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('personajes_id.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

@app.route('/autores/<int:id>')
def autores_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	sql = "select nombre from Autores where id = " + str(id)
	cur.execute(sql)
	resultado = cur.fetchall()
	sql = "select * from Animes, Autores where Animes.autor_id = Autores.id and Autores.id = " + str(id)
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('autores_id.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

@app.route('/tipos/<int:id>')
def tipos_id(id):
	sql = "select row_number() over (order by tipo), tipo from Animes group by tipo order by tipo"
	cur.execute(sql)
	tipos = cur.fetchall()
	sql = "select * from Generos"
	cur.execute(sql)
	generos = cur.fetchall()
	resultado = [tipos[0][0],tipos[0][1]]
	sql = "select * from Animes where tipo = '%s'" %(str(tipos[id-1][1]))
	cur.execute(sql)
	animes = cur.fetchall()
	return render_template('tipos.html',animes=animes,generos=generos,resultado=resultado,tipos=tipos)

