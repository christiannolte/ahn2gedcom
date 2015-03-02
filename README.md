# ahn2gedcom

Is a converter that converts genealogy Files from a format, that was used by a "Data Becker Goldene Serie" Software called "Familienchronik" into the gedcom format.

The Software requires Python. It can be started by calling the file filereader.py.

This file requests the filename of the *.AHN file to be imported.
Some general checks will be performed like:

- Check for persons with unknown gender
- Check for persons with a "slash" in the given name


The gedcom export will be written to a file
gedocm_export_(name of ahn file).ged


Have fun
Christian