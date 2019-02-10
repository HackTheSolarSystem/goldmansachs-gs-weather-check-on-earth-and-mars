from flask import Flask
app = Flask(__name__)
from file_retriever import retrieve_from_server

@app.route('/')
@app.route('/welcome')
def HelloWorld():
    return "Welcome to Daily Weather!"

@app.route('/')
@app.route('/daily-weather', methods=['GET'])
def get_daily_weather():
    #TODO FileWatcher - to watch for real time image from NASA/MARCI
    #TODO Extract data
    retrieve_from_server('mars','https://minnlawyer.com/files/2017/04/comma-clipart-clipart-best-frrJZJ-clipart.jpg', 'https://cdn.pixabay.com/photo/2017/01/03/02/07/vine-1948358_1280.png','20180202','0000')
    return 'Successful'

if __name__ =='__main__':
    app.run(debug=True)
