Stances = ['Abortion', 'Firearms and explosives', 'Refugees, asylum, displaced persons', 'Immigration status and procedures','Sex, gender, sexual orientation discrimination','Health care coverage and access', 'Labor standards','Tax administration and collection,taxpayers', 'International law and treaties', 'Intelligence activities,surveillance,classified information']

def get_sen_core_from_file(sen_code):
    tf = open(sen_code+".txt","r")
    ustr = tf.read()
    tf.close()
    exec("d = " + ustr)
    return d


s1 = {} # Either get from the above function
s2 = {} # call score_this_senator(sud[code])
score_s1 = 0
score_s2 = 0
# User results come in one at a time
# The below function iterates the score
def comp(key, score):
    a = 0
    b = 0
    if key in s1.keys():
        a = s1[key]
        a = a / abs(a)
    if key in s2.keys():
        b = s2[key]
        b = b / abs(b)
    if score = a:
        score_s1 += 1
    if score = b:
        score_s2 += 1

# To run the above on a full set of stances,
# for i in Stances: comp(i, +/-1)

# This function is for populating our score list
def cycle_senators(dus):
    for i in dus:
        if i[0] not in ['A','B','C']:
            tf = open(i+".txt")
            tf.write(str(score_this_senator(dus[i])))
            tf.close()

