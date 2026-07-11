# Código sucio - Guardar como citas_sucio.py

# Estructura simplificada para el catálogo de precios
PRECIOS_ESPECIALIDADES = {
    "Cardiologia": 150.0,
    "Pediatria": 90.0,
    "Dermatologia": 110.0
}

# Patrón: Extraer Método para el Reporte
def imprimir_comprobante(cita_id, paciente, especialidad, precio_base, costo_final):
    print("=== COMPROBANTE DE CITA ===")
    print("ID: " + cita_id)
    print("Paciente: " + paciente)
    print("Especialidad: " + especialidad)
    print(f"Costo Base: S/. {precio_base:.2f}")
    print(f"Total a Pagar: S/. {costo_final:.2f}")
    print("---------------------------\n")

# Patrón: Renombrar Variables en la firma y parámetros
def registrar_cita(lista_citas, paciente, especialidad, tiene_seguro):
    
    # Patrón: Simplificar Condicionales (Validación de Especialidad)
    if especialidad not in PRECIOS_ESPECIALIDADES:
        print(f"Error: Especialidad {especialidad} no disponible.\n")
        return

    # Patrón: Simplificar Condicionales (Asignación de costo base)
    precio_base = PRECIOS_ESPECIALIDADES[especialidad]
    
    # Cálculo de descuento por seguro
    costo_final = precio_base
    if tiene_seguro == "S":
        costo_final = precio_base * 0.20 # 80% de descuento por seguro

    # Guardar en la lista usando estructura descriptiva
    cita_id = "CITA-" + str(len(lista_citas) + 1)
    lista_citas.append({
        "id": cita_id, 
        "paciente": paciente, 
        "especialidad": especialidad, 
        "tiene_seguro": tiene_seguro
    })

    # Llamada al método extraído
    imprimir_comprobante(cita_id, paciente, especialidad, precio_base, costo_final)


# Datos de prueba para ejecución
lista_citas = []
registrar_cita(lista_citas, "Juan Perez", "Cardiologia", "S")
registrar_cita(lista_citas, "Maria Lopez", "Pediatria", "N")
registrar_cita(lista_citas, "Luis Gomez", "Oftalmologia", "N") # Error esperado

