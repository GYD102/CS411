Stances = ['Abortion', 'Firearms and explosives', 'Refugees, asylum, displaced persons', 'Immigration status and procedures','Sex, gender, sexual orientation discrimination','Health care coverage and access', 'Labor standards','Tax administration and collection,taxpayers', 'International law and treaties', 'Intelligence activities,surveillance,classified information']

tf = open(sen_code+".txt","r")
ustr = tf.read()
tf.close()
exec("d = " + ustr)


