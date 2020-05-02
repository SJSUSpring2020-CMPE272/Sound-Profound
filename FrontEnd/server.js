#! /usr/bin/env node



const express = require("express");

const app = express();


const path = require("path");
const publicPath = path.join(__dirname);
app.use(express.static(publicPath));




//Host react application on root url
app.get("/", (req, res) => {
  res.sendFile(path.join(publicPath, "SoundProfund.html"));
});


app.listen(3000, () => {
  console.log("Server running on port: %d", 3000);
});

