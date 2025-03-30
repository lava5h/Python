import pytest
from pages.page_yougile import CreateProjects
from pages.page_yougile import ChangeProjects 
from pages.page_yougile import GetProjects

# Данные для авторизации
token = "FExXjke2GyQGH3w2N9jopal13Ji68dPb64EAE7I3yUj--LC1+Y-E3CtABUDyj29J"

# URL для создания проекта
url = "https://ru.yougile.com/"

# Создание проекта
def test_create_positive():
    
    create_project = CreateProjects(url, token)
    response = create_project.create_project_positive(url)

    # Проверка статуса ответа
    assert response.status_code == 201
    response_body = response.json()
    assert "id" in response_body
    assert isinstance(response_body["id"], str)
    return create_project

def test_create_negative():
    
    create_project = CreateProjects(url, token)
    response = create_project.create_project_negative(url)

    # Проверка статуса ответа
    assert response.status_code == 400  

# Изменение проекта
def test_change_positive():

    create_project = test_create_positive()
    project_id = create_project.project_id
    
    change_project = ChangeProjects(project_id, url, token)
    response = change_project.change_project_positive(url)
    
    # Проверка статуса ответа
    assert response.status_code == 200
    response_body = response.json()
    assert "id" in response_body
    assert isinstance(response_body["id"], str)

def test_change_negative():

    create_project = test_create_positive()
    project_id = create_project.project_id
    
    change_project = ChangeProjects(project_id, url, token)
    response = change_project.change_project_negative(url)
    
    # Проверка статуса ответа
    assert response.status_code == 400 

# Получения информации проекта
def test_get_positive():

    create_project = test_create_positive()
    project_id = create_project.project_id
    
    get_project = GetProjects(project_id, url, token)
    response = get_project.get_project_positive(url)
    
    # Проверка статуса ответа
    assert response.status_code == 200
    response_body = response.json()
    assert "id" in response_body
    assert isinstance(response_body["id"], str)

def test_get_negative():

    create_project = test_create_positive()
    project_id = create_project.project_id
    
    get_project = GetProjects(project_id, url, token)
    response = get_project.get_project_negative(url)
    
    # Проверка статуса ответа
    assert response.status_code == 404
