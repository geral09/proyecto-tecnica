-- crea la tabla usuarios
CREATE TABLE users (id INTEGER PRIMARY KEY,name TEXT NOT NULL,email TEXT NOT NULL,creation_date DATETIME DEFAULT CURRENT_TIMESTAMP );
-- cerea la tabla cuentionarios de usuario
CREATE TABLE user_quiz (id_user INTEGER,quiz_level TEXT NOT NULL,question_total INTEGER DEFAULT 0 NOT NULL,question_correct INTEGER DEFAULT 0 NOT NULL,question_incorrect INTEGER DEFAULT 0 NOT NULL,creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (id_user) REFERENCES users(id));
-- cerea la tabla cuentionarios de usuario
CREATE TABLE admin_quiz (id_user INTEGER,id_admin_level INTEGER NOT NULL DEFAULT 3,text_admin_level TEXT NOT NULL DEFAULT 'Ver',creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (id_user) REFERENCES users(id));
