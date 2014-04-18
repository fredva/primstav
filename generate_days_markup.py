import sys
infile = sys.argv[1]

infile = open(infile, "r")

for line in infile:
    date, holiday = (word.strip() for word in line.split(";"))
    if holiday is not "":
        cssclass = " hover"
        extra = " &mdash; " + holiday
    else:
        cssclass, extra = "", ""
    print "<div class=\"day" + cssclass + "\">"
    print "  <h2>" + date + extra + "</h2>"
    print "</div>"

infile.close()
