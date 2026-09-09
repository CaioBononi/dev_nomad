from flask import Flask
from app.config.firebase_config import initialize_firebase
from app.controllers.auth_controller import auth_blueprint
from app.controllers.user_controller import user_blueprint

# Initialize Firebase Admin SDK
initialize_firebase()

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
app.register_blueprint(user_blueprint, url_prefix='/api/users')

@app.route('/')
def index():
    return {"message": "Welcome to the Dev Nomad API!"}

if __name__ == '__main__':
    app.run(debug=True)