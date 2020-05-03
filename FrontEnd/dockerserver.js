#! /usr/bin/env node



const express = require("express");

const app = express();
const PORT = 8080;
const HOST = '0.0.0.0';

const path = require("path");
const publicPath = path.join(__dirname);
app.use(express.static(publicPath));




//Host react application on root url
app.get("/", (req, res) => {
  res.sendFile(path.join(publicPath, "SoundProfund.html"));
});


app.listen(PORT,HOST, () => {
  console.log("Server running on port: %d", PORT);
});

