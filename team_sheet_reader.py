"""Pokepast reader.
Author: Justin Huang"""

import re
import pokemon_util

from urllib.request import urlopen

KEYWORD = ['Ability', 'Tera Type', 'EVs', 'IVs']

TESTDATA = '\nRayquaza @ Clear Amulet  \nAbility: Air Lock  \nLevel: 50  \nShiny: Yes  \nTera Type: Normal  \nEVs: 252 Atk / 4 SpD / 252 Spe  \nAdamant Nature  \n- Dragon Ascent  \n- Extreme Speed  \n- Swords Dance  \n- Protect  \n'

def pokepast_parser(url: str) -> str:
  """The pokepast parser.

  Args:
    url: The URL of pokepast

  Returns:
    The list of pokemon in the team sheet.
  """
  team_member_list = []
  pokepast_page = urlopen(url)
  if pokepast_page.getcode() == 200:
    data = pokepast_page.read().decode('utf-8')
    data_list = data.split('<article>')
    del data_list[0]
    data_list.pop()
    for pokemon in data_list:
      pokemon = re.sub(r'<[a-zA-Z0-9-"/=\+\s\.]+>', '', pokemon).replace('\t', '').replace('\n\n', '')
      team_member_list.append(pokemon + '\n')
  else:
    print("Error!")

  return team_member_list

def convert_str_to_pokemon(poke_info: str) -> pokemon_util.Pokemon:
  poke_info_list = poke_info.split('\n')
  pokemon = pokemon_util.Pokemon()
  for info in poke_info_list:
    if ' @ ' in info:
      name, item = info.split(' @ ')
      pokemon.set_name(name)
      pokemon.set_item(item)
    elif 'Ability: ' in info:
      ability = info.replace('Ability: ', '')
      pokemon.set_ability(ability)
    elif 'Tera Type: ' in info:
      tera_type = info.replace('Tera Type: ', '')
      pokemon.set_tera_type(tera_type)
    elif 'EVs: ' in info:
      evs = info.replace('EVs: ', '')
      pokemon.set_evs(evs)
    elif 'IVs: ' in info:
      ivs = info.replace('IVs: ', '')
      pokemon.set_ivs(ivs)
    elif 'Nature' in info:
      nature = info.replace('Nature', '')
      pokemon.set_nature(nature)
    elif '-' in info:
      move = info.replace('-', '')
      pokemon.append_move(move)
  #print(pokemon)
  return pokemon

if __name__ == "__main__":
  team_member = pokepast_parser('https://pokepast.es/ffe04ea7dc0b46d3')
  for pokemon in team_member:
    convert_str_to_pokemon(pokemon)