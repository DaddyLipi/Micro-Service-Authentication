import requests

class MailServiceAdapter:
    def __init__(self):
        self.baseUrl = "https://ae3b-190-181-40-230.ngrok-free.app/"

    def changePassword(self, userID, newPassword):
        endpoint = '/send_mail/password_change'
        url = self.baseUrl + endpoint

        payload = {
            'userID':userID
        }

        try:
            response = requests.put(url, json=payload)
            if response.status_code == 200:
                print("Password changed successfully.")
            else:
                print("Failed to change password. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))

    def changeUsername(self, userID, username):
        endpoint = '/send_mail/change_username'
        url = self.baseUrl + endpoint

        payload = {
            'userID':userID,
            'username':username
        }

        try:
            response = requests.put(url, json=payload)
            if response.status_code == 200:
                print("Username changed successfully.")
            else:
                print("Failed to change username. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
    def newLogin(self, userID, username):
        endpoint = '/send_mail/new_Login'
        url = self.baseUrl + endpoint

        payload = {
            'userID': userID,
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Login successfully.")
            else:
                print("Failed Login. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))

            
    def register(self, userID,username, password):
        endpoint = '/send_mail/Register'
        url = self.baseUrl + endpoint

        payload = {
            'userID': userID,
            'username': username,
            'password':password
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Registry successfully.")
            else:
                print("Failed to register. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
            