# -*- coding: iso-8859-1 -*-
from gedcom_helper import gedcom_helper
import struct
from families import families
from individuals import individuals

filename=raw_input ("Name der AHN-Datei, die verarbeitet werden soll? ")
version="1.0.0"

myfam=families()
myind=individuals()
print "Trying to convert file \"weber.ahn\" if you want to convert another file,"
print "please change the referenced filename in filereader.py."
print "You can find the variable filename at the beginning of the file"
print ""
print "Version: " + version
print "lets go..."
print ""
f=open(filename,"rb")
f.seek(0,2)
size=f.tell()
entries=size/1100
i=0

while i<entries:
    print "+++++++++++++++++++++++++++++++++++++++"
    print "Datensatz "+ str(i+1)+"/"+str(entries) 
    f.seek(i*1100)
    id=struct.unpack('i', f.read(4))[0]
    name=f.read(20).rstrip().rstrip()
    geburtsname=f.read(20).rstrip()
    vorname=f.read(20).rstrip()
    w_vornamen=f.read(30).rstrip()
    birth_date=f.read(10).rstrip()
    birth_place=f.read(30).rstrip()
    bapt_date=f.read(10).rstrip()
    bapt_place=f.read(30).rstrip()
    gender=f.read(8).rstrip()
    religion=f.read(12).rstrip()
    occupation=f.read(39).rstrip()
    death_date=f.read(10).rstrip()
    death_place=f.read(30).rstrip()
    age=f.read(15).rstrip()
    funeral_date=f.read(10).rstrip()
    funeral_place=f.read(30).rstrip()
    notes=f.read(300).rstrip()
    daddy=struct.unpack('i', f.read(4))[0]
    mommy=struct.unpack('i', f.read(4))[0]
    partner1=struct.unpack('i', f.read(4))[0]
    marri1date=f.read(10).rstrip()
    marri1place=f.read(30).rstrip()
    f.read(72) #dummyread f. 18 Kinder
    partner2=struct.unpack('i', f.read(4))[0]
    marri2date=f.read(10).rstrip()
    marri2place=f.read(30).rstrip()
    f.read(72) #dummyread f. 18 Kinder
    partner3=struct.unpack('i', f.read(4))[0]
    marri3date=f.read(10).rstrip()
    marri3place=f.read(30).rstrip()
    f.read(72) #dummyread f. 18 Kinder
    partner4=struct.unpack('i', f.read(4))[0]
    marri4date=f.read(10).rstrip()
    marri4place=f.read(30).rstrip()
    f.read(72) #dummyread f. 18 Kinder
    fid=myfam.get_id_or_create_family(daddy,mommy)
    myfam.add_child_to_family(fid,id)
    own_fid1=own_fid2=own_fid3=own_fid4=0
    if partner1!=0:
        if gender=="männlich":
            own_fid1=myfam.get_id_or_create_family(id,partner1)
        else:
            own_fid1=myfam.get_id_or_create_family(partner1,id)
        myfam.set_date_and_place(own_fid1,marri1date,marri1place)

    if partner2!=0:
        if gender=="männlich":
            own_fid2=myfam.get_id_or_create_family(id,partner2)
        else:
            own_fid2=myfam.get_id_or_create_family(partner2,id)
        myfam.set_date_and_place(own_fid2,marri2date,marri2place)

    if partner3!=0:
        if gender=="männlich":
            own_fid3=myfam.get_id_or_create_family(id,partner3)
        else:
            own_fid3=myfam.get_id_or_create_family(partner3,id)
        myfam.set_date_and_place(own_fid3,marri3date,marri3place)

    if partner4!=0:
        if gender=="männlich":
            own_fid4=myfam.get_id_or_create_family(id,partner4)
        else:
            own_fid4=myfam.get_id_or_create_family(partner4,id)
        myfam.set_date_and_place(own_fid4,marri4date,marri4place)

    #print str(id) + " " + name + " " + vorname + " " + w_vornamen
    #print "\tGeburtsname: "+ geburtsname
    #print "\tGeburt: "+ birth_date +" " + birth_place
    #print "\tGeschlecht: " + gender
    #print "\tBeruf: "+ occupation
    #print "\tVater: " + str(daddy) + " Mutter: "+str(mommy)
    #print "\tTod: "+death_date + " in " + death_place
    #print "\tAlter: "+age
    #print "\tBeerdigung: "+funeral_date + " in " + funeral_place
    #print "\tPartner1: " + str(partner1) +" "+ marri1date + " " + marri1place
    #print "\tPartner2: " + str(partner2) +" "+ marri2date + " " + marri2place
    #print "\tPartner3: " + str(partner3) +" "+ marri3date + " " + marri3place
    #print "\tPartner4: " + str(partner4) +" "+ marri4date + " " + marri4place
    #print ""
    myind.add_individual(id,
                         name,
                         geburtsname,
                         vorname+" "+w_vornamen,
                         birth_date,birth_place,gender,
                         bapt_date,bapt_place,religion,
                         death_date,death_place,
                         funeral_date,funeral_place,
                         partner1,
                         partner2,
                         partner3,
                         partner4,
                         notes,
                         daddy,mommy,
                         occupation,
                         myfam.get_id_or_create_family(daddy,mommy),
                         own_fid1,own_fid2,own_fid3,own_fid4)
    i=i+1
#myfam.print_them()
#myind.print_them()
#Personen mit unbekannten Geschlecht finden
for i in myind._individuals:
    if i._geschlecht!="männlich" and i._geschlecht!="weiblich":
        print "-------------------------------------------------------------------------------"
        print i._vorname+"/"+i._name+ " wurde mit unbekannten Geschlecht gefunden"
        newgender=raw_input ("Geschlecht m(aennlich)/w(eiblich)/u(nbekannt) m/w/u? ")
        if newgender=="m":
            i._geschlecht="männlich"
        elif newgender=="w":
            i._geschlecht="weiblich"
        else:
            i._geschlecht="unknown"
#Personen mit Schraegstrich im Namen finden
for i in myind._individuals:
    if i._vorname.find("/")!=-1:
        print "-------------------------------------------------------------------------------"
        print "Schraegstrich in Vorname gefunden, Ein Vorname darf keinen Schraegstrich enthalten"
        print i._vorname
        i._vorname=raw_input ("Geben Sie dan Namen ohne Schraegstrich ein! ")

myfile=open("gedcom_export_"+filename+".ged","w")
gedcom_helper().write_header(myfile)
print "-------------------------------------------------------------"
print "Hier muessen Familien auf weibliche Ehemaenner und maennliche Ehefrauen ueberprueft werden"
print "-------------------------------------------------------------"
myind.write_them_to_gedcom(myfile)
myfam.write_them_to_gedcom(myfile)
gedcom_helper().write_footer(myfile)
print "---------------------------------------"
print "Pruefe Geschlechter auf Konsistenz"
print "Zuerst die Ehemaenner"
for hus in myfam.get_all_hus():
    geschlecht = myind.get_gender(hus)
    if geschlecht != "männlich":
        if hus!=0:
            print myind.get_name(hus) + " ist evtl. als " + geschlecht + " eingetragen"
    
print "---------------------------------------"
print "Ehemaenner fertig, jetzt die Ehefrauen"
print "---------------------------------------"
for wif in myfam.get_all_wif():
    geschlecht = myind.get_gender(wif)
    if geschlecht != "weiblich":
        if wif!=0:
            print myind.get_name(wif) + " ist evtl. als " + geschlecht + " eingetragen"
print "Ehefrauen fertig"
print "---------------------------------------"
myfile.close()
