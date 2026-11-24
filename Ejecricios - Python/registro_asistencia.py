def registro_asistencia(nombre, estado):
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser tipo Texto")

    if nombre.strip() == "":
        raise ValueError("El nombre no debe estar vacio")

    if estado not in ("Presente", "Ausente", "Tardanza"):
        raise ValueError("El estado no es valido")

    return f"Asistencia registrada: {nombre} - {estado}"

test = [
    ("Jose", "Ausente"),
    ("", "Presente"),
    ("Manuel", "Enfermo"),
    (123, "Tardanza"),
    ("Pedro", "Tardanza")
]

for nombre, estado in test:
    try:
        print(registro_asistencia(nombre, estado))
    except (ValueError, TypeError) as error:
        print("Error:", error)