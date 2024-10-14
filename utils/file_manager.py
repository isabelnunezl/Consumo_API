import json

class FileManager:
    @staticmethod
    def save_to_json(data, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)  # 'ensure_ascii=False' guarda los caracteres no ASCII correctamente
            print(f"Datos guardados en {filename} (JSON)")
        except Exception as e:
            print(f"Error al guardar los datos en {filename}: {e}")