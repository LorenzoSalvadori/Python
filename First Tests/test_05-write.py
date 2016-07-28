#/usr/bin/env python

bikes = {'Bimota_SB8_2014':'Ducati_1098R_2014' , "Bimota_DB8_2004" : 'Ducati_1098R_2014'}
bikes['Bimota_DB8_Oronero'] = 'Ducati_1098R_2014'

f = open("DB_blabla.xml", "w")
f.write("<vehicleList>\n")
for key in bikes:
    f.write("\t<audiokit vehicleKey = \"")
    f.write(key)
    f.write("\"\t sourcescriptval=\"c:/users/srcnoconv/data/soundconfig/vehicles/Ducati/")
    f.write(bikes[key])
    f.write(".xml\" />\n")

f.write("</vehicleList>")
f.close()