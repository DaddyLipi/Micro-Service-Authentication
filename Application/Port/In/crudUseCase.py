from Core.user import User
from Adapters.repository.authRepository import AuthRepository


class CrudUserCase:
    def __init__(self):
        self.authRepository = AuthRepository.getInstance()
        

    def registerUser(self, userID: int, username: str, password: str) -> User:
        user = User(userID, username, password)
        return self.authRepository.create(user)

    def getUser(self, userID: int) -> User:
        user=self.authRepository.get_by_id(userID)
        return user

    def updateUsername(self, userID: int, username: str) -> User:
        user = self.authRepository.get_by_id(userID)
        if not user:
            return None
        user.username = username
        return self.authRepository.update_username(user)
    
    def updatePassword(self, userID: int, password: str) -> User:
        user = self.authRepository.get_by_id(userID)
        if not user:
            return None
        user.password = password
        return self.authRepository.update_password(user)
    
    def deleteUser(self, userID: int) -> None:
        self.authRepository.delete(userID)
