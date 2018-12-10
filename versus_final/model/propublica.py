import requests
import config
from bs4 import BeautifulSoup
from model.popos.senator import Senator

# todo: store this in db for senators we're using
cached_senators = {'Lamar Alexander': 'A000360', 'Kelly Ayotte': 'A000368', 'Tammy Baldwin': 'B001230',
                   'John Barrasso': 'B001261', 'Max Baucus': 'B000243', 'Mark Begich': 'B001265',
                   'Michael Bennet': 'B001267', 'Richard Blumenthal': 'B001277', 'Roy Blunt': 'B000575',
                   'Cory Booker': 'B001288', 'John Boozman': 'B001236', 'Barbara Boxer': 'B000711',
                   'Sherrod Brown': 'B000944', 'Richard Burr': 'B001135', 'Maria Cantwell': 'C000127',
                   'Benjamin Cardin': 'C000141', 'Thomas Carper': 'C000174', 'Bob Casey': 'C001070',
                   'Saxby Chambliss': 'C000286', 'Jeffrey Chiesa': 'C001100', 'Daniel Coats': 'C000542',
                   'Tom Coburn': 'C000560', 'Thad Cochran': 'C000567', 'Susan Collins': 'C001035',
                   'Christopher Coons': 'C001088', 'Bob Corker': 'C001071', 'John Cornyn': 'C001056',
                   'William Cowan': 'C001099', 'Michael Crapo': 'C000880', 'Ted Cruz': 'C001098',
                   'Joe Donnelly': 'D000607', 'Richard Durbin': 'D000563', 'Michael Enzi': 'E000285',
                   'Dianne Feinstein': 'F000062', 'Deb Fischer': 'F000463', 'Jeff Flake': 'F000444',
                   'Al Franken': 'F000457', 'Kirsten Gillibrand': 'G000555', 'Lindsey Graham': 'G000359',
                   'Charles Grassley': 'G000386', 'Kay Hagan': 'H001049', 'Tom Harkin': 'H000206',
                   'Orrin Hatch': 'H000338', 'Martin Heinrich': 'H001046', 'Heidi Heitkamp': 'H001069',
                   'Dean Heller': 'H001041', 'Mazie Hirono': 'H001042', 'John Hoeven': 'H001061',
                   'James Inhofe': 'I000024', 'Johnny Isakson': 'I000055', 'Mike Johanns': 'J000291',
                   'Tim Johnson': 'J000177', 'Ron Johnson': 'J000293', 'Tim Kaine': 'K000384', 'John Kerry': 'K000148',
                   'Angus King': 'K000383', 'Mark Kirk': 'K000360', 'Amy Klobuchar': 'K000367',
                   'Mary Landrieu': 'L000550',
                   'Frank Lautenberg': 'L000123', 'Patrick Leahy': 'L000174', 'Mike Lee': 'L000577',
                   'Carl Levin': 'L000261', 'Joe Manchin': 'M001183', 'Edward Markey': 'M000133',
                   'John McCain': 'M000303',
                   'Claire McCaskill': 'M001170', 'Mitch McConnell': 'M000355', 'Robert Menendez': 'M000639',
                   'Jeff Merkley': 'M001176', 'Barbara Mikulski': 'M000702', 'Jerry Moran': 'M000934',
                   'Lisa Murkowski': 'M001153', 'Christopher Murphy': 'M001169', 'Patty Murray': 'M001111',
                   'Bill Nelson': 'N000032', 'Rand Paul': 'P000603', 'Rob Portman': 'P000449', 'Mark Pryor': 'P000590',
                   'Jack Reed': 'R000122', 'Harry Reid': 'R000146', 'Jim Risch': 'R000584', 'Pat Roberts': 'R000307',
                   'John Rockefeller': 'R000361', 'Marco Rubio': 'R000595', 'Bernard Sanders': 'S000033',
                   'Brian Schatz': 'S001194', 'Charles Schumer': 'S000148', 'Tim Scott': 'S001184',
                   'Jeff Sessions': 'S001141', 'Jeanne Shaheen': 'S001181', 'Richard Shelby': 'S000320',
                   'Debbie Stabenow': 'S000770', 'Jon Tester': 'T000464', 'John Thune': 'T000250',
                   'Patrick Toomey': 'T000461', 'Mark Udall': 'U000038', 'Tom Udall': 'U000039',
                   'David Vitter': 'V000127',
                   'John Walsh': 'W000818', 'Mark Warner': 'W000805', 'Elizabeth Warren': 'W000817',
                   'Sheldon Whitehouse': 'W000802', 'Roger Wicker': 'W000437', 'Ron Wyden': 'W000779',
                   'Shelley Capito': 'C001047', 'Bill Cassidy': 'C001075', 'Tom Cotton': 'C001095',
                   'Steve Daines': 'D000618', 'Joni Ernst': 'E000295', 'Cory Gardner': 'G000562',
                   'James Lankford': 'L000575', 'David Perdue': 'P000612', 'Gary Peters': 'P000595',
                   'Mike Rounds': 'R000605', 'Ben Sasse': 'S001197', 'Dan Sullivan': 'S001198',
                   'Thom Tillis': 'T000476',
                   'Catherine Cortez Masto': 'C001113', 'Tammy Duckworth': 'D000622', 'Kamala Harris': 'H001075',
                   'Margaret Hassan': 'H001076', 'Cindy Hyde-Smith': 'H001079', 'Doug Jones': 'J000300',
                   'John Kennedy': 'K000393', 'Jon Kyl': 'K000352', 'Tina Smith': 'S001203',
                   'Luther Strange': 'S001202',
                   'Chris Van Hollen': 'V000128', 'Todd Young': 'Y000064', 'Bernie Sanders': 'S000033'}
