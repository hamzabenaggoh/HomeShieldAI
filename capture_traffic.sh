#!/bin/bash

# Directory to store captured PCAP files
PCAP_DIR="/code/captured_pcap"
mkdir -p $PCAP_DIR

# Network interface for capturing traffic (modify 'eth0' to match your interface)
INTERFACE="eth0"
CAPTURE_TIME=30 # Time in seconds to capture each batch of packets
CAPTURE_COUNT=10 # Number of captures to make

# Capture live traffic in batches according to time and save them as PCAP files, 10 times
for i in $(seq 1 $CAPTURE_COUNT); do
    PCAP_FILE="$PCAP_DIR/$(date +%Y-%m-%d_%H-%M-%S)_$i.pcap"
    echo "Capturing traffic for $CAPTURE_TIME seconds into $PCAP_FILE (Capture $i of $CAPTURE_COUNT)"
    
    # Capture traffic for the specified time duration and save to the PCAP file
    tcpdump -i $INTERFACE -w $PCAP_FILE -G $CAPTURE_TIME -W 1
    echo "Captured traffic for $CAPTURE_TIME seconds into $PCAP_FILE"
    
    # Process the captured PCAP file with CICFlowMeter
    /process_pcap.sh $PCAP_FILE
done



#Later add a way to delete old capture data