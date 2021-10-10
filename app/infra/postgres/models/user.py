from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    created_date = fields.DatetimeField(auto_now_add=True)
