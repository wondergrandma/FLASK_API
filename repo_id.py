import gitlab
import config
from database_engine import insertRepoId

#Funkcia ktorá získa ID repozitáru, ktoré je dôležité pre ukladanie súborov.
gl = gitlab.Gitlab(private_token=config.SERVER_PRIVATE_TOKEN)

def getRepoId(user_name):

    projects = gl.projects.list(owned = True, search = f'{user_name}_rules')
    
    for project in projects:
        id = project.id 

    insertRepoId(id, user_name)


"""gl = gitlab.Gitlab(private_token=config.SERVER_PRIVATE_TOKEN)

projects = gl.projects.list(owned = True ,search='test')
project = gl.projects.get(38163703)

for projetc in projects:
    id = projetc.id

print(id)

print(projects)
print(project)

print("##################################")
print(id)"""
