const GovTrack = require('./apis/govTrack');
const express = require('express');

const app = express();
const cors = require('cors');
const port = process.env.PORT || 5000;  // sets the port that express will run on

// avoids No 'Access-Control-Allow-Origin' - Node / Apache Port Issue
app.use(cors({origin: 'http://localhost:3000'}));


app.get('/express_backend', (req, res) => {
    res.send({ express: 'OOOO' });
});


app.get('/apis/govTrack/bio/:firstName/:lastName', (req, res) => {
    const firstName = req.params.firstName;
    const lastName = req.params.lastName;
    const bio = GovTrack.getPoliticianBio(firstName, lastName);

    res.send({'bio': bio});
});



app.listen(port, () => console.log(`Listening on port ${port}`));
