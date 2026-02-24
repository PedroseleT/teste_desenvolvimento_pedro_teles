from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
import data_store as ds
import services as sv

console = Console()

def mostrar_tela_1():

    while True:
        console.clear()
        table = Table(title="Relatório de Alunos (Tela 1)")
        table.add_column("ID", style="cyan")
        table.add_column("Nome", style="magenta")
        table.add_column("Grau (Degree)", style="green")
        table.add_column("Turma (Class)", style="yellow")

        for s in ds.students_db:
            table.add_row(
                str(s['id']), 
                s['name'], 
                sv.get_degree_name(s['degreeId']), 
                sv.get_class_name(s['classId'])
            )
        
        console.print(table)
        console.print("\n[1] Editar Aluno [2] Gerar +300 Alunos [0] Voltar")
        op = Prompt.ask("Escolha", choices=["1", "2", "0"], show_choices=False)

        if op == "1":
            try:
                id_edit = int(Prompt.ask("Digite o ID do aluno que deseja editar"))
                
                aluno = next((s for s in ds.students_db if s['id'] == id_edit), None)
                
                if aluno:
                    console.print(Panel(f"Editando: [bold]{aluno['name']}[/]\nO que você deseja alterar?"))
                    console.print("[1] Nome\n[2] Classe (Turma)\n[0] Cancelar")
                    sub_op = Prompt.ask("Escolha", choices=["1", "2", "0"], show_choices=False)

                    if sub_op == "1":
                        aluno['name'] = Prompt.ask("Digite o novo nome", default=aluno['name'])
                        console.print("[bold green]Nome atualizado![/]")
                    
                    elif sub_op == "2":
                        opcoes_validas = [str(i) for i in range(len(ds.CLASSES['classes']))]
                        while True:
                            nova_classe = Prompt.ask(
                                f"Nova Class ID ({'/'.join(opcoes_validas)})", 
                                default=str(aluno['classId'])
                            )
                            if nova_classe in opcoes_validas:
                                aluno['classId'] = int(nova_classe)
                                console.print("[bold green]Classe atualizada![/]")
                                break
                            else:
                                console.print("[bold red]Opção inválida![/]")
                    
                    Prompt.ask("Pressione Enter para continuar")
                else:
                    console.print(f"[bold red]Aluno com ID {id_edit} não encontrado.[/]")
                    Prompt.ask("Pressione Enter para continuar")

            except ValueError:
                console.print("[bold red]Erro: O ID deve ser um número.[/]")
                Prompt.ask("Pressione Enter para tentar novamente")

        elif op == "2":
            sv.generate_300_students()

        elif op == "0":
            break

def mostrar_tela_2():

    while True:
        console.clear()
        table = Table(title="Relatório de Professores (Tela 2)")
        table.add_column("Professor", style="cyan")
        table.add_column("Matéria", style="magenta")
        table.add_column("Degrees/Classes", style="yellow")

        for rel in ds.relationships_db:
            try:
                teacher = next(t['name'] for t in ds.TEACHERS if t['id'] == rel['teacherId'])
                matter = next(m['name'] for m in ds.MATTERS if m['id'] == rel['matterId'])
                
                info_clash = ""
                for d in rel['degrees']:
                    deg_name = sv.get_degree_name(d['degreeId'])
                    classes_names = [sv.get_class_name(c.get('classPosition', c.get('classId'))) for c in d['classes']]
                    info_clash += f"{deg_name}: ({', '.join(classes_names)})\n"
                
                table.add_row(teacher, matter, info_clash.strip())
            except StopIteration:
                continue
        
        console.print(table)
        console.print("\n[1] Ver Alunos por Degree [2] Adicionar Relacionamento [0] Voltar")
        op = Prompt.ask("Escolha", choices=["1", "2", "0"], show_choices=False)

        if op == "1":
            try:
                deg_id = int(Prompt.ask("Digite o ID do Degree para filtrar alunos"))
                alunos_filtrados = [s['name'] for s in ds.students_db if s['degreeId'] == deg_id]
                
                if alunos_filtrados:
                    console.print(Panel(f"Alunos encontrados: {', '.join(alunos_filtrados)}", title="Resultado"))
                else:
                    console.print("[bold yellow]Nenhum aluno matriculado neste Degree.[/]")
                Prompt.ask("Pressione Enter para continuar")
            except ValueError:
                console.print("[bold red]ID inválido![/]")

        elif op == "2":
            try:
                t_id = int(Prompt.ask("ID do Professor"))
    
                if not any(t['id'] == t_id for t in ds.TEACHERS):
                    console.print("[bold red]Erro: Este Professor não existe![/]")
                    Prompt.ask("Pressione Enter para voltar")
                    continue

                m_id = int(Prompt.ask("ID da Matéria"))
                if not any(m['id'] == m_id for m in ds.MATTERS):
                    console.print("[bold red]Erro: Esta Matéria não existe![/]")
                    Prompt.ask("Pressione Enter para voltar")
                    continue

                d_id = int(Prompt.ask("ID do Degree"))
                if not any(d['id'] == d_id for d in ds.DEGREES):
                    console.print("[bold red]Erro: Este Degree não existe![/]")
                    Prompt.ask("Pressione Enter para voltar")
                    continue

                new_id = len(ds.relationships_db) + 1
                ds.relationships_db.append({
                    "id": new_id, 
                    "teacherId": t_id, 
                    "matterId": m_id,
                    "degrees": [{"degreeId": d_id, "classes": [{"classPosition": 0}]}]
                })
                console.print("[bold green]Relacionamento adicionado com sucesso![/]")
                Prompt.ask("Pressione Enter para continuar")

            except ValueError:
                console.print("[bold red]Erro: Digite apenas números para os IDs![/]")
                Prompt.ask("Pressione Enter para continuar")

        elif op == "0":
            break

def menu_principal():

    while True:
        console.clear()
        console.print(Panel.fit("SISTEMA DE GESTÃO ESCOLAR - TESTE TECNICO", style="bold blue"))
        console.print("[1] Tela 1 (Alunos)\n[2] Tela 2 (Professores)\n[0] Sair")
        
        escolha = Prompt.ask("Selecione uma opção", choices=["1", "2", "0"], show_choices=False)
        
        if escolha == "1":
            mostrar_tela_1()
        elif escolha == "2":
            mostrar_tela_2()
        elif escolha == "0":
            console.print("[bold cyan]Saindo do sistema... Até logo![/]")
            break

if __name__ == "__main__":
    menu_principal()