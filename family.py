# -*- coding: iso-8859-1 -*-
from gedcom_helper import gedcom_helper


class family():
    def __init__(self,hus,wif,id):
        self._id=id
        self._hus=hus
        self._wif=wif
        self._childs=[]
        self._date=""
        self._place=""

    def add_child(self,child):
        self._childs.append(child)

    def set_marriage_information(self,date,place):
        self._date=date
        self._place=place

    def get_hus(self):
        return self._hus

    def get_wif(self):
        return self._wif

    def get_id(self):
        return self._id

    def compare(self,hus,wif):
        if self._hus == hus  and self._wif == wif:
            return 1
        return 0

    def print_fam(self):
        print "Family-ID: " + str(self._id)
        print "\tHusband: " + str(self._hus)
        print "\tWife: " + str(self._wif)
        print "\tDate: " +self._date + " in " + self._place
        
        for chd in self._childs:
            print "\t\tChild: "+str(chd)
        print ""

    def write2gedcom(self,filedes):
        filedes.write("0 @F"+str(self._id)+"@ FAM\n")
        if self._hus!=0:
            filedes.write("1 HUSB @I" + str(self._hus) +"@\n")
        if self._wif!=0:
            filedes.write("1 WIFE @I" + str(self._wif) +"@\n")
        for chl in self._childs:
            filedes.write("1 CHIL @I"+str(chl)+"@\n")
        if self._date!="" or self._place!="":
            filedes.write("1 MARR Y\n")
            if self._date!="":
                filedes.write("2 DATE "   +  gedcom_helper().convert_date(self._date) +"\n")
            if self._place!="":
                filedes.write("2 PLAC "   +  self._place +"\n")

            
