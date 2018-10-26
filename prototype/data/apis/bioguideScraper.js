const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const cheerio = require('cheerio');

class BioguideScraper {

    static getBio(politicianId) {

        const url = `http://bioguide.congress.gov/scripts/biodisplay.pl?index=${politicianId}`;
        const request = new XMLHttpRequest();
        request.open("GET", url, false);   // XMLHttpRequest.open(method, url, async)
        request.send();

        const $ = cheerio.load(request.responseText);
        return $('p').text().replace(/\n/g, '');
    }
}

function test() {
    const politicianId = 'S000033';
    const res = BioguideScraper.getBio(politicianId);
    console.log(res);
}

// test();

module.exports = BioguideScraper;
