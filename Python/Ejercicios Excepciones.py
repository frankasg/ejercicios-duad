def print_menu():
    print("""
          -------------------------------------------
          Menú de Opciones
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Borrar Resultado
          6. Salir
          -------------------------------------------
          """)

def try_to_get_actual_number_from_user():
    try:        
        actual_number = float(input("Digite un número con el cual desee realizar sus operaciones: "))     
        return True, actual_number        
    
    except ValueError as value_error:
        print(f"Error [ValueError]: El valor no corresponde a un numero. Detalle: {value_error}")
        return False, None

def get_menu_option():
    try:
        menu_option = int(input("Selecciona una las opciones anteriores: "))        

        if menu_option < 1 or menu_option > 6:
            print(f"La opción {menu_option} no corresponde a ninguna de las brindadas anteriormente. Por favor escoja una opción válida.")
        
        return menu_option
    
    except ValueError as value_error:
        print(f"Error [ValueError]: Opción inválida. Detalle: {value_error}")
        return 0

def add(value1, value2):
    return value1 + value2

def subtract(value1, value2):
    return value1 - value2

def multiply(value1, value2):
    return value1 * value2

def divide(value1, value2):
    try:
        return value1 / value2
    except ZeroDivisionError as e:
        print(f"Error [ZeroDivisionError]: Intentaste dividir un número entre 0. Detalles: {e}")
        return value1
    

def calculate_math_operation(operation, actual_number):    
    result = 0
    try:        
        new_number = float(input("Digite el nuevo número con el cual desea realizar la operacion: "))

        if operation == 1:
            result = add(actual_number, new_number)
               
        elif operation == 2:
            result = subtract(actual_number, new_number)
                    
        elif operation == 3:
            result = multiply(actual_number, new_number)
                    
        elif operation == 4:
            result = divide(actual_number, new_number)
    
    except ValueError as value_error:
        print(f"Error [ValueError]: El nuevo valor no corresponde a un valor válido. Detalle: {value_error}")    

    finally:
        return result

def main():
    actual_number = None
    try:
        
        display_menu = False

        while not display_menu:
            display_menu, actual_number = try_to_get_actual_number_from_user()

        program_terminated = False
        
        while not program_terminated:           
            print_menu()
            menu_option = get_menu_option()

            if menu_option == 5:
                actual_number = 0
                print(f"El valor del número actual es: {actual_number}")
                continue

            if menu_option == 6:
                program_terminated = True
                continue

            elif menu_option < 1 or menu_option > 6:
                continue
            
            actual_number = calculate_math_operation(menu_option, actual_number)

            print(f"El valor del número actual es: {actual_number}")

    
    except ValueError as value_error:
        print(f"Error [ValueError]: El valor inicial no corresponde a un valor válido. Detalle: {value_error}")

    except Exception as ex:
        print(f"Ha ocorrido un error inesperado. Detalle: {ex}")
         #estoy imprimiendo este error en pantalla pero para efectos practicos del ejercicio, ya que claramente no es el tipo de error que queremos mostrar en pantalla

if __name__ == "__main__":
    main()