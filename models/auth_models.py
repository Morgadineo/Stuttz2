from dataclasses import dataclass
from typing import Optional

@dataclass
class UserRegistration:
    nome: str = ""
    email: str = ""
    senha: str = ""
    confirmar_senha: str = ""
    aceita_termos: bool = False
    
    def is_valid(self) -> bool:
        # Validações básicas para protótipo
        return all([
            self.nome.strip(),
            self.email.strip() and "@" in self.email,
            self.senha and len(self.senha) >= 6,
            self.senha == self.confirmar_senha,
            self.aceita_termos
        ])

@dataclass  
class AcademicInfo:
    nivel_escolaridade: str = ""
    area_interesse: str = ""
    objetivos: str = ""
    tempo_disponivel: str = ""
    
    def is_complete(self) -> bool:
        return all([self.nivel_escolaridade, self.area_interesse, self.tempo_disponivel]) 