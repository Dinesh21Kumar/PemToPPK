from flask import Flask, request, json,Response
import os
import time
from werkzeug import secure_filename
from pathlib import Path
from flask_json import FlaskJSON,jsonify, JsonError, json_response, as_json
ALLOWED_EXTENSIONS = set(['pem'])
app = Flask(__name__)
cwd = os.getcwd()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/pemtoppk',methods=["GET","POST"])
def pemtoppk():
    if request.method == 'POST':
        try:
            user_name = request.form.get('user_name')
            pem_key = request.form.get('pem_key')
            print ("print username ")
            print (user_name)
            print ("print input pem key ")
            print (pem_key)
            pemFileName = user_name + ".pem"
            pemFile = open(pemFileName, "w")
            pemFile.write(pem_key)
            pemFile.close()
            ppkFileName = user_name+ ".ppk"
            os.system("puttygen " + pemFileName  + " -O private -o "+ ppkFileName)
            ppkFile = open(ppkFileName, "r")
            ppkKey = ppkFile.read()
            print (ppkKey)
            data = {'key': ppkKey}
            js = json.dumps(data)
            resp = Response(ppkKey,status=200,mimetype='text/html')
            os.system("rm -rf "+ pemFileName)
            os.system("rm -rf "+ ppkFileName)
            return resp
        except Exception as ex:
            print (ex)
            return Response(error = ex,status=400,mimetype='text/html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
