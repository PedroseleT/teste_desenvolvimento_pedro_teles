CLASSES = {"classes": [{"name": "A"}, 
                       {"name": "B"}, 
                       {"name": "C"}, 
                       {"name": "D"}, 
                       {"name": "E"}, 
                       {"name": "F"}]}
DEGREES = [
    {"id": 1, "name": "Ensino Fundamental"}, {"id": 2, "name": "1° ano do ensino médio"},
    {"id": 3, "name": "2° ano ensino médio"}, {"id": 4, "name": "3° ano do ensino médio"},
    {"id": 5, "name": "Cursinho"}, {"id": 8, "name": "4º ano do ensino fundamental"},
    {"id": 9, "name": "5º ano do ensino fundamental"}, {"id": 10, "name": "6º ano do ensino fundamental"},
    {"id": 11, "name": "7º ano do ensino fundamental"}, {"id": 12, "name": "8º ano do ensino fundamental"},
    {"id": 13, "name": "9º ano do ensino fundamental"}, {"id": 6, "name": "Estudo em casa"}, {"id": 7, "name": "Outros"}
]
MATTERS = [{"id": 1, "name": "Matemática"}, {"id": 2, "name": "Português"}, {"id": 3, "name": "História"}, {"id": 4, "name": "Geografia"}]
TEACHERS = [{"id": 1, "name": "Professor 1"}, {"id": 2, "name": "Professor 2"}, {"id": 3, "name": "Professor 3"}, {"id": 4, "name": "Professor 4"}, {"id": 5, "name": "Professor 5"}, {"id": 6, "name": "Professor 6"}]

# Listas mutáveis 
students_db = [
    {"id": 1, "ra": 12346, "name": "Nome do aluno 1", "degreeId": 1, "classId": 0},
    {"id": 2, "ra": 456798, "name": "Nome do aluno 2", "degreeId": 2, "classId": 0},
    {"id": 3, "ra": 752156, "name": "Nome do aluno 3", "degreeId": 3, "classId": 1},
    {"id": 4, "ra": 852348, "name": "Nome do aluno 4", "degreeId": 4, "classId": 1},
    {"id": 5, "ra": 454643, "name": "Nome do aluno 5", "degreeId": 6, "classId": 1}
]

relationships_db = [
    {"id": 1, "teacherId": 1, "matterId": 1, "degrees": [{"degreeId": 1, "classes": [{"classPosition": 0}, {"classPosition": 1}]}]},
    {"id": 2, "teacherId": 2, "matterId": 2, "degrees": [{"degreeId": 8, "classes": [{"classPosition": 0}]}]}
]