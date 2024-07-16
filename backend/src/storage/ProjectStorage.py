import sqlite3
import datetime
from typing import List, Optional
from model.ProjectModel import ProjectModel

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
            INSERT INTO projects (name, icon, banner, wallet, bio, project_type, description, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (project.name, project.icon, project.banner, project.wallet, project.bio, project.project_type, project.description, project.created_at, project.updated_at))
            conn.commit()
            return cursor.lastrowid

    def get_project_id(self, project_id: int) -> Optional[ProjectModel]:
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
            row = cursor.fetchone()
            if row:
                return ProjectModel(
                    id=row[0],
                    name=row[1],
                    icon=row[2],
                    banner=row[3],
                    wallet=row[4],
                    bio=row[5],
                    project_type=row[6],
                    description=row[7],
                    created_at=row[8],
                    updated_at=row[9]
                )
            return None

    def get_all_projects(self) -> List[ProjectModel]:
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM projects")
            rows = cursor.fetchall()
            return [
                ProjectModel(
                    id=row[0],
                    name=row[1],
                    icon=row[2],
                    banner=row[3],
                    wallet=row[4],
                    bio=row[5],
                    project_type=row[6],
                    description=row[7],
                    created_at=row[8],
                    updated_at=row[9]
                ) for row in rows
            ]

    def update_project(self, project: ProjectModel):
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE projects
            SET name = ?, icon = ?, banner = ?, wallet = ?, bio = ?, project_type = ?, description = ?, created_at = ?, updated_at = ?
            WHERE id = ?
            """, (project.name, project.icon, project.banner, project.wallet, project.bio, project.project_type, project.description, project.created_at, project.updated_at, project.id))
            conn.commit()

    def delete_project(self, project_id: int):
        with sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
            conn.commit()
