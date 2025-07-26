# 🎓 StudentOverflow
***Proyecto final para la materia de Programación Avanzada*
---

**StudentOverflow** Aplicación web desarrollada en Python con Flask. Su funcionalidad se basa para estudiantes que desean hacer preguntas académicas y colaborar respondiendo a otros.

---

## 📁 Estructura del proyecto
studentoverflow/
│
├── app/
│   ├── models.py
│   ├── routes.py
│   ├──__init__.py
│	├── api.py
│	├──auth.py
│   └── templates/
│        └── base.html
│        ├── detalle_pregunta.html
│		 ├── index.html
│        ├── login.html
│		 ├──preguntar.html
│		 └── register.html
│
├── documentation-db/
├── Entrgeables/
├── migrations/
├── .env
├── config.py
├── requirements.txt
├── README.md
└── run.py

---

## 🚀 Funcionalidades principales

- ✅ Registro e inicio de sesión de usuarios
- ✅ Publicación de preguntas con título y descripción
- ✅ Respuestas por parte de la comunidad
- ✅ Respuesta automática usando una API externa (Cuando la pregunta no ha tenido respuestas)
- ✅ Página de inicio dinámica según sesión del usuario
- ✅ Interfaz amigable, clara y responsiva

---

## 🛠 Tecnologías utilizadas

| Backend          | Frontend         | Base de datos        | Herramientas Dev |
|------------------|------------------|----------------------|------------------|
| Python 3.x       | HTML + CSS       | PostgreSQL (PgAdmin) | Flask CLI        |
| Flask            | Jinja2           | SQLAlchemy           | Flask-Migrate    |
| Flask-SQLAlchemy | Bootstrap básico | Psycopg2             | Git / GitHub     |

---


## 🧪 Instalación y ejecución

### 📦 1. Clona el repositorio

```bash
git clone https://github.com/Marcelo116/proyecto_StudentOverflow.git
cd studentoverflow
```
---
### 🧪 2. Crea el entorno virtual

```python -m venv venv
source venv/bin/activate
```
---
### 📄 3. Istala dependencias

```
pip install -r requirements.txt
```

---

### ⚙️ 4. Configura tu base de datos PostgreSQL en el archivo .env o en config.py y realiza migraciones
```
flask db init
flask db migrate -m "Inicial"
flask db upgrade
```
---

### ️🚀 5. Corre la app
```
python3 run.py
```