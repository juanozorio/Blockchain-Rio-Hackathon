
from flask import Flask, request, jsonify
from service.ProjectService import ProjectService
from storage.ProjectStorage import ProjectStorage
import datetime

app = Flask(__name__)
storage = ProjectStorage()
service = ProjectService(storage)

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
        return jsonify(project.__dict__), 200
    return jsonify({'error': 'Project not found'}), 404

@app.route('/projects', methods=['GET'])
def get_all_projects():
    projects = service.get_all_projects()
    return jsonify([project.__dict__ for project in projects]), 200

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
    return jsonify({'message': 'Project updated successfully'}), 200

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    service.delete_project(project_id)
    return jsonify({'message': 'Project deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
