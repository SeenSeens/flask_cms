# import hashlib
#
# from app import db
# from app.models.users import User, UserRole
#
#
# def add_user(name, username, password, **kwargs):
#     password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#     user = User(name=name.strip(),
#                 username=username.strip(),
#                 password=password,
#                 email=kwargs.get('email'),
#                 avatar=kwargs.get('thumbnail'))
#     db.session.add(user)
#     db.session.commit()
#
# def check_login(username, password):
#     if username and password:
#         password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#         return User.query.filter_by(username=username.strip(), password=password.strip()).first()
#
# def get_user_by_id(user_id):
#     return User.query.get(id=user_id).first()
#
# def update_user(user_id, name, username, email, password=None, avatar=None, user_role=None):
#     user = User.query.get(user_id)
#     if user:
#         user.name = name.strip()
#         user.username = username.strip()
#         user.email = email.strip()
#         user.user_role = UserRole(int(user_role))
#         if password:
#             user.password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
#         if avatar:
#             user.thumbnail = avatar
#         db.session.commit()
#     return user