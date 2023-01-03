from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
import gitlab
import config
import json 
from functions import pushFile, createRepo, createEmptyDir, createUser

#Definovanie API endpointov, volanie funkcií pod každým, ktorý je definovaný.

app = Flask("GitLabManagerAPI")
api = Api(app)
#gl = gitlab.Gitlab(url = config.SERVER_URL, private_token = config.SERVER_PRIVATE_TOKEN)
gl = gitlab.Gitlab(private_token=config.SERVER_PRIVATE_TOKEN)

#---------------  MAIN PART OF CODE ----------------
#Metóda, ktorý vytvorí nového užívateľa, vytvorí mu repozotár v ktorom sa budú nachádzať zložky pre pravidlá
class MakeUser(Resource):
    def post(self, user_name):
        createUser(user_name)
        createRepo(user_name)
        createEmptyDir(user_name)
        return "Repository for " f'{user_name}' "was created!"

#Triedenie prichádzajúcich pravidiel do zložiek na GitLabe
class SortRules(Resource):
    def post(self):

        data = request.data
        json_data = json.loads(data)

        type = json_data['type']
        type = type.upper()

        text = json_data['data']

        match type:
            case "RSA":
                pushFile(type, text)
                return "RSA rule created"
            case "QRADAR":
                pushFile(type, text)
                return "Qradar rule created"
            case "SOLARWINDS":
                pushFile(type, text)
                return "SolarWinds rule created"
            case _:
                pushFile(type)
                return "Default"

#---------------- MAIN RESOURCES ------------------
#definovanie endpointov
api.add_resource(SortRules, '/data')
api.add_resource(MakeUser, '/user/<string:user_name>')

if __name__ == '__main__':
    #Konfigurácia API, url a port
    app.run(host = config.HOST_API_URL, port = config.HOST_API_PORT, use_reloader=True)