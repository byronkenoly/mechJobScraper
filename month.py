from datetime import datetime

# Switch Case implementation in Python using Class
class jwkMonth:
    def day(self, month):
 
        default = "Incorrect day"
 
        return getattr(self, 'case_' + str(month), lambda: default)()
 
    def case_1(self):
        return "Jan"
 
    def case_2(self):
        return "Feb"
 
    def case_3(self):
        return "Mar"

    def case_4(self):
        return "Apr"

    def case_5(self):
        return "May"
    
    def case_6(self):
        return "Jun"
    
    def case_7(self):
        return "Jul"

    def case_8(self):
        return "Aug"

    def case_9(self):
        return "Sep"

    def case_10(self):
        return "Oct"

    def case_11(self):
        return "Nov"

    def case_12(self):
        return "Dec"

class mjmMonth:
    def day(self, month):
 
        default = "Incorrect day"
 
        return getattr(self, 'case_' + str(month), lambda: default)()
 
    def case_1(self):
        return "January"
 
    def case_2(self):
        return "February"
 
    def case_3(self):
        return "March"

    def case_4(self):
        return "April"

    def case_5(self):
        return "May"
    
    def case_6(self):
        return "June"
    
    def case_7(self):
        return "July"

    def case_8(self):
        return "August"

    def case_9(self):
        return "September"

    def case_10(self):
        return "October"

    def case_11(self):
        return "November"

    def case_12(self):
        return "December"

today = datetime.now()
currentMonth = today.month