from Adapters.out.MailServiceAdapter import MailServiceAdapter
class loginPort:
    def __init__(self):
        self.mailAdapter=MailServiceAdapter()
    def login(self,userID,username):
        self.mailAdapter.newLogin(userID,username)