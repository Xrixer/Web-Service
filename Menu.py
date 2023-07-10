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



    