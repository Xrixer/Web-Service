import requests;
from flask import Flask, request, jsonify
import os

def main_menu():
    while True:
        os.system('cls')
        print("Menú principal")
        print("1. Listar")
        print("2. Crear")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            list_menu()
        elif choice == "2":
            create_menu()
        elif choice == "3":
            update_menu()
        elif choice == "5":
            print("Gracias por usar nuestros servicios")
            break
        else:
            print("Opción inválida")

def list_menu():
    while True:
        os.system('cls')
        print("Menú de listado")
        print("1. Personas")
        print("2. Secciones")
        print("3. Escuelas")
        print("4. Facultades")
        print("5. Estudiantes")
        print("6. Profesores")
        print("7. Volver")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            persons = requests.get('http://localhost:3000/persons').json()
            print("Lista de personas:")
            for person in persons:
                print(f"{person['id']}: {person['first_name']} {person['last_name']}")
        elif choice == "2":
            sections = requests.get('http://localhost:3000/sections').json()
            print("Lista de secciones:")
            for section in sections:
                print(f"{section['id']}: {section['type']} - UC: {section['uc']}")
        elif choice == "3":
            schools = requests.get('http://localhost:3000/schools').json()
            print("Lista de escuelas:")
            for school in schools:
                print(f"{school['id']}: {school['name']} - {school['description']}")
        elif choice == "4":
            faculties = requests.get('http://localhost:3000/faculties').json()
            print("Lista de facultades:")
            for faculty in faculties:
                print(f"{faculty['id']}: {faculty['name']} - {faculty['description']}")
        elif choice == "5":
            enrollments = requests.get('http://localhost:3000/enrollments?type=student').json()
            print("Lista de estudiantes:")
            for enrollment in enrollments:
                print(f"{enrollment['id']}: {enrollment['person_id']} - {enrollment['section_id']}")
        elif choice == "6":
            enrollments = requests.get('http://localhost:3000/enrollments?type=teacher').json()
            print("Lista de profesores:")
            for enrollment in enrollments:
                print(f"{enrollment['id']}: {enrollment['person_id']} - {enrollment['section_id']}")
        elif choice == "7":
            break
        else:
            print("Opción inválida")

def create_menu():
    while True:
        os.system('cls')
        print("Menú de creación")
        print("1. Persona")
        print("2. Sección")
        print("3. Escuela")
        print("4. Facultad")
        print("5. Volver")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            first_name = input("Ingresa el nombre: ")
            last_name = input("Ingresa el apellido: ")
            dni = input("Ingresa el DNI: ")
            data = {'first_name': first_name, 'last_name': last_name, 'dni': dni}
            response = requests.post('http://localhost:3000/persons', json=data)
            if response.status_code == 201:
                print("Persona creada exitosamente")
            else:
                print("Error al crear la persona")
        elif choice == "2":
            uc = input("Ingresa la UC: ")
            semester = input("Ingresa el semestre: ")
            type = input("Ingresa el tipo (mandatory o elective): ")
            ht = input("Ingresa las horas teóricas: ")
            hp = input("Ingresa las horas prácticas: ")
            hl = input("Ingresa las horas de laboratorio: ")
            data = {'uc': uc, 'semester': semester, 'type': type, 'ht': ht, 'hp': hp, 'hl': hl}
            response = requests.post('http://localhost:3000/sections', json=data)
            if response.status_code == 201:
                print("Sección creada exitosamente")
            else:
                print("Error al crear la sección")
        elif choice == "3":
            name = input("Ingresa el nombre: ")
            description = input("Ingresa la descripción: ")
            data = {'name': name, 'description': description}
            response = requests.post('http://localhost:3000/schools', json=data)
            if response.status_code == 201:
                print("Escuela creada exitosamente")
            else:
                print("Error al crear la escuela")
        elif choice == "4":
            name = input("Ingresa el nombre: ")
            description = input("Ingresa la descripción: ")
            data = {'name': name, 'description': description}
            response = requests.post('http://localhost:3000/faculties', json=data)
            if response.status_code == 201:
                print("Facultad creada exitosamente")
            else:
                print("Error al crear la facultad")
        elif choice == "5":
            break
        else:
            print("Opción inválida")

def update_menu():
    while True:
        os.system('cls')
        print("Menú de actualización")
        print("1. Actualizar persona")
        print("2. Actualizar sección")
        print("3. Actualizar escuela")
        print("4. Actualizar facultad")
        print("5. Volver")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            id = input("Ingresa el ID de la persona que deseas actualizar: ")
            first_name = input("Ingresa el nuevo nombre: ")
            last_name = input("Ingresa el nuevo apellido: ")
            dni = input("Ingresa el nuevo DNI: ")
            data = {'first_name': first_name, 'last_name': last_name, 'dni': dni}
            response = requests.put(f'http://localhost:3000/persons/{id}', json=data)
            if response.status_code == 200:
                print("Persona actualizada exitosamente")
            else:
                print("Error al actualizar la persona")
        elif choice == "2":
            id = input("Ingresa el ID de la sección que deseas actualizar: ")
            uc = input("Ingresa la nueva UC: ")
            semester = input("Ingresa el nuevo semestre: ")
            type = input("Ingresa el nuevo tipo (mandatory o elective): ")
            ht = input("Ingresa las nuevas horas teóricas: ")
            hp = input("Ingresa las nuevas horas prácticas: ")
            hl = input("Ingresa las nuevas horas de laboratorio: ")
            data = {'uc': uc, 'semester': semester, 'type': type, 'ht': ht, 'hp': hp, 'hl': hl}
            response = requests.put(f'http://localhost:3000/sections/{id}', json=data)
            if response.status_code == 200:
                print("Sección actualizada exitosamente")
            else:
                print("Error al actualizar la sección")
        elif choice == "3":
            id = input("Ingresa el ID de la escuela que deseas actualizar: ")
            name = input("Ingresa el nuevo nombre: ")
            description = input("Ingresa la nueva descripción: ")
            data = {'name': name, 'description': description}
            response = requests.put(f'http://localhost:3000/schools/{id}', json=data)
            if response.status_code == 200:
                print("Escuela actualizada exitosamente")
            else:
                print("Error al actualizar la escuela")
        elif choice == "4":
            id = input("Ingresa el ID de la facultad que deseas actualizar: ")
            name = input("Ingresa el nuevo nombre: ")
            description = input("Ingresa la nueva descripción: ")
            data = {'name': name, 'description': description}
            response = requests.put(f'http://localhost:3000/faculties/{id}', json=data)
            if response.status_code == 200:
                print("Facultad actualizada exitosamente")
            else:
                print("Error al actualizar la facultad")
        elif choice == "5":
            break
        else:
            print("Opción inválida")

    