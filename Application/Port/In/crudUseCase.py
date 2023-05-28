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

    # def updateUser(self, userID: int, username: str, email: str) -> User:
    #     user = self.authRepository.get_by_id(userID)
    #     if not user:
    #         return None
    #     user.username = username
    #     user.email = email
    #     return self.authRepository.update(user)
    # def deleteUser(self, userID: int) -> None:
    #     self.authRepository.delete(userID)
