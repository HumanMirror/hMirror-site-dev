from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 

class Contact(webapp.RequestHandler):
    def get(self):  
        self.response.out.write(template.render('index.html', {}))
    def post(self):
        sender = "harsha.mrakesh@gmail.com"
        subject = self.request.get("name")
        body = self.request.get("message")          
        message = mail.EmailMessage(sender=sender, subject=subject)
        message.to = "harsha.mrakesh@gmail.com"
        message.body = body
        message.send()

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)

def main():
    application = webapp.WSGIApplication([('/contact', Contact),  
                                           LogSenderHandler.mapping()],
                                           debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()