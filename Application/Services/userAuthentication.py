from Application.Port.In.crudUseCase import CrudUserCase
from Core.user import User
from Adapters.DTO.userDTO import UserDTO

class UserAuth:
    def __init__(self):
        self.userUseCase = CrudUserCase()

    def registerUser(self, userDTO: UserDTO) -> User:
        resgisterdUser= self.userUseCase.registerUser(userDTO.userID, userDTO.username, userDTO.password)
        return resgisterdUser

    def login(self, userDTO: UserDTO) -> User:
        return self.userUseCase.getUser(userDTO.userID)

    # def updateUser(self, userDTO: UserDTO) -> User:
    #     modifiedUser= self.userUseCase.updateUser(userDTO.userID,userDTO.username, userDTO.email)
    #     if modifiedUser:
    #         updateUsernamePort().updateUsername(userDTO.userID,userDTO.username)
    #     return modifiedUser

    # def deleteUser(self, userDTO: UserDTO) -> None:
    #     self.userUseCase.deleteUser(userDTO.userID)
    #     DeleteUserPort().deleteUser(userDTO.userID)