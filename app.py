from flask import Flask, request, jsonify

app = Flask(__name__)

persons = []
sections = []
schools = []
faculties = []
enrollments = []

class Person:
    def __init__(self, id, dni, first_name, last_name):
        self.id = id
        self.dni = dni
        self.first_name = first_name
        self.last_name = last_name

class Section:
    def __init__(self, id, uc, semester, type, ht, hp, hl):
        self.id = id
        self.uc = uc
        self.semester = semester
        self.type = type
        self.ht = ht
        self.hp = hp
        self.hl = hl

class School:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Faculty:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.schools = []

class Enrollment:
    def __init__(self, id, person_id, section_id, type):
        self.id = id
        self.person_id = person_id
        self.section_id = section_id
        self.type = type


@app.route('/persons', methods=['GET', 'POST'])
def handle_persons():
    if request.method == 'GET':
        return jsonify([person.__dict__ for person in persons])
    elif request.method == 'POST':
        data = request.json
        person = Person(len(persons) + 1, data['dni'], data['first_name'], data['last_name'])
        persons.append(person)
        return jsonify(person.__dict__), 201

@app.route('/persons/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_person(id):
    person = next((person for person in persons if person.id == id), None)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404
    if request.method == 'GET':
        return jsonify(person.__dict__)
    elif request.method == 'PUT':
        data = request.json
        person.dni = data['dni']
        person.first_name = data['first_name']
        person.last_name = data['last_name']
        return jsonify(person.__dict__)
    elif request.method == 'DELETE':
        persons.remove(person)
        return '', 204

@app.route('/sections', methods=['GET', 'POST'])
def handle_sections():
    if request.method == 'GET':
        return jsonify([section.__dict__ for section in sections])
    elif request.method == 'POST':
        data = request.json
        section = Section(len(sections) + 1, data['uc'], data['semester'], data['type'], data['ht'], data['hp'], data['hl'])
        sections.append(section)
        return jsonify(section.__dict__), 201

@app.route('/sections/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_section(id):
    section = next((section for section in sections if section.id == id), None)
    if section is None:
        return jsonify({'error': 'Section not found'}), 404
    if request.method == 'GET':
        return jsonify(section.__dict__)
    elif request.method == 'PUT':
        data = request.json
        section.uc = data['uc']
        section.semester = data['semester']
        section.type = data['type']
        section.ht = data['ht']
        section.hp = data['hp']
        section.hl = data['hl']
        return jsonify(section.__dict__)
    elif request.method == 'DELETE':
        sections.remove(section)
        return '', 204

@app.route('/schools', methods=['GET', 'POST'])
def handle_schools():
    if request.method == 'GET':
        return jsonify([school.__dict__ for school in schools])
    elif request.method == 'POST':
        data = request.json
        school = School(len(schools) + 1, data['name'], data['description'])
        schools.append(school)
        return jsonify(school.__dict__), 201

@app.route('/schools/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_school(id):
    school = next((school for school in schools if school.id == id), None)
    if school is None:
        return jsonify({'error': 'School not found'}), 404
    if request.method == 'GET':
        return jsonify(school.__dict__)
    elif request.method == 'PUT':
        data = request.json
        school.name = data['name']
        school.description = data['description']
        return jsonify(school.__dict__)
    elif request.method == 'DELETE':
        schools.remove(school)
        return '', 204

@app.route('/faculties', methods=['GET', 'POST'])
def handle_faculties():
    if request.method == 'GET':
        return jsonify([faculty.__dict__ for faculty in faculties])
    elif request.method == 'POST':
        data = request.json
        faculty = Faculty(len(faculties) + 1, data['name'], data['description'])
        faculties.append(faculty)
        return jsonify(faculty.__dict__), 201

@app.route('/faculties/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_faculty(id):
    faculty = next((faculty for faculty in faculties if faculty.id == id), None)
    if faculty is None:
        return jsonify({'error': 'Faculty not found'}), 404
    if request.method == 'GET':
        return jsonify(faculty.__dict__)
    elif request.method == 'PUT':
        data = request.json
        faculty.name = data['name']
        faculty.description = data['description']
        return jsonify(faculty.__dict__)
    elif request.method == 'DELETE':
        faculties.remove(faculty)
        return '', 204

@app.route('/enrollments', methods=['GET', 'POST'])
def handle_enrollments():
    if request.method == 'GET':
        return jsonify([enrollment.__dict__ for enrollment in enrollments])
    elif request.method == 'POST':
        data = request.json
        enrollment = Enrollment(len(enrollments) + 1, data['person_id'], data['section_id'], data['type'])
        enrollments.append(enrollment)
        return jsonify(enrollment.__dict__), 201

@app.route('/enrollments/<int:id>', methods=['DELETE'])
def handle_enrollment(id):
    enrollment = next((enrollment for enrollment in enrollments if enrollment.id == id), None)
    if enrollment is None:
        return jsonify({'error': 'Enrollment not found'}), 404
    enrollments.remove(enrollment)
    return '', 204

@app.route('/persons/<int:person_id>/enrollments', methods=['GET', 'POST'])
def handle_person_enrollments(person_id):
    if request.method == 'GET':
        person_enrollments = [enrollment.__dict__ for enrollment in enrollments if enrollment.person_id == person_id]
        return jsonify(person_enrollments)
    elif request.method == 'POST':
        data = request.json
        section_id = data['section_id']
        section = next((section for section in sections if section.id == section_id), None)
        if section is None:
            return jsonify({'error': 'Section not found'}), 404
        enrollment = Enrollment(len(enrollments) + 1, person_id, section_id, section.type)
        enrollments.append(enrollment)
        return jsonify(enrollment.__dict__), 201

if __name__ == '__main__':
    app.run(debug=True, port=3000)