#Importando o pytest e os modelos do sistema
import pytest
from models.user_system import UserSystem
from models.user import User

# CT01 - Realizar a entrada de um usuário que está dentro dos requisitos do cadastro esperando um sucesso
def test_register_valid_user():
    us = UserSystem()
    user = us.register_user("João", "joao.email@site.com", "joao2024")
    assert user.email == "joao.email@site.com"
    assert us.total_users() == 1

# CT02 — Tentativa de cadastro de um usuário com o e-mail errado esperando erro de e-mail inválido
def test_register_user_invalid_email():
    us = UserSystem()
    with pytest.raises(ValueError, match="E-mail inválido."):
        us.register_user("Lara", "lara@site", "lara123")

# CT03 — Tentativa de cadastro de um usuário com a senha fraca, esperando erro de Senha Fraca
def test_register_user_weak_password():
    us = UserSystem()
    with pytest.raises(ValueError, match="Senha fraca."):
        us.register_user("Mika", "mika@email.com", "senha")

# CT04 — Tentativa de buscar Usuário por Email
def test_find_user_by_email():
    us = UserSystem()
    us.register_user("Paulo", "paulo@email.com", "paulo2024")
    user = us.find_user_by_email("paulo@email.com")
    assert user is not None
    assert user.name == "Paulo"

# CT05 — Tentativa de mostrar total de Usuários
def test_total_users_count():
    us = UserSystem()
    us.register_user("Ana", "ana@email.com", "ana123")
    us.register_user("Bruno", "bruno@email.com", "bruno456")
    us.register_user("Carla", "carla@email.com", "carla789")
    assert us.total_users() == 3
