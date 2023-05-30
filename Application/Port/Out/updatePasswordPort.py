from Adapters.out.MailServiceAdapter import MailServiceAdapter
class updatePasswordPort:
    def __init__(self):
        self.mailAdapter=MailServiceAdapter()
    def updatePassword(self,userID,password):
        self.mailAdapter.changePassword(userID,password)