from flask import request, jsonify, make_response, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from Adapters.DTO.userDTO import UserDTO
from Application.Services.userAuthentication import UserAuth
AuthBP = Blueprint('auth', __name__)

@AuthBP.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        #return jsonify({'error': 'Nombre de usuario y contraseña requeridos'}),400
        return jsonify(data),400
    userDto=UserDTO(userID=data["userID"], username=data["username"],password=data["password"])
    user_service = UserAuth()  
    user = user_service.registerUser(userDto)
    return jsonify({'message': 'Usuario registrado exitosamente'})

@AuthBP.route('/login', methods=['POST'])
def login():
    data=data = request.get_json()

    if not data:
        return jsonify({'error': 'Nombre de usuario y contraseña requeridos'}), 400

    userDto=UserDTO(userID=data["userID"], username=data["username"],password=data["password"])
    auth_service=UserAuth()
    auth=auth_service.login(userDto)
    if not check_password_hash(auth.password, data['password']):
        return jsonify({'error': 'Credenciales inválidas'}), 401

    # Generar el token de autenticación
    token = jwt.encode({'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'amongus')

    return jsonify({'token': token})

@AuthBP.route('/logout', methods=['POST'])
def logout():
    # Aquí podrías realizar alguna acción adicional si lo deseas
    return jsonify({'message': 'Sesión cerrada exitosamente'})


# Decorador para proteger rutas que requieren autenticación
def require_auth(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if token:
            try:
                # Verificar y decodificar el token utilizando la clave secreta
                payload = jwt.decode(token, AuthBP.config['SECRET_KEY'], algorithms=['HS256'])
                return func(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return jsonify({'error': 'Token expirado'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'error': 'Token inválido'}), 401
        else:
            return jsonify({'error': 'Token de autenticación requerido'}), 401

    wrapper.__name__ = func.__name__
    return wrapper