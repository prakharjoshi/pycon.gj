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


class codeofconduct(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("coc.html")
		self.response.write(template.render())

class organisers(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("organisers.html")
		self.response.write(template.render())

class contacts(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("contacts.html")
		self.response.write(template.render())

class speakers(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("speakers.html")
		self.response.write(template.render())

class content(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("content.html")
		self.response.write(template.render())

class schedule(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("schedule.html")
		self.response.write(template.render())

class price(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("price.html")
		self.response.write(template.render())

class venue(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("venue.html")
		self.response.write(template.render())

class hotels(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("hotels.html")
		self.response.write(template.render())

class partnersList(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("partners.html")
		self.response.write(template.render())

class partnerJoin(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("partnerJoin.html")
		self.response.write(template.render())

class cfp(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("cfp.html")
		self.response.write(template.render())

class register(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("register.html")
		self.response.write(template.render())

class conference(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("conference.html")
		self.response.write(template.render())

class program(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("programe.html")
		self.response.write(template.render())

class participation(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("participation.html")
		self.response.write(template.render())

class partners(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("partners.html")
		self.response.write(template.render())

class archive(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template("archive.html")
		self.response.write(template.render())
        
############### End handlers ##################


############### Initialization ################

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/coc', codeofconduct),
    ('/organizers',organisers),
    ('/contacts',contacts),
    ('/speakers',speakers),
    ('/content',content),
    ('/schedule',schedule),
    ('/price',price),
    ('/venue',venue),
    ('/hotels',hotels),
    ('/partners/list',partnersList),
    ('/partners/join/',partnerJoin),
    ('/cfp',cfp),
    ('/register',register),
    ('/conference',conference),
    ('/program',program),
    ('/participation',participation),
    ('/partners',partners),
    ('/archive',archive)


], debug=True)

############# End initialization ##############


