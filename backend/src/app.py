from flask import Flask, request, jsonify
from model.ProjectModel import ProjectModel
from service.ProjectService import ProjectService

app = Flask(__name__)

project_service = ProjectService()

@app.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    try:
        project = ProjectModel(
            name=data.get('name'),
            icon=data.get('icon'),
            banner=data.get('banner'),
            wallet=data.get('wallet'),
            bio=data.get('bio'),
            project_type=data.get('project_type'),
            description=data.get('description')
        )
        project_service.add_project(project)
        return jsonify({'message': 'Project added successfully!'}), 201
    except AttributeError as e:
        return jsonify({'error': 'AttributeError: ' + str(e)}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/projects/<int:id>', methods=['GET'])
def get_project_by_id(id):
    project = project_service.get_project_by_id(id)
    if project:
        return jsonify(project.to_dict())
    return jsonify({'error': 'Project not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
