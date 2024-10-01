<!-- ejeta sqlite -->
sqlite3.exe
<!-- muestra la da de sqlite -->
.help
<!-- coamando para crear la base de datos quiz-->
sqlite3.exe quiz.db
<!-- selecciona conecta a la base de datos quiz -->
sqlite3.exe quiz.db
<!-- coamando para crear la tabla usuaraios -->
CREATE TABLE users (id INTEGER PRIMARY KEY,name TEXT NOT NULL,email TEXT NOT NULL,creation_date DATETIME DEFAULT CURRENT_TIMESTAMP );
<!-- comando para crear la tabla cuantinorio usuario -->
CREATE TABLE user_quiz (id_user INTEGER,quiz_level TEXT NOT NULL,question_total DEFAULT 0 NOT NULL,question_correct INTEGER DEFAULT 0 NOT NULL,question_incorrect INTEGER DEFAULT 0 NOT NULL,creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (id_user) REFERENCES users(id));
<!-- elimina la tala usuarios -->
DROP TABLE users;
<!-- modifica el nombre de la tabla usuarios -->
ALTER TABLE users RENAME TO users1;
<!-- elimina todos los registros de la tabla usuarios  -->
DELETE FROM users;
<!-- elimina todos los registros de la tabla quiz usuarios  -->
DELETE FROM user_quiz;
<!-- inserta registro en la tabla usuarios -->
INSERT INTO users (name,email) VALUES('John Doe','<johndoe@mail.com>');
<!-- inserta vrios registros ala ves en la tabla usuarios -->
INSERT INTO users (name,email) VALUES('Jhanne Doe','<jhannedoe@mail.com>'),('Jim Doe','<jimdoe@mail.com>');
<!-- actulaiza registro en la tabla usuarios -->
UPDATE users SET name='Jhane Does',email='<jhanedoe@mail.com>' WHERE id = 2;
<!-- elimina registro en la tabla usuarios -->
DELETE FROM users WHERE id = 4;
<!-- selecciona todas los datos de la tabla usuarios -->
SELECT * FROM users;
<!-- selecciona todas los datos de la tabla quiz usuarios -->
SELECT * FROM user_quiz;
<!-- muestra las bases de datos -->
PRAGMA database_list;
<!-- muestra las tablas de la base de datos -->
.tables
<!-- desconecta la base de datos -->
.quit
<!-- verifica que el soporte para claves foraneas este activo -->
PRAGMA foreign_keys;
<!-- activa el soporte para claves foraneas -->
PRAGMA foreign_keys = ON;
<!-- activa el soporte para claves foraneas -->
PRAGMA foreign_keys = OFF;
<!-- Consultar el Tamaño Máximo de una Página: -->
PRAGMA page_size;
<!-- Consultar las Opciones de Compilación: -->
PRAGMA max_page_count;
<!-- Consultar las Opciones de Compilación: -->
PRAGMA compile_options;
<!-- ver la estructura de la tabla -->
PRAGMA table_info(user_quiz);
<!-- Salir de SQLite: -->
.exit
<!-- ejecuta comandos desde un archivo caundo son demasiado largos -->
.read create_tables.sql
<!-- convierte la fecha y hora a la region del equipo -->
SELECT datetime(creation_date, 'localtime') FROM users;

<!-- ----------------------------------------------------------------------- -->
<!-- para poder integrar codigo phon fentro de html se usa Jinja2 -->

1. Variables y Expresiones

<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>Hola, {{ name }}!</p>
    <p>La suma de 5 y 3 es {{ 5 + 3 }}.</p>
</body>
</html>

2. Condicionales
{% if user %}
    <p>Hola, {{ user.username }}!</p>

{% else %}
    <p>Hola, invitado!</p>
{% endif %}

También puedes usar {% elif %} y {% else %} para múltiples condiciones:
{% if age < 18 %}
    <p>Eres menor de edad.</p>
{% elif age < 65 %}
    <p>Eres adulto.</p>
{% else %}
    <p>Te has jubilado.</p>
{% endif %}

3. Bucles

<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>

Puedes usar el índice del bucle con loop.index y loop.index0:
<ul>
    {% for user in users %}
        <li>{{ loop.index }}: {{ user.name }}</li>
    {% endfor %}
</ul>

4. Filtros

<p>{{ text | upper }}</p> <!-- Convierte el texto a mayúsculas -->
<p>{{ number | number_format }}</p> <!-- Formatea números -->
<p>{{ date | date("d/m/Y") }}</p> <!--Da formato a fechas -->

5. Macros
{% macro render_table(rows) %}
    <table>
        {% for row in rows %}
            <tr>
                {% for cell in row %}
                    <td>{{ cell }}</td>
                {% endfor %}
            </tr>
        {% endfor %}
    </table>
{% endmacro %}

<!-- Usar el macro -->
{{ render_table([[1, 2], [3, 4]]) }}

6. Incluir Plantillas
<!-- En la plantilla principal -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    {% include 'header.html' %}
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
    {% include 'footer.html' %}
</body>
</html>

7. Extender Plantillas
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mi Sitio{% endblock %}</title>
</head>
<body>
    <header>
        <h1>{% block header %}Encabezado{% endblock %}</h1>
    </header>
    <main>
        {% block content %}Contenido{% endblock %}
    </main>
    <footer>
        {% block footer %}Pie de página{% endblock %}
    </footer>
</body>
</html>

