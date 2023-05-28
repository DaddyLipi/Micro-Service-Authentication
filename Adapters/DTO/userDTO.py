class UserDTO:
    def __init__(self, userID=None, username=None,password=None):
        self.userID = userID
        self.username = username
        self.password = password

    @staticmethod
    def fromEntity(user):
        return UserDTO(
            userID=user.userID,
            username=user.username,
            password=user.password
        )