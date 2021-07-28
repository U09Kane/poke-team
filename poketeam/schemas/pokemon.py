from .base import CamelBaseSchema


class PokemonBase(CamelBaseSchema):
    number: int
    name: str
    type_primary: str
    type_secondary: str
    stats_sum: int
    hp: int
    attack: int
    attack_special: int
    defense: int
    defense_special: int
    speed: int
    generation: int
    is_legendary: bool
    image_url: str


class Pokemon(PokemonBase):
    id: int
