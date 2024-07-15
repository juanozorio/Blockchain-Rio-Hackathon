from src.storage.ProjectStorage import ProjectStorage
from src.model.ProjectModel import ProjectModel

#Exemplo de uso
if __name__ == "__main__":
      storage = ProjectStorage()
      new_project = ProjectModel(name="Project Alpha", icon="icon.png", banner="banner.png", wallet="0xABC123", bio="Bio of Project Alpha", project_type=True, descript="Description of Project Alpha")
      project_id = storage.add_project(new_project)
      print(project_id)
    # new_project.id = project_id

    # Obter projeto pelo ID
    # project = storage.get_project(1)
    # print(project)

    # Atualizar projeto
    # if project:
    #     project.bio = "Testando atualização"
    #     storage.update_project(project)

    # Obter todos os projetos
    # all_projects = storage.get_all_projects()
    # for project in all_projects:
    #     print(project)

    # # Deletar projeto
    # delete_project_id = 1
    # storage.delete_project(delete_project_id)