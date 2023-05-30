from Application.Port.In.crudUseCase import CrudUserCase
from Core.user import User
from Adapters.DTO.userDTO import UserDTO
from Application.Port.Out.updatePasswordPort import updatePasswordPort
from Application.Port.Out.loginPort import loginPort
from Application.Port.Out.registerUserPort import resgisterUserPort
from Application.Port.Out.updateUsernamePort import updateUserPort

class UserAuth:
    def __init__(self):
        self.userUseCase = CrudUserCase()

    def registerUser(self, userDTO: UserDTO) -> User:
        resgisterdUser= self.userUseCase.registerUser(userDTO.userID, userDTO.username, userDTO.password)
        if resgisterdUser:
            resgisterUserPort().regiserUser(userDTO.userID,userDTO.username,userDTO.password)
        return resgisterdUser

    def login(self, userDTO: UserDTO) -> User:
        token=self.userUseCase.getUser(userDTO.userID)
        if token:
            loginPort().login(userDTO.userID,userDTO.username)
        return token

    def updateUsername(self, userDTO: UserDTO) -> User:
        modifiedUser= self.userUseCase.updateUsername(userDTO.userID,userDTO.username)
        if modifiedUser:
            updateUserPort().updateUsername(userDTO.userID,userDTO.username)
        return modifiedUser

    def updatePassword(self, userDTO: UserDTO) -> User:
        modifiedPassword= self.userUseCase.updatePassword(userDTO.userID,userDTO.password)
        if modifiedPassword:
            updatePasswordPort().updatePassword(userDTO.userID,userDTO.password)
        return modifiedPassword

    def deleteUser(self, userDTO: UserDTO) -> None:
        return self.userUseCase.deleteUser(userDTO.userID)