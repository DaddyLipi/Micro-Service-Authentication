from flask import Flask

from Adapters.controllers.auth_controller import AuthBP
app = Flask(__name__)
app.register_blueprint(AuthBP)

app.run()