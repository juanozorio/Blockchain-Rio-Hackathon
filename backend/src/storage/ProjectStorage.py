import sqlite3
import datetime
import logging
from typing import List, Optional

# Registrando adaptadores e conversores de datetime
def adapt_datetime(ts):
    return ts.strftime('%Y-%m-%d %H:%M:%S')

def convert_datetime(s):
    try:
        return datetime.datetime.strptime(s.decode('utf-8'), '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        return datetime.datetime.strptime(s.decode('utf-8'), '%Y-%m-%d %H:%M:%S')

sqlite3.register_adapter(datetime.datetime, adapt_datetime)
sqlite3.register_converter("timestamp", convert_datetime)

# Classe de modelo
class ProjectModel:
    def __init__(self, id: Optional[int], name: str, icon: str, banner: str, wallet: str, bio: str, project_type: bool, description: str, created_at: datetime.datetime = None, updated_at: datetime.datetime = None):
        self.id = id
        self.name = name
        self.icon = icon
        self.banner = banner
        self.wallet = wallet
        self.bio = bio
        self.project_type = project_type
        self.description = description
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()

    def get_wallet(self) -> str:
        return self.wallet

    def __repr__(self):
        return f"Project(id={self.id}, name='{self.name}', icon='{self.icon}', banner='{self.banner}', wallet='{self.wallet}', bio='{self.bio}', project_type={self.project_type}, descript='{self.descript}', created_at={self.created_at}, updated_at={self.updated_at})"


# Classe de camada de armazenamento
class ProjectStorage:
    def __init__(self, db_name: str = "project.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                icon TEXT,
                banner TEXT,
                wallet TEXT NOT NULL,
                bio TEXT,
                project_type BOOLEAN NOT NULL,
                description TEXT,
                created_at TIMESTAMP NOT NULL,
                updated_at TIMESTAMP NOT NULL
            )
            """)
            conn.commit()

    def add_project(self, project: ProjectModel) -> int:
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO projects (name, icon, banner, wallet, bio, project_type, descript, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (project.name, project.icon, project.banner, project.wallet, project.bio, project.project_type, project.description, project.created_at, project.updated_at))
            conn.commit()
            return cursor.lastrowid

    def get_project(self, project_id: int) -> Optional[ProjectModel]:
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
            row = cursor.fetchone()
            if row:
                return ProjectModel(*row)
            return None

    def get_all_projects(self) -> List[ProjectModel]:
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM projects")
            rows = cursor.fetchall()
            return [ProjectModel(*row) for row in rows]

    def update_project(self, project: ProjectModel):
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE projects
            SET name = ?, icon = ?, banner = ?, wallet = ?, bio = ?, project_type = ?, descript = ?, created_at = ?, updated_at = ?
            WHERE id = ?
            """, (project.name, project.icon, project.banner, project.wallet, project.bio, project.project_type, project.description, project.created_at, project.updated_at, project.id))
            conn.commit()

    def delete_project(self, project_id: int):
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
            conn.commit()


    