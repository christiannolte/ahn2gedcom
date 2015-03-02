from family import family

class families():
    def __init__(self):
        self._families=[]
        self._next_id=1

    def get_id(self,hus,wif):
        for fam in self._families:
            if fam.compare(hus,wif)==1:
                return fam.get_id()
        return(0)

    def get_all_hus(self):
        liste=[]
        for fam in self._families:
            liste.append(fam.get_hus())
        return liste

    def get_all_wif(self):
        liste=[]
        for fam in self._families:
            liste.append(fam.get_wif())
        return liste


    def create_family(self,hus,wife):
        if hus == 0 and wife == 0:
            return 0
        myfam=family(hus,wife,self._next_id)
        self._families.append(myfam)
        self._next_id=self._next_id+1
        return(self._next_id-1)                 #since incremented

    def add_child_to_family(self,family_id,child_id):
        if family_id==0:
            return 0
        for fam in self._families:
            if fam.get_id() == family_id:
                fam.add_child(child_id)

    def get_id_or_create_family(self,hus,wif):
        if self.get_id(hus,wif)==0:
            self.create_family(hus,wif)
        return self.get_id(hus,wif)

    def set_date_and_place(self,id,date,place):
        for fam in self._families:
            if fam.get_id() == id:
                fam.set_marriage_information(date,place)
            
        

    def print_them(self):
        for fam in self._families:
            fam.print_fam()
        
    def write_them_to_gedcom(self,filedes):
        for fam in self._families:
            fam.write2gedcom(filedes)

            
        