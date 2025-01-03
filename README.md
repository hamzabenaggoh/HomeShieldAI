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

To install snortML as a docker container (was very helpful!):

https://github.com/ettorecalvi/snortml2docker

For the CICflowmeter as a docker container:

https://github.com/hamelin/cicflowmeter-docker

Using some code from Western-OC2-Lab for ML models:

@ARTICLE{9443234,
  author={Yang, Li and Moubayed, Abdallah and Shami, Abdallah},
  journal={IEEE Internet of Things Journal}, 
  title={MTH-IDS: A Multitiered Hybrid Intrusion Detection System for Internet of Vehicles}, 
  year={2022},
  volume={9},
  number={1},
  pages={616-632},
  doi={10.1109/JIOT.2021.3084796}}


## Caviats


-add guide for setting up flowmeter on mac devices or specify this