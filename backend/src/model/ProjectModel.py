class ProjectModel:
    def __init__(self, id: int, name: str, icon: str, banner: str, wallet: str, bio: str, project_type: bool, descript: str):
        self.id = id
        self.name = name
        self.icon = icon
        self.banner = banner
        self.wallet = wallet
        self.bio = bio
        self.project_type = project_type
        self.descript = descript

    def get_wallet(self) -> str:
        return self.wallet

    def __repr__(self):
        return f"Project(id={self.id}, name='{self.name}', icon='{self.icon}', banner='{self.banner}', wallet='{self.wallet}', bio='{self.bio}', project_type={self.project_type}, descript='{self.descript}')"


