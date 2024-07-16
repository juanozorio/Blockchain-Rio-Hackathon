# service/ProjectService.py
from typing import List, Optional
from model.ProjectModel import ProjectModel
from storage.ProjectStorage import ProjectStorage
import datetime

class ProjectService:
    def __init__(self, storage: ProjectStorage):
        self.storage = storage

    def create_project(self, name: str, icon: str, banner: str, wallet: str, bio: str, project_type: bool, description: str) -> int:
        project = ProjectModel(
            name=name,
            icon=icon,
            banner=banner,
            wallet=wallet,
            bio=bio,
            project_type=project_type,
            description=description
        )
        return self.storage.add_project(project)

    def get_project(self, project_id: int) -> Optional[ProjectModel]:
        return self.storage.get_project_id(project_id)

    def get_all_projects(self) -> List[ProjectModel]:
        return self.storage.get_all_projects()

    def update_project(self, project_id: int, name: str, icon: str, banner: str, wallet: str, bio: str, project_type: bool, description: str):
        project = self.storage.get_project_id(project_id)
        if project:
            project.name = name
            project.icon = icon
            project.banner = banner
            project.wallet = wallet
            project.bio = bio
            project.project_type = project_type
            project.description = description
            project.updated_at = datetime.datetime.now()
            self.storage.update_project(project)

    def delete_project(self, project_id: int):
        self.storage.delete_project(project_id)
