def despedir_con_nombre(nombre: str = "") -> str:
    """Devuelve un mensaje de despedida personalizado."""
    if not nombre:
        nombre = "desconocido"
    return f"Adiós, {nombre}"

def test_despedir_con_nombre_incluye_nombre():
    assert "Alex" in despedir_con_nombre("Alex")

def test_despedir_sin_nombre_usa_desconocido():
    assert "desconocido" in despedir_con_nombre()