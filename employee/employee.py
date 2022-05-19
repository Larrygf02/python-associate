
class Employee():

    def __init__(self, name, email_address, title, phone_number=None):
        self.name = name
        self.email_address = email_address
        self.title = title
        self.phone_number = phone_number

    def email_signature(self, include_phone=None):
        optional_message = ''
        if self.phone_number is not None:
            optional_message = optional_message + " phone: "+ str(self.phone_number) + ","

        if include_phone is not None:
            optional_message = optional_message + " additional_phone: " + str(include_phone)
         
        return f"Employe name: {self.name}, email: {self.email_address}, title: {self.title}," + optional_message