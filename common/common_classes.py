class Address:
    def __init__(self, address, city, state, postal_code, phone_mobile):
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone_mobile = phone_mobile

    def __repr__(self):
        return '(Address=%s\nCity=%s\nState=%s\nPostcode=%s\nPhone=%s\n)' % \
               (self.address, self.city, self.state, self.postal_code, self.phone_mobile)


class PersonalInformation:
    def __init__(self, email, first_name, last_name, password, title=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        if title is not None:
            self.title = title

    def __repr__(self):
        return '(Email=%s\nTitle=%s\nFirst Name=%s\nLast Name=%s\nPassword=%s\n)' % \
               (self.email, self.title, self.first_name, self.last_name, self.password)

