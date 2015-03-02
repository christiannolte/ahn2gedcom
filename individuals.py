from individual import individual

class individuals():
    def __init__(self):
        self._individuals=[]

    def add_individual(self,id,name,geburtsname,vorname,geburtsdatum,geburtsort,geschlecht,taufdatum,taufort,religion,sterbedatum,sterbeort,beerdigungsdatum,beerdigungsort,partner1,partner2,partner3,partner4,notizen,vater,mutter,beruf,childof,f1,f2,f3,f4):
        ni=individual(id,name,geburtsname,vorname,geburtsdatum,geburtsort,geschlecht,taufdatum,taufort,religion,sterbedatum,sterbeort,beerdigungsdatum,beerdigungsort,partner1,partner2,partner3,partner4,notizen,vater,mutter,beruf,childof,f1,f2,f3,f4)
        self._individuals.append(ni)
        
    def get_gender(self,id):
        for ind in self._individuals:
            if ind._id==id:
                return ind._geschlecht

    def get_name(self,id):
        for ind in self._individuals:
            if ind._id==id:
                return ind._vorname + " " + ind._name

    def print_them(self):
        for ind in self._individuals:
            ind.printme()

    def write_them_to_gedcom(self,filedes):
        for ind in self._individuals:
            ind.write2gedcom(filedes)
