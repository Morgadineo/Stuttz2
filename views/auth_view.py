"""
TELA DE LOGIN/CADASTRO
Implementa a interface de registro de usuário
"""

import flet as ft
from config import Config

class AuthView:
    """
    Classe que constrói a tela de login/cadastro
    
    Esta view é responsável por exibir:
    - Campos para cadastro de usuário
    - Validações visuais do formulário
    - Botão para submeter o cadastro
    """
    
    def __init__(self, controller):
        """
        Inicializa a view com uma referência ao controlador de autenticação
        
        Args:
            controller: Instância do AuthController que gerencia o estado do cadastro
        """
        self.controller = controller
    
    def build(self) -> ft.Control:
        """
        Constrói toda a interface de login/cadastro
        
        Returns:
            Componente Flet que representa a tela completa de autenticação
        """
        return ft.Column([
            self.build_header(),
            self.build_registration_form(),
        ], scroll=ft.ScrollMode.AUTO, spacing=20)
    
    def build_header(self) -> ft.Control:
        """
        Constrói o cabeçalho da tela de cadastro
        
        Returns:
            Container com título e subtítulo da tela
        """
        return ft.Column([
            ft.Text(
                "Bem-vindo ao Stuttz",
                size=Config.FONT_SIZE_TITLE,
                weight=ft.FontWeight.BOLD,
                color=Config.COLORS['text_dark'],
                text_align=ft.TextAlign.CENTER,
                font_family=Config.TITLE_FONT
            ),
            ft.Text(
                "Crie sua conta para começar sua jornada",
                size=Config.FONT_SIZE_BODY,
                color=Config.COLORS['primary_blue'],
                text_align=ft.TextAlign.CENTER,
                font_family=Config.TEXT_FONT
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    def build_registration_form(self) -> ft.Control:
        """
        Constrói o formulário de registro com todos os campos
        
        Returns:
            Container com campos do formulário e botão de cadastro
        """
        # Campo de nome completo
        nome_field = ft.TextField(
            label="Nome Completo",
            border_color=Config.COLORS['primary_blue'],
            color=Config.COLORS['text_dark'],
            focused_border_color=Config.COLORS['accent_gold'],
            on_change=lambda e: self.update_registration_field('nome', e.control.value)
        )
        
        # Campo de email
        email_field = ft.TextField(
            label="Email",
            border_color=Config.COLORS['primary_blue'],
            color=Config.COLORS['text_dark'],
            focused_border_color=Config.COLORS['accent_gold'],
            keyboard_type=ft.KeyboardType.EMAIL,
            on_change=lambda e: self.update_registration_field('email', e.control.value)
        )
        
        # Campo de senha
        password_field = ft.TextField(
            label="Senha",
            border_color=Config.COLORS['primary_blue'],
            color=Config.COLORS['text_dark'],
            focused_border_color=Config.COLORS['accent_gold'],
            password=True,
            can_reveal_password=True,
            on_change=lambda e: self.update_registration_field('senha', e.control.value)
        )
        
        # Campo de confirmar senha
        confirm_password_field = ft.TextField(
            label="Confirmar Senha",
            border_color=Config.COLORS['primary_blue'],
            color=Config.COLORS['text_dark'],
            focused_border_color=Config.COLORS['accent_gold'],
            password=True,
            can_reveal_password=True,
            on_change=lambda e: self.update_registration_field('confirmar_senha', e.control.value)
        )
        
        # Checkbox de aceitação dos termos
        terms_checkbox = ft.Checkbox(
            label="Aceito os termos de uso",
            value=False,
            on_change=lambda e: self.update_registration_field('aceita_termos', e.control.value)
        )
        
        # Botão de cadastro
        register_button = ft.ElevatedButton(
            text="Cadastre-se",
            bgcolor=Config.COLORS['accent_gold'],
            color=Config.COLORS['text_dark'],
            style=ft.ButtonStyle(
                padding=ft.padding.all(15),
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            on_click=self.controller.handle_register
        )
        
        # Montar o formulário
        return ft.Container(
            content=ft.Column([
                ft.Container(height=10),  # Espaçamento
                nome_field,
                ft.Container(height=10),  # Espaçamento
                email_field,
                ft.Container(height=10),  # Espaçamento
                password_field,
                ft.Container(height=10),  # Espaçamento
                confirm_password_field,
                ft.Container(height=10),  # Espaçamento
                terms_checkbox,
                ft.Container(height=20),  # Espaçamento maior
                register_button,
            ], spacing=5),
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
    
    def update_registration_field(self, field_name: str, value):
        """
        Atualiza os dados de registro quando um campo é alterado
        
        Args:
            field_name: Nome do campo a ser atualizado
            value: Novo valor do campo
        """
        # Atualizar o objeto UserRegistration no controlador
        if hasattr(self.controller.registration_data, field_name):
            setattr(self.controller.registration_data, field_name, value) 