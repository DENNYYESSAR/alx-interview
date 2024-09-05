#!/usr/bin/node

const request = require('request');

// Check if a movie ID is provided as an argument.
// The script expects the movie ID as the third argument in the command line.
// If no movie ID is provided, the script will print a usage message and exit.
if (process.argv.length !== 3) {
  console.error('Usage: ./<script> <Movie ID>');
  process.exit(1);
}

// Fetch the movie ID from the command line argument.
// Construct the API URL using the provided movie ID.
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make an API request to fetch the movie details using the constructed URL.
// If there's an error in the request, it will be printed and the script will exit.
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body to extract movie data, particularly the 'characters' field,
  // which contains a list of URLs pointing to character details.
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // For each character URL in the 'characters' array, make a separate request to fetch
  // the character's details. Once fetched, print the character's name.
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse the character data and print the character's name to the console.
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
