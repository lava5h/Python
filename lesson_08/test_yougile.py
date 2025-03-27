import pytest

# Данные для авторизации
token = "..."

# URL для создания проекта
url = "https://ru.yougile.com/"

# Создание проектов
from pages.page_yougile import CreateProjects

def test_create_positive():
    
    create_project = CreateProjects(url, token)
    response = create_project.create_project_positive(url)

    # Проверка статуса ответа
    assert response.status_code == 201
    return create_project

if __name__ == "__main__":
    test_create_positive()

def test_create_negative():
    
    create_project = CreateProjects(url, token)
    response = create_project.create_project_negative(url)

    # Проверка статуса ответа
    assert response.status_code == 400

if __name__ == "__main__":
    test_create_negative()

from pages.page_yougile import ChangeProjects    

def test_change_positive():

    create_project = test_create_positive()
    project_id = create_project.project_id
    
    change_project = ChangeProjects(project_id, url, token)
    response = change_project.change_project_positive(url)
    
    # Проверка статуса ответа
    assert response.status_code == 200

if __name__ == "__main__":
    test_change_positive()

def test_change_negative():

    create_project = test_create_positive()
    project_id = create_project.project_id
    
    change_project = ChangeProjects(project_id, url, token)
    response = change_project.change_project_negative(url)
    
    # Проверка статуса ответа
    assert response.status_code == 400

if __name__ == "__main__":
    test_change_negative()

from pages.page_yougile import GetProjects 

def test_get_positive():

    create_project = test_create_positive()
    project_id = create_project.project_id
    
    get_project = GetProjects(project_id, url, token)
    response = get_project.get_project_positive(url)
    
    # Проверка статуса ответа
    assert response.status_code == 200

if __name__ == "__main__":
    test_get_positive()

def test_get_negative():

    create_project = test_create_positive()
    project_id = create_project.project_id
    
    get_project = GetProjects(project_id, url, token)
    response = get_project.get_project_negative(url)
    
    # Проверка статуса ответа
    assert response.status_code == 404

if __name__ == "__main__":
    test_get_negative()
