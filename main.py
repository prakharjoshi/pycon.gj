################# Imports ####################

# Python imports
import os

# Framework imports
import jinja2
import webapp2

############## End imports ####################


############# Setup environment ###############

# Jinja environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

########### End environment setup #############


################# Handlers ####################

# The index page handler
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("index.html")
        self.response.write(template.render())


class COChandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("coc.html")
        self.response.write(template.render())


class OrganisersHandlers(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("organisers.html")
        self.response.write(template.render())


class ContactsHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("contacts.html")
        self.response.write(template.render())


class SpeakersHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("speakers.html")
        self.response.write(template.render())


class ContentHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("content.html")
        self.response.write(template.render())


class ScheduleHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("schedule.html")
        self.response.write(template.render())


class PriceHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("price.html")
        self.response.write(template.render())


class VenueHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("venue.html")
        self.response.write(template.render())


class HotelsHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("hotels.html")
        self.response.write(template.render())


class PartnersListHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("partners-list.html")
        self.response.write(template.render())


class PartnerJoinHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("partner-join.html")
        self.response.write(template.render())


class CFPHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("cfp.html")
        self.response.write(template.render())


class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("register.html")
        self.response.write(template.render())

############### End handlers ##################


############### Initialization ################

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/coc', COChandler),
    ('/organizers', OrganisersHandlers),
    ('/contacts', ContactsHandler),
    ('/speakers', SpeakersHandler),
    ('/content', ContentHandler),
    ('/schedule', ScheduleHandler),
    ('/price', PriceHandler),
    ('/venue', VenueHandler),
    ('/hotels', HotelsHandler),
    ('/partners/list', PartnersListHandler),
    ('/partners/join', PartnerJoinHandler),
    ('/cfp', CFPHandler),
    ('/register', RegisterHandler)
], debug=True)

############# End initialization ##############
