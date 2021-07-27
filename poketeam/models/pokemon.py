import peewee as pw

from .. import db


class PokemonDB(pw.Model):
    id: int
    number: int = pw.IntegerField(null=False, unique=True)
    name: str = pw.CharField(max_length=50, null=False)
    type_primary: str = pw.CharField(max_length=10, null=False)
    type_secondary: str = pw.CharField(max_length=10)
    stats_sum: int = pw.IntegerField(null=False)
    hp: int = pw.IntegerField(null=False)
    attack: int = pw.IntegerField(null=False)
    attack_special: int = pw.IntegerField(null=False)
    defense: int = pw.IntegerField(null=False)
    defense_sepecial: int = pw.IntegerField(null=False)
    speed: int = pw.IntegerField(null=False)
    generation: int = pw.IntegerField(null=False)
    is_legendary: pw.BooleanField(default=True, null=False)

    class Meta:
        database = db
        table_name = 'Pokemon'


db.create_tables([PokemonDB])
