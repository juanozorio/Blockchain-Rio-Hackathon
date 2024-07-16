from model.ProjectModel import ProjectModel
from storage.ProjectStorage import ProjectStorage

class ProjectService:
    def __init__(self):
        self.projects = []
        self.storage = ProjectStorage()
        
    def validate_project(self, project: ProjectModel) -> bool:
        if not project.wallet:
            raise ValueError("Wallet address is required")
        
        if not project.name or not isinstance(project.name, str) or len(project.name.strip()) == 0:
            raise ValueError("Project name is required and must be a non-empty string")

        if not project.bio or not isinstance(project.bio, str) or len(project.bio.strip()) == 0:
            raise ValueError("Bio is required and must be a non-empty string")
        
        if not isinstance(project.project_type, bool):
            raise ValueError("Project type must be a boolean value")
        
        if not project.description or not isinstance(project.description, str) or len(project.description.strip()) == 0:
            raise ValueError("Description is required and must be a non-empty string")
        
        return True

    def add_project(self, project: ProjectModel):
        if self.validate_project(project):
            self.storage.add_project(project)
            print(f"Project {project.name} has been added.")

    def get_project_by_id(self, project_id: int) -> ProjectModel:
        return self.storage.get_project(project_id)
