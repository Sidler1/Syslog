import re


class ParserFirewall:

    def __init__(self, message):
        self.message = message

    def pars(self):
        head = re.compile(r"[a-z]{1,}=")
        inhalt = re.split("[a-z]{1,}=", self.message)
        del inhalt[0]
        titel = head.findall(self.message)
        header = 0
        data = {}
        while header < len(titel):
            data[titel[header][:-1]] = inhalt[header]
            header += 1
        return data

class ParserSwitch:

    def __init__(self, message):
        self.message = message
        
    def pars(self):
        head = re.compile(r"[a-z]{1,}:")
        pri = re.compile(r"<[0-9]{1,}>")
        inhalt = re.split("[a-z]{1,}:", self.message)
        prio = pri.findall(self.message)
        titel = head.findall(self.message)
        del inhalt[0]
        header = 0
        data = {}
        data['msg'] = inhalt[header]
        data['pri'] = prio[0][1:-1]
        return data

class ParserLinux:

    def __init__(self, message):
        self.message = message
        
    def pars(self):
        head = re.compile(r"([a-z]{1,}\[[0-9]{1,}\]\:)|([e-r]{6}\:)")
        pri = re.compile(r"\<[0-9]{1,}\>")
        inhalt = re.split("([a-z]{1,}\[[0-9]{1,}\]\:)|([e-r]{6}\:)", self.message)
        prio = pri.findall(self.message)
        titel = head.findall(self.message)
        del inhalt[0]
        data = {}
        if len(inhalt) < 1:
            return None
        elif inhalt[0] == None:
            data['trigger'] = inhalt[1]
            data['msg'] = inhalt[2]
        else:
            data['trigger'] = inhalt[0]
            data['msg'] = inhalt[2]
        data['pri'] = prio[0][1:-1]
        data['msg'] = data['msg'][:-1]
        return data
