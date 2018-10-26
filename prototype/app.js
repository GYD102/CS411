const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const GovTrack = require('./data/apis/govTrack');
const app = express();

app.use(bodyParser.urlencoded({
    extended: true
}));

app.use(bodyParser.json());


// web form
app.get("/", function(request, response){
    response.sendFile(path.join(__dirname + '/public/index.html'));
});

// submission result
app.post('/', function(req, res) {

    const capitalize = (string) => string.charAt(0).toUpperCase() + string.slice(1);

    const firstName = capitalize(req.body.politician.firstName);
    const lastName = capitalize(req.body.politician.lastName);
    const politicianData = GovTrack.getPoliticianDetails(firstName, lastName);
    console.log(politicianData);

    if (politicianData.Error) {
        res.send('error, ' + firstName + " " + lastName + " not a valid senator");
    }

    else {
        res.render('politicianDetails.ejs',
            {
                data: politicianData,
                name: firstName + " " + lastName,
            });
    }
});

app.listen(3000, function(){
    console.log("listening on port 3000");
});
