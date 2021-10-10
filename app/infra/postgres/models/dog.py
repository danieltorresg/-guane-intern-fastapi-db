from tortoise import fields, models
from tortoise.fields.base import SET_NULL


class Dog(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True)
    picture = fields.CharField(max_length=255, default="string")
    is_adopted = fields.BooleanField(default=True)
    created_date = fields.DatetimeField(auto_now_add=True)
    owner = fields.ForeignKeyField(
        "models.User",
        related_name="owner",
        on_delete=SET_NULL,
        null=True,
    )
    in_charge = fields.ForeignKeyField(
        "models.User",
        related_name="in_charge",
        on_delete=SET_NULL,
        null=True,
    )
