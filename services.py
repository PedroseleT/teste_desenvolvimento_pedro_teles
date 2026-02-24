import random
from data_store import students_db, DEGREES, CLASSES
from rich.console import Console
from rich.table import Table
from rich.bar import Bar

console = Console()

def get_degree_name(degree_id):
    for d in DEGREES:
        if d['id'] == degree_id:
            return d['name']
    return "N/A"

def get_class_name(class_id):
    try:
        # Pega o nome da classe pelo índice/posição
        return CLASSES['classes'][class_id]['name']
    except (IndexError, KeyError, TypeError):
        return "N/A"

def generate_300_students():
    # Pega o último ID para continuar a contagem
    current_id = max([s['id'] for s in students_db]) if students_db else 0
    
    for i in range(1, 301):
        new_student = {
            "id": current_id + i,
            "ra": random.randint(100000, 999999),
            "name": f"Estudante Gerado {current_id + i}",
            "degreeId": random.choice(DEGREES)['id'],
            "classId": random.randint(0, len(CLASSES['classes']) - 1)
        }
        students_db.append(new_student)
    
    plot_student_distribution_terminal()

def plot_student_distribution_terminal():
    """Gera um gráfico visual usando barras do Rich no terminal"""
    table = Table(title="[bold blue]Distribuição de Alunos por Degree[/]", show_header=True, header_style="bold magenta")
    table.add_column("Degree (Série)", style="cyan")
    table.add_column("Qtd", justify="right", style="green")
    table.add_column("Gráfico", width=40)

    # Conta os alunos por degree
    distribuicao = []
    for deg in DEGREES:
        count = len([s for s in students_db if s['degreeId'] == deg['id']])
        distribuicao.append({"name": deg['name'], "count": count})

    # Encontra o maior valor para escalar as barras proporcionalmente
    max_alunos = max([d['count'] for d in distribuicao]) if distribuicao else 1

    for item in distribuicao:
        # Criando barra visual baseada no total de alunos
        bar_visual = Bar(size=max_alunos, begin=0, end=item['count'], color="green")
        table.add_row(
            item['name'], 
            str(item['count']), 
            bar_visual
        )

    console.print("\n")
    console.print(table)
    input("\n[Pressione Enter para continuar...]")