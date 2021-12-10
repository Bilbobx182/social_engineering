## SOCIAL ENGINEERING

Question this repo attempts to answer :

How many people actually scan QR codes? We see them on posters, art, stickers on poles.
But do people scan the QR codes and go to URLs? Certainly that could bring some risk being brought to sites they may not way.

### What it is

This is just a flask server that runs on an EC2 instance within a docker container.
It will log each entry to the server.
We also have helper code to convert IPs to country of origin.

When running, it's assumed that an SSL certificate will exist for flask to execute on the host machine.
`/etc/letsencrypt/live/taifuwiddies.net:/ssl`

### Build

To build the docker images do `./bin/build.sh`