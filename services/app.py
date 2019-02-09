from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello world"

@app.route('/weatherCheck', methods=['GET'])
def weatherCheck():
    return 'Successful'

@app.route('/getWeatherFile',methods=['GET'])
def getweatherFile():
    return ''
if __name__ =='__main__':
    app.run(debug=True)
