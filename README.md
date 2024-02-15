# Tribal Interview
## Endpoint Chuck Norris Problem

## How to execute
To avoid unused installations on your computers, I decide to create a Dockerfile to run the solution easily.

⁠ sh
git clone
docker build -t chuck_norris .
docker run -p 8080:8080 chuck_norris
 ⁠

After this you can do a GET Request to ⁠ http://localhost:8080/ ⁠ to get the result