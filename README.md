# HomeShieldAI

This project is in ongoing development! Will add more details in here later as the project progresses.
Be on the lookout!


## The Vision


## Approach





## Run

to run cicflowmeter docker image

docker run --rm \                                                      
    -v "/Users/hamzabenaggoun/Desktop/HomeShieldAI/pcap_input:/pcap" \
    -v "/Users/hamzabenaggoun/Desktop/HomeShieldAI/pcap_output:/flow" \
    cfm:v2 /pcap /flow


## Setup steps

### Install snor3 docker image

docker pull ciscotalos/snort3
docker run --rm -it ciscotalos/snort3

useful commands for snort3 docker image:
./start.sh
./interact.sh
exit
docker stop snort3




## Credits

This project uses code for exploration purposes from the following repository:

https://github.com/TnTech-CEROC/adversarial_ml_ids



## Caviats


-add guide for setting up flowmeter on mac devices or specify this