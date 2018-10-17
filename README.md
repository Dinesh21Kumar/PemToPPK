# PemToPPK

Description: This is a simple python program to convert .pem key file to .ppk file.

How to run ?

1. docker pull dinesh63504kumar/pemtoppk
2. docker create -it -p 5000:5000 dinesh63504kumar/pemtoppk bash
3. docker start <container-id>
4. Open Postman client

API URL: http://localhost:5000/pemtoppk
REQ Type: POST
Body:
form-data 
{
"pem_key":"paste your RSA format .pem key in text format"
"output_filename": "Input some ppk file name"
}

Response: 
Content of .ppk file in text format.
