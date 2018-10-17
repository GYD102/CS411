const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const BioguideScraper = require('./bioguideScraper');

class GovTrack {

    static getRequest(url) {
        const request = new XMLHttpRequest();
        request.open("GET", url, false);   // XMLHttpRequest.open(method, url, async)
        request.setRequestHeader(GovTrack.apiHeaderKey, GovTrack.apiKey);
        request.send();
        return JSON.parse(request.responseText);
    }

    static getPoliticianId(firstName, lastName, chamber, congressNum) {
        if (!(new Set(['senate', 'house'])).has(chamber)) throw "Invalid chamber! Must be one of {'senate', 'house'}";

        const url = `https://api.propublica.org/congress/${GovTrack.apiVersion}/${congressNum}/${chamber}/members.json`;
        const membersArray = GovTrack.getRequest(url)['results'][0]['members'];

        for (let i = 0; i < membersArray.length; i++) {
            const member = membersArray[i];
            if (member['first_name'] === firstName && member['last_name'] === lastName) {
                return member['id'];
            }
        }

        throw `${firstName} ${lastName} not found in ${chamber} for congress ${congressNum}`;
    }

    static getPoliticianDetails(firstName, lastName) {
        const politician = GovTrack.supportedPoliticians[firstName + lastName];
        if (!politician) return {'Error' : `Politician ${firstName + " " + lastName} not supported`};

        const id = GovTrack.getPoliticianId(firstName, lastName, politician['chamber'], politician['congressNum']);
        const url = `https://api.propublica.org/congress/${GovTrack.apiVersion}/members/${id}.json`;
        const jsonData = GovTrack.getRequest(url);
        jsonData['results'][0]['bio'] = BioguideScraper.getBio(id);

        return jsonData;
    }

    static getPoliticianBio(firstName, lastName) {
        const details = GovTrack.getPoliticianDetails(firstName, lastName);
        if (!('Error' in details)) {
            return details['results'][0]['bio'];
        }
        return details;
    }
}

// static class variables
GovTrack.apiHeaderKey = 'X-API-Key';
GovTrack.apiKey = 'OTozN0dFdEQXKUu7PCAYO16Tofnamt0El3xVk6gp';
GovTrack.apiVersion = 'v1';
GovTrack.supportedPoliticians = {
    'BernardSanders': {'chamber': 'senate', 'congressNum': '115'},
    'HillaryClinton': {'chamber': 'senate', 'congressNum': '110'}
};


function test() {
    console.log(GovTrack.getPoliticianBio('Bernard', 'Sanders'));
    console.log(GovTrack.getPoliticianDetails('Bernard', 'Sanders'));
    console.log(GovTrack.getPoliticianDetails('Hillary', 'Clinton'));
    console.log(GovTrack.getPoliticianDetails('Jake', 'Toriyama'));
}

// test();

module.exports = GovTrack;

