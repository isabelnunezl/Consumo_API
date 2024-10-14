class DataValidator:
    @staticmethod
    def validate(data):
        if not isinstance(data, list):
            raise ValueError("Formato de datos no válido: Se esperaba una lista.")
        for item in data:
            if 'idMeal' not in item or 'strMeal' not in item:
                raise ValueError(f"Faltan campos requeridos en: {item}")
        return True
