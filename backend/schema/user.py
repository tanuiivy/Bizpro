from extensions import ma
from models.user import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True 

    id = ma.auto_field(dump_only=True)
    fullname = ma.auto_field(required=True)
    email = ma.auto_field(required=True)
    role = ma.auto_field(required=True)
    
    # Only needed for login – never shown in response
    password = fields.String(required=True, load_only=True)