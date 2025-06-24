"""
CONTROLADOR DE AUTENTICAÇÃO
Este arquivo gerencia as operações de autenticação e informações acadêmicas
"""

import flet as ft
from models.auth_models import UserRegistration, AcademicInfo
from config import Config, Messages

class AuthController:
    """
    Classe que controla as funcionalidades de autenticação e informações acadêmicas
    
    Responsável por:
    - Gerenciar o registro de usuários
    - Validar dados de formulário
    - Controlar o fluxo de navegação entre as telas de autenticação
    """
    
    def __init__(self, page: ft.Page, main_controller):
        """
        Inicializa o controlador de autenticação
        
        Args:
            page: Objeto Page do Flet que representa a janela principal
            main_controller: Referência ao AppController principal
        """
        self.page = page
        self.main_controller = main_controller
        self.registration_data = UserRegistration()
        self.academic_data = AcademicInfo()
    
    def handle_register(self, e):
        """
        Processa o formulário de cadastro e avança para tela acadêmica
        
        Args:
            e: Evento de clique no botão de cadastro
        """
        print("🔍 Botão de cadastro clicado!")
        print(f"Dados do formulário: {self.registration_data}")
        
        if self.registration_data.is_valid():
            print("✅ Dados válidos, navegando para o formulário acadêmico")
            self.main_controller.navigate_to_academic_form()
        else:
            print("❌ Dados inválidos, exibindo erro")
            self.show_validation_error("Preencha todos os campos corretamente")
    
    def handle_academic_submit(self, e):
        """
        Processa o formulário de informações acadêmicas e inicia o roadmap
        
        Args:
            e: Evento de clique no botão de envio
        """
        if self.academic_data.is_complete():
            self.main_controller.navigate_to_roadmap()
        else:
            self.show_validation_error("Complete todas as informações necessárias")
    
    def show_validation_error(self, message: str):
        """
        Exibe mensagem de erro de validação
        
        Args:
            message: Mensagem de erro a ser exibida
        """
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(
                message,
                color=Config.COLORS['error_red'],
                font_family=Config.INTERFACE_FONT,
                size=Config.FONT_SIZE_BODY
            ),
            bgcolor=Config.COLORS['error_bg'],
            action="OK"
        )
        self.page.snack_bar.open = True
        self.page.update() 