class SMSSender():
    def send_sms(self, message):
        print('Отпр сообщ через смс:', message)

class PushSender():
    def send_push(self, message):
        print('Отпр соо через пуш-увед', message)
        
class MailSender():
    def send_mail(self, message):
        print('Отпр соо через почту', message)
        
class SuperSender(SMSSender, PushSender, MailSender):
    
    def __init__(self, message):
        self.message = message
        
    def send_all(self):
        self.send_sms(self.message)
        self.send_push(self.message)
        self.send_mail(self.message)
        
Super_Sender = SuperSender('mess?')
print(Super_Sender.send_all())