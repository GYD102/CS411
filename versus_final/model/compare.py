from propublica_glib import *

Stances = ['Abortion', 'Firearms and explosives', 'Refugees, asylum, displaced persons', 'Immigration status and procedures','Sex, gender, sexual orientation discrimination','Health care coverage and access', 'Labor standards','Tax administration and collection,taxpayers', 'International law and treaties', 'Intelligence activities','surveillance','classified information']

def get_sen_core_from_file(sen_code):
    tf = open(sen_code+".txt","r")
    ustr = tf.read()
    d = locals()
    tf.close()
    print("f = " + ustr)
    exec ("f = " + ustr, globals(), d)
    return d['f']

#s1 = get_sen_core_from_file("")
#s2 = get_sen_core_from_file("")

#user = {}

#score_s1 = 0
#score_s2 = 0
# User results come in one at a time
# The below function iterates the score
def comp(key, user_score, score_list, s1, s2):
    a = 0
    b = 0
    if key in s1.keys():
        a = s1[key]
        a = a / abs(a)
    if key in s2.keys():
        b = s2[key]
        b = b / abs(b)
    if user_score == a:
        score_list[0] += 1
    if user_score == b:
        score_list[1] += 1
    return score_list

#for i in user:
#    comp(i, user[i])
    
        
# To run the above on a full set of stances,
# for i in Stances: comp(i, +/-1)

# This function is for populating our score list
def cycle_senators(dus):
    for i in dus:
        if i[0] not in ['A','B','C']:
            tf = open(i+".txt")
            tf.write(str(score_this_senator(dus[i])))
            tf.close()

