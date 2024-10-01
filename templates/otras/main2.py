# main.py
import os
from flask import Flask, send_file
from src.py.preguntas import submit  # Importa la función submit desde preguntas.py

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    return send_file('templates/index.html')

# Registra la función submit para la ruta '/submit'
app.add_url_rule('/submit', view_func=submit, methods=['POST'])

# Método main de la aplicación
def main():
    app.run(port=int(os.environ.get('PORT', 8100)), debug=True)

if __name__ == "__main__":
    main()
 


                                
                                  
                              
                                    
                                       
                        
                                        