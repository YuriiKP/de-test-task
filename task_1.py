import json

def get_server_response():
    '''
    Имитируем ответ сервера 
    '''
    
    response = '''
    {
      "squadName": "Super hero squad",
      "homeTown": "Metro City",
      "formed": 2016,
      "secretBase": "Super tower",
      "active": true,
      "members": [
        {
          "name": "Molecule Man",
          "age": 29,
          "secretIdentity": "Dan Jukes",
          "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
        },
        {
          "name": "Madame Uppercut",
          "age": 39,
          "secretIdentity": "Jane Wilson",
          "powers": ["Million tonne punch", "Damage resistance", "Superhuman reflexes"]
        },
        {
          "name": "Eternal Flame",
          "age": 1000000,
          "secretIdentity": "Unknown",
          "powers": ["Immortality", "Heat Immunity", "Inferno", "Teleportation", "Interdimensional travel"]
        }
      ]
    }
    '''
    
    return json.loads(response)



def main():
    '''
    Получаем имена и суперсилы
    '''
    
    data = get_server_response()

    print('# --- Задание A')
    members_names = []
    for member in data['members']:
        members_names.append(member['name'])
    
    print(members_names)


    print('\n# --- Задание A')
    members_powers = {}
    for member in data['members']:
        name = member['name']
        powers = member['powers']
        members_powers[name] = powers
    
    print(members_powers)



if __name__ == "__main__":
    main()