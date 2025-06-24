"""
TELA DE INFORMAÇÕES ACADÊMICAS
Implementa o formulário para coleta de informações acadêmicas
"""

import flet as ft
from config import Config

class AcademicFormView:
    """
    Classe que constrói a tela do formulário acadêmico
    
    Esta view é responsável por exibir:
    - Campos para coletar informações acadêmicas
    - Opções de níveis de escolaridade e áreas de interesse
    - Botão para criar o roadmap personalizado
    """
    
    def __init__(self, controller):
        """
        Inicializa a view com uma referência ao controlador
        
        Args:
            controller: Instância do AuthController que gerencia o estado do formulário
        """
        self.controller = controller
        
        # Opções para os dropdowns
        self.niveis_escolaridade = [
            "Ensino Fundamental",
            "Ensino Médio",
            "Ensino Técnico",
            "Graduação em Andamento",
            "Graduação Completa",
            "Pós-graduação"
        ]
        
        self.areas_interesse = [
            "Desenvolvimento Web",
            "Ciência de Dados",
            "Automação",
            "Inteligência Artificial",
            "Desenvolvimento de Jogos",
            "Sistemas Embarcados",
            "Aplicações Desktop",
            "Aplicações Mobile"
        ]
        
        self.tempos_disponiveis = [
            "Menos de 5 horas por semana",
            "Entre 5 e 10 horas por semana",
            "Entre 10 e 20 horas por semana",
            "Mais de 20 horas por semana"
        ]
    
    def build(self) -> ft.Control:
        """
        Constrói toda a interface do formulário acadêmico
        
        Returns:
            Componente Flet que representa a tela completa do formulário
        """
        return ft.Column([
            self.build_header(),
            self.build_academic_form(),
        ], scroll=ft.ScrollMode.AUTO, spacing=20)
    
    def build_header(self) -> ft.Control:
        """
        Constrói o cabeçalho da tela
        
        Returns:
            Container com título e subtítulo da tela
        """
        return ft.Column([
            ft.Text(
                "Informações Acadêmicas",
                size=Config.FONT_SIZE_TITLE,
                weight=ft.FontWeight.BOLD,
                color=Config.COLORS['text_dark'],
                text_align=ft.TextAlign.CENTER,
                font_family=Config.TITLE_FONT
            ),
            ft.Text(
                "Vamos personalizar sua experiência de aprendizado",
                size=Config.FONT_SIZE_BODY,
                color=Config.COLORS['primary_blue'],
                text_align=ft.TextAlign.CENTER,
                font_family=Config.TEXT_FONT
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    def build_academic_form(self) -> ft.Control:
        """
        Constrói o formulário acadêmico
        
        Returns:
            Container com campos do formulário e botão de envio
        """
        # Dropdown de nível de escolaridade
        nivel_dropdown = ft.Dropdown(
            label="Nível de Escolaridade",
            options=[ft.dropdown.Option(nivel) for nivel in self.niveis_escolaridade],
            border_color=Config.COLORS['primary_blue'],
            color=Config.COLORS['text_dark'],
            focused_border_color=Config.COLORS['accent_gold'],
            width=350,
            on_change=lambda e: self.update_academic_field('nivel_escolaridade', e.control.value)
        )
        
        # Dropdown de área de interesse
        area_dropdown = ft.Dropdown(
            label="Área de Interesse",
            options=[ft.dropdown.Option(area) for area in self.areas_interesse],
            border_color=Config.COLORS['primary_blue'],
            color=Config.COLORS['text_dark'],
            focused_border_color=Config.COLORS['accent_gold'],
            width=350,
            on_change=lambda e: self.update_academic_field('area_interesse', e.control.value)
        )
        
        # Campo de objetivos
        objetivos_field = ft.TextField(
            label="Objetivos de Aprendizado",
            border_color=Config.COLORS['primary_blue'],
            color=Config.COLORS['text_dark'],
            focused_border_color=Config.COLORS['accent_gold'],
            multiline=True,
            min_lines=3,
            width=350,
            on_change=lambda e: self.update_academic_field('objetivos', e.control.value)
        )
        
        # Dropdown de tempo disponível
        tempo_dropdown = ft.Dropdown(
            label="Tempo Disponível para Estudos",
            options=[ft.dropdown.Option(tempo) for tempo in self.tempos_disponiveis],
            border_color=Config.COLORS['primary_blue'],
            color=Config.COLORS['text_dark'],
            focused_border_color=Config.COLORS['accent_gold'],
            width=350,
            on_change=lambda e: self.update_academic_field('tempo_disponivel', e.control.value)
        )
        
        # Botão de criar roadmap
        create_button = ft.ElevatedButton(
            text="Criar Roadmap",
            bgcolor=Config.COLORS['accent_gold'],
            color=Config.COLORS['text_dark'],
            style=ft.ButtonStyle(
                padding=ft.padding.all(15),
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            on_click=self.controller.handle_academic_submit
        )
        
        # Montar o formulário
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=nivel_dropdown,
                    alignment=ft.alignment.center
                ),
                ft.Container(height=15),
                ft.Container(
                    content=area_dropdown,
                    alignment=ft.alignment.center
                ),
                ft.Container(height=15),
                ft.Container(
                    content=objetivos_field,
                    alignment=ft.alignment.center
                ),
                ft.Container(height=15),
                ft.Container(
                    content=tempo_dropdown,
                    alignment=ft.alignment.center
                ),
                ft.Container(height=25),
                ft.Container(
                    content=create_button,
                    alignment=ft.alignment.center
                ),
            ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=4,
                color="#60000000",
                offset=ft.Offset(0, 2)
            )
        )
    
    def update_academic_field(self, field_name: str, value):
        """
        Atualiza os dados acadêmicos quando um campo é alterado
        
        Args:
            field_name: Nome do campo a ser atualizado
            value: Novo valor do campo
        """
        # Atualizar o objeto AcademicInfo no controlador
        if hasattr(self.controller.academic_data, field_name):
            setattr(self.controller.academic_data, field_name, value) 