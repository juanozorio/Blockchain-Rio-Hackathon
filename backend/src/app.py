from flask import Flask, request, jsonify
from service.ProjectService import ProjectService
from storage.ProjectStorage import ProjectStorage
from collections import OrderedDict
import datetime

app = Flask(__name__)
storage = ProjectStorage()
service = ProjectService(storage)

def format_project(project):
    return OrderedDict([
        ('id', project.id),
        ('name', project.name),
        ('icon', project.icon),
        ('banner', project.banner),
        ('wallet', project.wallet),
        ('bio', project.bio),
        ('project_type', project.project_type),
        ('description', project.description),
        ('created_at', project.created_at.isoformat() if isinstance(project.created_at, datetime.datetime) else project.created_at),
        ('updated_at', project.updated_at.isoformat() if isinstance(project.updated_at, datetime.datetime) else project.updated_at),
    ])

@app.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    project_id = service.create_project(
        name=data['name'],
        icon=data.get('icon', ''),
        banner=data.get('banner', ''),
        wallet=data['wallet'],
        bio=data.get('bio', ''),
        project_type=data['project_type'],
        description=data.get('description', '')
    )
    return jsonify({'id': project_id}), 201

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = service.get_project(project_id)
    if project:
        return jsonify(format_project(project)), 200
    return jsonify({'error': 'Project not found'}), 404

@app.route('/projects', methods=['GET'])
def get_all_projects():
    projects = service.get_all_projects()
    return jsonify([format_project(project) for project in projects]), 200

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    service.update_project(
        project_id,
        name=data['name'],
        icon=data.get('icon', ''),
        banner=data.get('banner', ''),
        wallet=data['wallet'],
        bio=data.get('bio', ''),
        project_type=data['project_type'],
        description=data.get('description', '')
    )
    project = service.get_project(project_id)
    return jsonify(format_project(project)), 200

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    service.delete_project(project_id)
    return jsonify({'message': 'Project deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
