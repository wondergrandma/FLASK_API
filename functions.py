import gitlab
import config
import uuid
import requests
from compare import compareRule
from database_engine import createUserInDatabase, selectRepoId
from repo_id import getRepoId

#Jednotlivé funkcie voláne zo súboru view.py

#gl = gitlab.Gitlab(url = config.SERVER_URL, private_token = config.SERVER_PRIVATE_TOKEN)
gl = gitlab.Gitlab(private_token=config.SERVER_PRIVATE_TOKEN)

#Tvorba užívateľa, vytvorí ho do databázového súboru
def createUser(user_name):
    email = "defailt"
    createUserInDatabase(user_name, email)

#Tvorba repozitáru
def createRepo(name):
    #Projektom vytvoríme vlastne repozitár. 
    project = gl.projects.create({'name': f'{name}_rules'})
    getRepoId(name)

#Tvorba prázdnej zložky + vytvorenie prázdneho súboru do zložky.
def createEmptyDir(user_name):
    #id = 38163703

    user_name = user_name
    #id_int = selectRepoId(user_name)
    #id = int(id_int)
    id = selectRepoId(user_name)

    for rules in config.DIR_NAMES:
        req = requests.post("https://gitlab.com/api/v4/projects/"+f'{id}'+"/repository/files/"+f'{rules}'+"_RULES%2Finicialize.txt?ref=main",
                headers = {"PRIVATE-TOKEN": config.SERVER_PRIVATE_TOKEN},
                data={      "start_branch": "main",
                            "branch": "main",
                            "content": "",
                            "commit_message": "Initialization file"})

#Poslanie súboru do repozitáru na GitLab server.
def pushFile(type, text):
    compared_type = compareRule(type)

    #treba špecifikovať ID repozitáru do ktorého sa bude vkladať súbor
    project_id = 38163703
    project = gl.projects.get(project_id)

    #Generovanie zatial náhodného ID pre každý typ pravidla     
    uni_id = uuid.uuid1()

    f = project.files.create({'file_path': f'{compared_type}'+'_RULES/'+f'{compared_type}'+'_'+f'{uni_id}'+'.txt',
                              'branch': 'main',
                              'content': f'{text}',
                              'author_email': 'test@example.com',
                              'author_name': 'yourname',
                              'commit_message': 'Create testfile'})
    
    return "posted"
