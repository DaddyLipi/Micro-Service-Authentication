from Adapters.out.MailServiceAdapter import MailServiceAdapter
class resgisterUserPort:
    def __init__(self):
        self.mailAdapter=MailServiceAdapter()
    def regiserUser(self,userID,username,password):
        self.mailAdapter.register(userID,username,password)
