from services.api_service import APIService
from utils.data_validator import DataValidator
from utils.file_manager import FileManager


class Main:
    def __init__(self, api_service, data_validator, file_manager, items_per_page=10):
        self.api_service = api_service
        self.data_validator = data_validator
        self.file_manager = file_manager
        self.items_per_page = items_per_page

    def paginate(self, data):
        """Dividir los datos en páginas."""
        for i in range(0, len(data), self.items_per_page):
            yield data[i:i + self.items_per_page]

    def run(self):
        try:
            category = input("Ingresa una categoria: ").capitalize()
            data = self.api_service.get_data_by_category(category)

            if data:
                try:
                    self.data_validator.validate(data)

                    # Paginación de los datos
                    paginated_data = list(self.paginate(data))
                    current_page = 0
                    total_pages = len(paginated_data)

                    while True:
                        print(f"\nMostrando página {current_page + 1} de {total_pages}\n")

                        # Mostrar los datos de la página actual
                        for meal in paginated_data[current_page]:
                            print(f"{meal['strMeal']}")

                        # Pedir al usuario si desea avanzar o retroceder
                        command = input(
                            "\nIngresa 'n' para la siguiente página, 'p' para la página anterior, 'g' para guardar, o 'q' para salir: ").lower()

                        if command == 'n' and current_page < total_pages - 1:
                            current_page += 1
                        elif command == 'p' and current_page > 0:
                            current_page -= 1
                        elif command == 'g':
                            self.file_manager.save_to_json(data, f'{category}_meals.json')
                            self.file_manager.save_to_csv(data, f'{category}_meals.csv')
                            print("Datos guardados.")
                        elif command == 'q':
                            print("Saliendo.")
                            break
                        else:
                            print("Comando inválido o no hay más páginas.")
                except ValueError as e:
                    print(f"Error de validación: {e}")
            else:
                print(f"No se encontraron datos para la categoría: {category}")
        except KeyboardInterrupt:
            print("\nEjecución interrumpida por el usuario.")

if __name__ == '__main__':
    api_service = APIService('https://www.themealdb.com/api/json/v1/1/')
    data_validator = DataValidator()
    file_manager = FileManager()
    app = Main(api_service, data_validator, file_manager, items_per_page=5)
    app.run()