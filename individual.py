# -*- coding: iso-8859-1 -*-
from gedcom_helper import gedcom_helper


class individual():
    def __init__(self,id,name,geburtsname,vorname,geburtsdatum,geburtsort,geschlecht,taufdatum,taufort,religion,sterbedatum,sterbeort,beerdigungsdatum,beerdigungsort,partner1,partner2,partner3,partner4,notizen,vater,mutter,beruf,childof,f1,f2,f3,f4):
        print "processing " +vorname + " " + name 
        self._id=id
        self._name=name
        self._geburtsname=geburtsname
        self._vorname=vorname
        self._geburtsdatum=geburtsdatum
        self._geburtsort=geburtsort
        self._geschlecht=geschlecht
        self._taufdatum=taufdatum
        self._religion=religion
        self._taufort=taufort
        self._sterbedatum=sterbedatum
        self._sterbeort=sterbeort
        self._beerdigungsdatum=beerdigungsdatum
        self._beerdigungsort=beerdigungsort
        self._partner1=partner1
        self._partner2=partner2
        self._partner3=partner3
        self._partner4=partner4
        self._vater=vater
        self._mutter=mutter
        self._notes=notizen
        self._beruf=beruf
        self._childof=childof
        self._f1=f1
        self._f2=f2
        self._f3=f3
        self._f4=f4
        

    def printme(self):
        print "start-------------------------------------"
        print "PersonenID: "+ str(self._id)
        print "\tName: "+self._name
        print "\tGeburtsname: "+self._geburtsname
        print "\tVorname: "+self._vorname
        print "\tGeburtsdatum: "+self._geburtsdatum
        print "\tGeburtsort: "+self._geburtsort
        print "\tGeschlecht: "+self._geschlecht
        print "\tTaufdatum: "+self._taufdatum
        print "\tReligion: "+self._religion
        print "\tTaufort: "+self._taufort
        print "\tSterbedatum: "+self._sterbedatum
        print "\tSterbeort: "+self._sterbeort
        print "\tBeerdigungsdatum: "+self._beerdigungsdatum
        print "\tBeerdigungsort: "+self._beerdigungsort
        print "\tPartner1-ID: "+str(self._partner1)
        print "\tPartner2-ID: "+str(self._partner2)
        print "\tPartner3-ID: "+str(self._partner3)
        print "\tPartner4-ID: "+str(self._partner4)
        print "\tVater-ID: "+str(self._vater)
        print "\tMutter-ID: "+str(self._mutter)
        print "\tNotizen: "+self._notes
        print "\tBeruf:"+self._beruf
        print "\tChildof:"+str(self._childof)
        print "\Fam1:"+str(self._f1)
        print "\Fam2:"+str(self._f2)
        print "\Fam3:"+str(self._f3)
        print "\Fam4:"+str(self._f4)
        
        print "end---------------------------------------"

    def write2gedcom(self,filedes):
        filedes.write("0 @I"+str(self._id)+"@ INDI\n")
        if self._geburtsname!="":
            filedes.write("1 NAME "+ self._vorname +"/"+ self._geburtsname + "/\n")
        else:
            filedes.write("1 NAME "+ self._vorname +"/"+ self._name + "/\n")
        filedes.write("2 GIVN " + self._vorname +"\n")
        if self._geburtsname!="":
            filedes.write("2 SURN "+ self._geburtsname + "\n")
            filedes.write("2 _MARNM "+ self._name + "\n")
        else:
            filedes.write("2 SURN "+ self._name + "\n")
        if self._geschlecht=="männlich":
            filedes.write("1 SEX M\n")
        else:
            if self._geschlecht=="weiblich":
                filedes.write("1 SEX F\n")
            else:
                filedes.write("1 SEX U\n")
        if self._f1!=0:
            filedes.write("1 FAMS @F"+str(self._f1)+"@\n")
        if self._f2!=0:
            filedes.write("1 FAMS @F"+str(self._f2)+"@\n")
        if self._f3!=0:
            filedes.write("1 FAMS @F"+str(self._f3)+"@\n")
        if self._f4!=0:
            filedes.write("1 FAMS @F"+str(self._f4)+"@\n")
        if self._childof!=0:
            filedes.write("1 FAMC @F"+str(self._childof)+"@\n")
        if self._geburtsdatum!="" or self._geburtsort!="":
            filedes.write("1 BIRT\n")
            if self._geburtsdatum!="":
                filedes.write("2 DATE "+ gedcom_helper().convert_date(self._geburtsdatum) + "\n")
            if self._geburtsort!="":
                filedes.write("2 PLAC "+ self._geburtsort+"\n")
        if self._taufdatum!="" or self._taufort!="":
            filedes.write("1 BAPM\n")
            if self._taufdatum!="":
                filedes.write("2 DATE "+ gedcom_helper().convert_date(self._taufdatum) + "\n")
            if self._taufort!="":
                filedes.write("2 PLAC "+ self._taufort+"\n")
        if self._religion !="":
            filedes.write("1 RELI "+ self._religion + "\n")
        if self._beruf!="":
            filedes.write("1 OCCU "+self._beruf+"\n")
        if self._sterbedatum!="" or self._sterbeort!="":
            filedes.write("1 DEAT\n")
            if self._sterbedatum!="":
                filedes.write("2 DATE "+ gedcom_helper().convert_date(self._sterbedatum) + "\n")
            if self._sterbeort!="":
                filedes.write("2 PLAC "+ self._sterbeort+"\n")
        if self._beerdigungsdatum!="" or self._beerdigungsort!="":
            filedes.write("1 BURI\n")
            if self._beerdigungsdatum!="":
                filedes.write("2 DATE "+ gedcom_helper().convert_date(self._beerdigungsdatum  ) + "\n")
            if self._beerdigungsort!="":
                filedes.write("2 PLAC "+ self._beerdigungsort+"\n")
        if self._notes!="":
            srr=""
            for i in self._notes:
                if ord(i)==13 or ord(i)==10:
                    pass
                else:
                    srr+=i
            self._notes=srr
            zeilen=len(self._notes) / 50
            for zeile in range(0,zeilen):
                if zeile==0:
                    filedes.write("1 NOTE "+ self._notes[0:50]  + "\n")
                else:
                    filedes.write("2 CONT "+ self._notes[(zeile*50):(zeile+1)*50]  + "\n")
