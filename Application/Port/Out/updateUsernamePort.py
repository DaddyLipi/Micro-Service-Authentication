from Adapters.out.MailServiceAdapter import MailServiceAdapter
class updateUserPort:
    def __init__(self):
        self.mailAdapter=MailServiceAdapter()
    def updateUsername(self,userID,username):
        self.mailAdapter.changeUsername(userID,username)