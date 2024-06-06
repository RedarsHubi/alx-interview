#!/usr/bin/node
const request = require('request');

function getCharacters (movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data:', error);
      return;
    }

    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      const characterUrls = data.characters;

      const characterPromises = characterUrls.map((characterUrl) => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
              reject.error('Error fetching character data:', charError);
            } else if (charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              resolve(characterData.name);
            } else {
              reject.error('Error fetching character data:', charResponse.statusCode);
            }
          });
        });
      });

      Promise.all(characterPromises)
        .then((characterNames) => {
          characterNames.forEach((name) => {
            console.log(name);
          });
        })
        .catch((err) => {
          console.error(err);
        });
    } else {
      console.error('Error fetching movie data:', response.statusCode);
    }
  });
}

const movieId = process.argv[2];
getCharacters(movieId);
