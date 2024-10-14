import requests

class APIService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data_by_category(self, category):
        try:
            url = f"{self.base_url}/filter.php"
            params = {'c': category}
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get('meals', [])
        except requests.exceptions.HTTPError as http_err:
            print(f"Error de HTTP: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Error de conexión: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Error de tiempo de espera: {timeout_err}")
        except Exception as err:
            print(f"Ocurrió un error: {err}")
        return []