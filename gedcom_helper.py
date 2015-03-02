class gedcom_helper():
    def __init__(self):
        pass
    
    def convert_date(self,datestring):
        month = datestring[3:5]
        year = datestring[6:]
        nm="UNK"
        if month=="01":
            nm="JAN"
        if month=="02":
            nm="FEB"
        if month=="03":
            nm="MAR"
        if month=="04":
            nm="APR"
        if month=="05":
            nm="MAY"
        if month=="06":
            nm="JUN"
        if month=="07":
            nm="JUL"
        if month=="08":
            nm="AUG"
        if month=="09":
            nm="SEP"
        if month=="10":
            nm="OCT"
        if month=="11":
            nm="NOV"
        if month=="12":
            nm="DEC"
        newdate = datestring[:2] + " " + nm + " " + year
        return newdate
        


    def write_header(self,filedes):
        filedes.write("0 HEAD\n")
        filedes.write("1 SOUR PAF\n")
        filedes.write("2 NAME Personal Ancestral File\n")
        filedes.write("2 VERS 5.2.18.0\n")
        filedes.write("2 CORP The Church of Jesus Christ of Latter-day Saints\n")
        filedes.write("3 ADDR 50 East North Temple Street\n")
        filedes.write("4 CONT Salt Lake City, UT 84150\n")
        filedes.write("4 CONT USA\n")
        filedes.write("1 DEST Other\n")
        filedes.write("1 DATE 16 Feb 2011\n")
        filedes.write("2 TIME 15:06:06\n")
        filedes.write("1 FILE mytest.ged\n")
        filedes.write("1 GEDC\n")
        filedes.write("2 VERS 5.5\n")
        filedes.write("2 FORM LINEAGE-LINKED\n")
        filedes.write("1 CHAR ANSI\n")
        filedes.write("1 LANG German\n")
        filedes.write("1 SUBM @SUB1@\n")
        filedes.write("0 @SUB1@ SUBM\n")
        filedes.write("1 NAME Christian Nolte\n")
        filedes.write("1 ADDR irgendwo\n")
        filedes.write("2 CONT unbekannt\n")
        filedes.write("2 CONT  5878 irgend\n")
        #filedes.write("0 HEAD\n")
        #filedes.write("1 SOUR Reunion\n")
        #filedes.write("2 VERS V8.0\n")
        #filedes.write("2 CORP Leister Productions\n")
        #filedes.write("1 DEST Reunion\n")
        #filedes.write("1 DATE 11 FEB 2006\n")
        #filedes.write("1 FILE test\n")
        #filedes.write("1 GEDC\n")
        #filedes.write("2 VERS 5.5\n")
        #filedes.write("1 CHAR MACINTOSH\n")

    def write_footer(self,filedes):
        filedes.write("0 TRLR\n")
