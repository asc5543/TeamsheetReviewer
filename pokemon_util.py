"""Util for Pokemon information
Author: Justin Huang"""

STATS = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']
 
class Pokemon:
  """The Pokemon class with the information."""

  def __init__(self):
    self.name = ''
    self.gender = ''
    self.item = ''
    self.ability = ''
    self.tera_type = ''
    self.evs = {}
    self.ivs = {}
    self.nature = ''
    self.moves = []

    for stat in STATS:
      self.evs[stat] = 0
      self.ivs[stat] = 31

  def __str__(self):
    evs_str = ''
    ivs_str = ''
    for stat in STATS:
      if self.evs[stat] > 0:
        evs_str += f'{self.evs[stat]} {stat} / '
      if self.ivs[stat] < 31:
        ivs_str += f'{self.ivs[stat]} {stat} / '
    if len(evs_str) > 0:
      evs_str = evs_str[:len(evs_str)-3]
    if len(ivs_str) > 0:
      ivs_str = ivs_str[:len(ivs_str)-3]
    pokemon_info_str =  (f'{self.name} @ {self.item}\n'
                         f'Ability: {self.ability}\n'
                         f'Tera Type: {self.tera_type}\n')

    if len(evs_str) > 0:
      pokemon_info_str += f'EVs: {evs_str}\n'
    if len(ivs_str) > 0:
      pokemon_info_str += f'IVs: {ivs_str}\n'

    pokemon_info_str += f'{self.nature} Nature\n'

    for move in self.moves:
      pokemon_info_str += f'- {move}\n'

    return pokemon_info_str

  def set_name(self, name: str):
    self.name = name.strip()

  def set_gender(self, gender: str):
    self.gender = gender.strip()

  def set_item(self, item: str):
    self.item = item.strip()

  def set_ability(self, ability: str):
    self.ability = ability.strip()

  def set_tera_type(self, tera_type: str):
    self.tera_type = tera_type.strip()

  def set_nature(self, nature: str):
    self.nature = nature.strip()

  def set_evs(self, evs: str):
    evs_list = evs.split('/')
    for ev in evs_list:
      value, stat = ev.strip().split(' ')
      self.evs[stat] = int(value)

  def set_ivs(self, ivs: str):
    ivs_list = ivs.split('/')
    for iv in ivs_list:
      value, stat = iv.strip().split(' ')
      self.ivs[stat] = int(value)

  def append_move(self, move: str):
    if len(self.moves) < 4:
      self.moves.append(move.strip())
    else:
      print('Move is already 4!!!')

  def set_moves(self, moves: list[str]):
    for move in moves:
      self.moves.append(move)

if __name__ == '__main__':
  pokemon_a = Pokemon()
  pokemon_a.set_name('Rayquaza')
  pokemon_a.set_ability('Air Lock')
  pokemon_a.set_item('Clear Amulet')
  pokemon_a.set_tera_type('Normal')
  pokemon_a.set_nature('Adamant')
  pokemon_a.set_evs('252 Atk / 4 SpD / 252 Spe')
  pokemon_a.set_moves(['Dragon Ascent', 'Extreme Speed', 'Swords Dance', 'Protect'])
  pokemon_b = Pokemon()
  pokemon_b.set_name('Mienshao')
  pokemon_b.set_ability('Inner Focus')
  pokemon_b.set_item('Focus Sash')
  pokemon_b.set_tera_type('Fighting')
  pokemon_b.set_nature('Jolly')
  pokemon_b.set_evs('252 Atk / 4 SpD / 252 Spe')
  pokemon_b.set_moves(['Close Combat', 'Coaching', 'Wide Guard', 'Fake Out'])
  print(pokemon_a, '\n', pokemon_b)