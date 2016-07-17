import cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail

class SendEmail(webapp.RequestHandler):
    def post(self):
		print "Rakesh is here"
        name = self.request.get('name', '')
        email = self.request.get('email', '')
        telephone = self.request.get('telephone', '')
        msg = self.request.get('message', '')

        if name is None:
            self.response.out.write("Error: You did not enter a name.")
        elif email is None:
            self.response.out.write("Error: You did not enter an email.")
        elif telephone is None:
            self.response.out.write("Error: You did not enter a telephone.")
        elif msg is None:
            self.response.out.write("Error: You did not enter a message.")
        else:
            _subject = "Message from: " + name + ", Tel: " + telephone
            msg += "\n\nI can be reached at "
            msg += email

            message = mail.EmailMessage(sender = "harsha.mrakesh@gmail.com", to = "harsha.mrakesh@gmail.com")
            message.subject = _subject
            message.body = msg
            message.send()

            self.redirect('/')

def runApp():
    application = webapp.WSGIApplication([('/contact', SendEmail)], debug=True)
    run_wsgi_app(application)

if __name__ == "__main__":
    runApp()