cached_senators_id_to_name = {v: k for k, v in cached_senators.items()}


class ProPublica:

    @staticmethod
    def get_senator_ids():
        """
        :return: dict[senator_name] = senator_id
        """
        if cached_senators:
            return cached_senators

        # we're only going through chambers 113 - 115
        chambers = [113, 114, 115]
        senators = {}

        for chamber in chambers:
            url = f'https://api.propublica.org/congress/v1/{chamber}/senate/members.json'
            r = requests.get(url, headers=config.PRO_PUBLICA_HEADER)
            assert r.status_code == 200

            res = r.json()['results'][0]['members']
            for senator in res:
                senators[f'{senator["first_name"]} {senator["last_name"]}'] = senator['id']

        senators['Bernie Sanders'] = senators['Bernard Sanders']
        return senators

    @staticmethod
    def get_senator_bio_and_image(id):
        """
        :param id: string
        :return: (bio: string, img_url: string)
        """
        url = f'http://bioguide.congress.gov/scripts/biodisplay.pl?index={id}'
        r = requests.get(url)
        assert r.status_code == 200

        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')

        bio = soup.p.text
        img_url = 'http:' + soup.find_all('img')[1]['src']
        return bio, img_url

    @staticmethod
    def get_image_blob(url):
        """
        :param url: str .jpg image url
        :return: blob: bytes
        """
        r = requests.get(url)
        assert r.status_code == 200

        blob = r.content
        return blob

    @staticmethod
    def get_senator_object(senator_id):
        """
        :param senator_id: str
        :return: senator : Senator
        """
        name = cached_senators_id_to_name[senator_id]
        bio, image_url = ProPublica.get_senator_bio_and_image(senator_id)
        return Senator(senator_id, name, bio, image_url)


def test():
    senators = ProPublica.get_senator_ids()
    print(senators)

    bio, image_url = ProPublica.get_senator_bio_and_image(senators['Bernard Sanders'])
    print(bio, image_url)

    blob = ProPublica.get_image_blob(image_url)
    print(blob)


if __name__ == "__main__":
    test()
