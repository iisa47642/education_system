let express = require(`express`);
let app = express();
let port = 8000;

app.listen(port, function() {
    console.log(`http://localhost:${port}`);
});

let cors = require("cors");
app.use(cors({origin: 'http://localhost:5173'}));

app.use(express.json());

app.get("/route", function(req, res) {
    let s = "Hello world";
    res.send(s);
});