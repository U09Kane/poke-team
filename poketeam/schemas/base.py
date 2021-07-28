from pydantic import BaseModel
from humps import camelize


def _to_camel(name: str) -> str:
    return camelize(name)


class CamelBaseSchema(BaseModel):
    """Base class for all subsequent schema/models that should convert the
    keys for the outgoing objects into camelCase format, as opposed to
    snake_case.
    """

    class Config:
        orm_mode = True
        alias_generator = _to_camel
        allow_population_by_field_name = True
