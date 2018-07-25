import webapp2
import valid_day
import valid_month
import valid_year

form ="""
<form method ="post">
What is your birthday?
<br>
<label> day <input type  = "text" name = "day" value = "%(day)s"></label>
<label> month <input type  = "text" name = "month" %(month)s></label>
<label> year <input type  = "text" name = "year" %(year)s></label>
<div style ="color:red">%(error)s</div>
<br>
<br>
<input type = "submit"

</form>
"""


class MainPage(webapp2.RequestHandler):
	def write_form(error="",day="", month="", year=""):
		self.response.out.write(form %{"error":error
			                           "day":escape_html(day)
			                           "month":escape_html(month)
			                           "year":escape_html(year)})
    def get(self):
        self.write_form()
    def post(self):
    	# user_day = valid_day(self.request.get('day'))
    	# user_month = valid_month(self.request.get('month'))
    	# user_year = valid_year(self.request.get('year'))

    	user_day = (self.request.get('day'))
    	user_month =(self.request.get('month'))
    	user_year = (self.request.get('year'))

    	day = valid_day(user_day)
    	month = valid_month(user_month)
    	year = valid_year(user_year)


    	if not(day and month and year):
    		self.write_form("That doesnt look valid to me", user_day, user_month, user_year)
    	else:
    	self.redirect("/thanks")
class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanx, that is a totally valid day")

app = webapp2.WSGIApplication([
    ('/', MainPage),('\thanks', ThanksHandler)],
     debug=True)

