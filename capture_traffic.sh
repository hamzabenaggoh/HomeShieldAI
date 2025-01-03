#!/bin/bash

PCAP_DIR="/pcap"
mkdir -p $PCAP_DIR

INTERFACE="eth0"
CAPTURE_TIME=15 
CAPTURE_COUNT=10 

for i in $(seq 1 $CAPTURE_COUNT); do
    PCAP_FILE="$PCAP_DIR/$(date +%Y-%m-%d_%H-%M-%S)_$i.pcap"
    echo "Capturing traffic for $CAPTURE_TIME seconds into $PCAP_FILE (Capture $i of $CAPTURE_COUNT)"
    
    # tcpdump -i $INTERFACE -w $PCAP_FILE -G $CAPTURE_TIME
    # tcpdump -i eth0 -w $PCAP_FILE -G $CAPTURE_TIME 2>&1 | tee /tmp/tcpdump.log
    tcpdump -i eth0 -w $PCAP_FILE -G $CAPTURE_TIME -W 1 || echo "Timeout or no packets captured"
    # tcpdump -i eth0 -w $PCAP_FILE -G $CAPTURE_TIME
    echo "Captured traffic for $CAPTURE_TIME seconds into $PCAP_FILE"
    
    /process_pcap.sh "$PCAP_FILE"
done
