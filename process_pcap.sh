#!/bin/bash

# Ensure a PCAP file is passed as an argument
if [ -z "$1" ]; then
    echo "Error: No PCAP file provided."
    exit 1
fi

# Assign the provided PCAP file to a variable
PCAP_FILE="$1"
FLOW_DIR="/flow"
mkdir -p $FLOW_DIR

# Ensure the PCAP file exists
if [ ! -f "$PCAP_FILE" ]; then
    echo "Error: PCAP file '$PCAP_FILE' does not exist."
    exit 1
fi

# Process the provided PCAP file with CICFlowMeter using Gradle
echo "Processing provided PCAP file: $PCAP_FILE"
gradle --no-daemon -Pcmdargs="$PCAP_FILE:$FLOW_DIR" runcmd

# Check if Gradle task ran successfully
if [ $? -eq 0 ]; then
    echo "Successfully ran Gradle task with $PCAP_FILE"
else
    echo "Error running Gradle task with $PCAP_FILE"
    exit 1
fi
