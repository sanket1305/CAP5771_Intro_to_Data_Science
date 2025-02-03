# this commands are the shell version of what we did in python
# we can use any of them, from terminal
# or we can just run this file by commenting either of the commands

URL='https://nominatim.openstreetmap.org/search.php?q=Compton%2C+California&format=json'

# curl -s "${URL}" > citydata.json
wget -O citydata.json ${URL}