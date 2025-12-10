import json

def read_json_file(path):
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
    return data

def write_json_file(path, json_data):
    with open(path, 'w', encoding='utf-8' ) as json_file:
        json.dump(json_data, json_file, indent=4)

def get_user_info():
    try:        
        print('Ingrese los datos que a continuación se solicitan para agregar un pokemon al archivo')
        name = {}
        name['english'] = input('Nombre: ')
        
        type = input('Indique el tipo (si es mas de uno lo puede dividir por , ej: Fire,Water): ')

        base = {}
        base['hp'] = int(input('HP: '))
        base['attack'] = int(input('Attack: '))  
        base['defense'] = int(input('Defense: '))  
        base['sp_attack'] = int(input('Sp. Attack: '))  
        base['sp_defense'] = int(input('Sp. Defense: '))  
        base['speed'] = int(input('Speed: '))

        headers = ['name', 'type', 'base']
        result = {}
        
        for item in headers:
            if item == 'name':
                result[item] = name
            
            elif item == 'type':
                result[item] = type.split(',')
            
            else:
                result['base'] = base

        return result

    except ValueError as value_error:
         print(f'Error, se esperaba un valor numérico [ValueError]: {value_error}')  
    
    


def main():    
    try:
        pokemons = read_json_file('Pokemones.json')        
        new_pokemon = get_user_info()

        pokemons.append(new_pokemon)
        write_json_file('Pokemones.json', pokemons)

    except Exception as ex:
        print(f'Ha ocorrido un error inesperado. Detalle: {ex}')


if __name__ == '__main__':
    main()