class User:
    def __init__(self, userID, username, password):
        self.userID = userID
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(user_id={self.userID},username='{self.username}', password='{self.password}')"