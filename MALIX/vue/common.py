import re


class Common:

    def ask(self, key_name: str = "", regex: str = None, default: str = None):
        message = "Enter %s" % key_name
        if default is not None:
            message += "(%s)" % default
        message += ": "
        string = input(message).rstrip()
        if default is not None and string == "":
            return default
        if regex is not None:
            pattern = re.compile("^[\S-]{2,50}$")
            while not pattern.match(string):
                print("/!\\ Error input malformed")
                string = input(message)
        return string

    def ask_name(self, key_name="name", default=None):
        return self.ask(key_name=key_name, regex="^[\S-']{2,50}$", default=default).lower()

    def ask_email(self, default=None):
        return self.ask(key_name="email", regex=None, default=default)

    def ask_type(self, default=None):
        return self.ask(key_name="type (seller or customer)", regex="^(customer|seller)$", default=default)

    def ask_date(self, default=None):
        return self.ask(key_name="date", regex=None, default=default)

    def ask_places(self, default=None):
        return self.ask(key_name="places", regex=None, default=default)

    def ask_prix(self, default=None):
        return self.ask(key_name="prix", regex=None, default=default)

    def ask_nb(self, default=None):
        return self.ask(key_name="nb", regex=None, default=default)
        
    def ask_lieu(self, default=None):
        return self.ask(key_name="lieu", regex=None, default=default)