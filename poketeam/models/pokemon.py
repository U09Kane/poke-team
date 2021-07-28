import peewee as pw

from .. import db


_IMAGE_API_BASE_URL = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full'


class PokemonDB(pw.Model):
    id: int
    number: int = pw.IntegerField(null=False)
    name: str = pw.CharField(max_length=50, null=False)
    type_primary: str = pw.CharField(max_length=10, null=False)
    type_secondary: str = pw.CharField(max_length=10)
    stats_sum: int = pw.IntegerField(null=False)
    hp: int = pw.IntegerField(null=False)
    attack: int = pw.IntegerField(null=False)
    attack_special: int = pw.IntegerField(null=False)
    defense: int = pw.IntegerField(null=False)
    defense_special: int = pw.IntegerField(null=False)
    speed: int = pw.IntegerField(null=False)
    generation: int = pw.IntegerField(null=False)
    is_legendary: bool = pw.BooleanField(default=True, null=False)

    class Meta:
        database = db
        table_name = 'Pokemon'

    @property
    def image_url(self):
        num = str(self.number).zfill(3)
        url = f'{_IMAGE_API_BASE_URL}/{num}.png'
        return url


db.create_tables([PokemonDB])
