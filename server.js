const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const cors = require("cors");
const companyRoutes = require("./controllers/companies");
const fs = require("fs");
const { spawnSync } = require("child_process");
const redis = require("redis");
const REDIS_PORT = process.env.PORT || 6379;

const client = redis.createClient(REDIS_PORT);

client.on("error", err => {
  console.log("Error " + err);
});

const app = express();
const port = 3000;
app.use(cors());
app.use(bodyParser.json());
app.use(
  bodyParser.urlencoded({
    extended: true
  })
);
app.use(express.static("build"));

// run a python script, takes a file name as a parameter
function runScript(file, args) {
  // establish the tail of the python script call
  tail = [path.join(__dirname, "../python", file)];

  // add each argument to the tail
  args.forEach(item => {
    tail.push(item);
  });

  // run the python script
  return spawnSync("python", tail);
}

// run investment.py upon receiving a request for stock information
app.post("/investment", (req, res) => {
  const company = req.body.company;
  client.get(company, (err, response) => {
    if (response) {
      res.send(JSON.parse(response));
    } else {
      const stock = runScript("investment.py", [company]);

      // get historical stock data
      const history = runScript("historical.py", [company]);
      client.set(
        company,
        JSON.stringify([JSON.parse(stock.stdout), JSON.parse(history.stdout)]),
        "EX",
        30
      );

      // // send the data from the standard output of the python script
      res.send([JSON.parse(stock.stdout), JSON.parse(history.stdout)]);
    }
  });
});

// catch all
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "../src/index.html"));
});

app.listen(port, () => console.log(`listening on port ${3000}`));
