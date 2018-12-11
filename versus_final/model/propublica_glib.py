key = "xdyamWeUrsH9XtMdeFBHkJuXJbcZO52npg9mpgu"
import requests
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

url = "https://api.propublica.org/congress/v1/"
r = Request(
    "https://www.congress.gov/member/elizabeth-warren/W000817/?pageSize=250",
    headers = {'User-Agent': 'Mozilla/5.0'}
)
wp = urlopen(r).read()
wps = str(wp)
soup = BeautifulSoup(re.sub(r'(\s+|\n)', ' ', wps),'html.parser')



headers = {
    'X-API-Key': key
}

def api_call(string):
    return requests.get(
        url + string,
        headers = headers
    )

# Accepts
#   chamber:  one of two strings: "senate" or "house"
#   congress: congress number (in number or string form)
# Returns
#   return requests.models.Response
def members(congress,chamber):
    return api_call(
        "{congress}/{chamber}/members.json".format(
            congress = str(congress),
            chamber = chamber
        )
    )

def congress_request(url):
    r = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    wp = urlopen(r).read()
    wps = str(wp)
    return BeautifulSoup(re.sub(r'(\s+|\n)', ' ', wps),'html.parser')

page_init = "?pageSize=250&amp;page="
congurl = "https://www.congress.gov"

def get_all_sponsored(senator_string):
    page_num = 1
    numbers = []
    href = "/member/" + senator_string + page_init + str(page_num)
    while True:
        if page_num > 9:
            break
        print(congurl + href)
        soup = congress_request(congurl + href)
        #print(soup.find_all('a',class_="last off"))
        
        rows = soup.find_all(class_="result-heading")
        #print((re.search("[0-9]{3}th",
        #                 rows[0].contents[0]['href']).group(0)[:-2],
        #       rows[0].contents[0].contents[0]))
        item_nos = [(re.search("[0-9]{3}th",
                               i.contents[0]['href']).group(0)[:-2],
                     i.contents[0].contents[0])
                    for i in rows]
        numbers += item_nos
        page_num += 1
        href = soup.find_all(class_="next")
        if soup.find_all(class_="last off") != []:
            break
        href = href[0]['href']
        #print(href)
        #print(soup.find_all('a',class_="last off") != [])
    numbers = list(set(numbers))
    #print(numbers)
    return numbers

senators_115 = members(115, "senate").json()['results'][0]['members']
senators_url = [x['first_name'] + '-' +
                x['last_name'] + '/' +
                x['id'] + '/'
                for x in senators_115]
sud = {}
for i in senators_url:
    sud.update({i[-8:-1]:i})

# Accepts
#   member_id: a string, \b[A-Z][0-9]{6}\b
# Returns
#   return requests.models.Response
def cosponsored_bills(member_id):
    return api_call(
        "members/{member_id}/bills/cosponsored.json".format(
            member_id = member_id
        )
    )


# Accepts
#   requests.models.Response returned by the "cosponsored_bills" function
# Returns
#   list of tuples: first value is the congress, second number is the bill slug
def cosponsored_bills_usable(response_obj):
    return [
        (x['congress'], x['bill_id'][:-4])
        for x in
        response_obj.json()['results'][0]['bills']
    ]


# >>> [(x['congress'],x['bill_id']) for x in cb.json()['results'][0]['bills']]

# Accepts
#   congress: number 105 through 115
#   bill_id:  "a bill slug, for example 'hr4881' - these can be found in bill
#               resonses"
# Returns
#   return requests.models.Response
def bill_subjects(congress, bill_id):
    return api_call(
        "{congress}/bills/{bill_id}/subjects.json".format(
            congress = str(congress),
            bill_id = bill_id
        )
    )

#test_sponsored = test_sponsored
#t = test_sponsored[12]
#test_subject = bill_subjects(t[0],t[1].replace(".","").lower())
# test_subjects = [bill_subjects(i[0],i[1].replace(".","").lower()) for i in test_sponsored] 
#t2 = test_subject.json()['results'][0]
#party = t2['sponsor_party']
#subjects = list(t2['subjects'][0].values())

def get_topics_and_party(congress, slug):
    a = bill_subjects(congress,slug.replace(".","").lower())
    a = a.json()['results'][0]
    topics = [i['name'] for i in a['subjects']]
    return (a['sponsor_party'], topics)


# Takes "senator string"
# fname-lname/A######/
# from object "senators_url"
def score_this_senator(senator_string):
    sponsored = get_all_sponsored(senator_string)
    ke = 0
    done = 0
    final_dictionary = {}
    print(len(sponsored))
    for i in sponsored:
        if done > 2000:
            break
        try:
            res = get_topics_and_party(i[0],i[1])
            k = 0
            if res[0] == "D":
                k = 1
            elif res[0] == "R":
                k = -1
            for j in res[1]:
                #print(j)
                if j in final_dictionary.keys():
                    final_dictionary[j] = final_dictionary[j] + k
                else:
                    final_dictionary.update({j:k})
        except (KeyError, IndexError) as e:
            ke+=1
            print("ke now equals " + str(ke))
        done += 1
        if done % 25 == 0:
            print(done)
    print(final_dictionary)
    return final_dictionary
