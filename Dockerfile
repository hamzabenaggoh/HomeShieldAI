# FROM ubuntu:22.04
FROM --platform=linux/amd64 ubuntu:22.04

RUN apt update -y
RUN apt upgrade -y
RUN apt install -y gradle maven git libpcap-dev tcpdump tshark

RUN git clone https://github.com/ahlashkari/CICFlowMeter /code
RUN cd /code/jnetpcap/linux/jnetpcap-1.4.r1425 && \
    mvn install:install-file \
        -Dfile=jnetpcap.jar -DgroupId=org.jnetpcap -DartifactId=jnetpcap \
        -Dversion=1.4.1 -Dpackaging=jar
WORKDIR /code
RUN gradle --no-daemon build

COPY capture_traffic.sh /capture_traffic.sh
COPY process_pcap.sh /process_pcap.sh
RUN chmod +x /capture_traffic.sh /process_pcap.sh

COPY gradle-task /gradle-task
RUN cat /gradle-task >>build.gradle && rm /gradle-task

COPY go /go
RUN chmod 500 /go
ENTRYPOINT ["/go"]
