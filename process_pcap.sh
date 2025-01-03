#!/bin/bash

# Directory where the captured PCAP files are stored
PCAP_DIR="/code/captured_pcap"
OUTPUT_DIR="/code/flow_output"
mkdir -p $OUTPUT_DIR

# Path to the CICFlowMeter command or task
CIC_FLOW_METER_CMD="gradle --no-daemon -Pcmdargs=$1 runcmd"

# Process the PCAP file (input argument is the path to the PCAP file)
PCAP_FILE="$1"
if [ -f "$PCAP_FILE" ]; then
    echo "Processing $PCAP_FILE with CICFlowMeter..."

    # Run the CICFlowMeter task to generate flows from the PCAP file
    $CIC_FLOW_METER_CMD

    # Move the output flow CSV to the designated output folder
    mv "$PCAP_FILE" "$OUTPUT_DIR/$(basename $PCAP_FILE).csv"
    echo "Processed $PCAP_FILE into flow CSV"
else
    echo "PCAP file not found or invalid!"
fi
