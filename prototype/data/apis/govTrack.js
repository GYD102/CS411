const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const BioguideScraper = require('./bioguideScraper');
const senators = require('../senators');

class GovTrack {

    static getRequest(url) {
        const request = new XMLHttpRequest();
        request.open("GET", url, false);   // XMLHttpRequest.open(method, url, async)
        request.setRequestHeader(GovTrack.apiHeaderKey, GovTrack.apiKey);
        request.send();
        return JSON.parse(request.responseText);
    }

    static getPoliticianDetails(firstName, lastName) {
        if (!senators[firstName + ' ' + lastName]) return {'Error' : `Politician ${firstName + " " + lastName} not supported`};

        const id = senators[firstName + " " + lastName];
        const detailsUrl = `https://api.propublica.org/congress/${GovTrack.apiVersion}/members/${id}.json`;
        const jsonData = GovTrack.getRequest(detailsUrl);
        jsonData['results'][0]['bio'] = BioguideScraper.getBio(id);

        return jsonData['results'][0];
    }
}

// static class variables
GovTrack.apiHeaderKey = 'X-API-Key';
GovTrack.apiKey = 'OTozN0dFdEQXKUu7PCAYO16Tofnamt0El3xVk6gp';
GovTrack.apiVersion = 'v1';


const test = false;
if (test) {
    console.log(
        GovTrack.getPoliticianDetails('Bernie', 'Sanders')
    );
}

module.exports = GovTrack;

