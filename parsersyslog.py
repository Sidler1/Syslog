import re


class ParserFirewall:

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        self.pars

    def __call__(self):
        self.pars

    def pars(self):
        t = re.compile(r"[a-z]{1,}=")
        e = re.split("[a-z]{1,}=", self.message)
        del e[0]
        titel = t.findall(self.message)
        return titel, e
