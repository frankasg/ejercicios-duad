import csv

def print_menu():
    print("""
          -------------------------------------------
          Menú de Opciones
          1. Agregar juego
          2. Generar CSV
          3. Generar CSV con tabulaciones
          4. Salir
          -------------------------------------------
          """)
    
def get_menu_option():
    try:
        menu_option = int(input("Selecciona una las opciones anteriores: "))        

        if menu_option < 1 or menu_option > 4:
            print(f"La opción {menu_option} no corresponde a ninguna de las brindadas anteriormente. Por favor escoja una opción válida.")
        
        return menu_option
    
    except ValueError as value_error:
        print(f"Error [ValueError]: Opción inválida. Detalle: {value_error}")
        return 0
    
def get_new_game_properties():    
    user_input = input("Para agregar un nuevo juego brinde la siguiente información separada por comas [Nombre,Género,Desarrolador,Clasificación ESRB]: ")
    game_properties = user_input.split(",")

    if(len(game_properties) != 4):
        print(f"La información proporcionada no coincide con el ejemplo brindado. Ej: [Nombre,Género,Desarrolador,Clasificación ESRB]")    
        return []
    
    return game_properties

def add_game(games, headers, game_properties):
    game = {}
    for index in range(len(headers)):
        game[headers[index]] = game_properties[index].strip()
    
    games.append(game)
    return games

def generate_CSV(games, headers, delimiter):
    with open("Games.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, headers, delimiter = delimiter) 
        writer.writeheader()
        writer.writerows(games)
    
    print("El archivo CSV ha sido creado con el nombre de Games")

def main():    
    try:
        program_terminated = False
        headers = ["Nombre", "Género", "Desarrollador", "Clasificación ESRB"]
        games = []

        while not program_terminated:     
            print_menu()
            menu_option = get_menu_option()            

            if menu_option == 1:
                game_properties = get_new_game_properties()

                if len(game_properties) != 0:
                    add_game(games, headers, game_properties)
            
            elif menu_option == 2:
                generate_CSV(games, headers, ",")
            
            elif menu_option == 3:
                generate_CSV(games, headers, "\t")

            elif menu_option == 4:
                program_terminated = True
                continue
    
    except Exception as ex:
        print(f"Ha ocorrido un error inesperado. Detalle: {ex}")


if __name__ == "__main__":
    main()