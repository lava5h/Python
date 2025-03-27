import requests

# Создание проектов
class CreateProjects:
    
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.project_id = None

    project_data_positive = {
        "title": "Проект",
        "users": {
            "4d3940ce-41a6-402d-8070-ec00024891e6": "admin"
        }
    }

    project_data_negative = {
        "title": "",
        "users": {
            "4d3940ce-41a6-402d-8070-ec00024891e6": "admin"
        }
    }
    
    # Функция создания проекта (позитивный)
    def create_project_positive(self, url):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "/api-v2/projects", headers=headers, json=self.project_data_positive)
        self.project_id = response.json()["id"]
        return response
    
    # Функция создания проекта (негативный)
    def create_project_negative(self, url):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "/api-v2/projects", headers=headers, json=self.project_data_negative)
        return response

# Изменение проектов
class ChangeProjects:
    def __init__(self, project_id, url, token):
        self.project_id = project_id
        self.url = url
        self.token = token

    project_data_positive = {
        "title": "Новый проект",
    }

    project_data_negative = {
        "title": "",
    }

# Функция редактирования проекта (позитивный)
    def change_project_positive(self, url):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        response = requests.put(url + "/api-v2/projects/" + self.project_id, headers=headers, json=self.project_data_positive)
        return response
    
# Функция редактирования проекта (негативный)
    def change_project_negative(self, url):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        response = requests.put(url + "/api-v2/projects/" + self.project_id, headers=headers, json=self.project_data_negative)
        return response
    
# Получение информации по id
class GetProjects:
    def __init__(self, project_id, url, token):
        self.project_id = project_id
        self.url = url
        self.token = token

    # Функция получения информации (позитивный)
    def get_project_positive(self, url):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url + "/api-v2/projects/" + self.project_id, headers=headers)
        return response
    
    # Функция получения информации (негативный) с неверным id
    def get_project_negative(self, url):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url + "/api-v2/projects/" + "36eff4324ft", headers=headers)
        return response
