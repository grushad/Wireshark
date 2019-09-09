# Wireshark

### Some features of wireshark are implemented using the python library pyshark

The features implemented are:
* Capturing live data packets.
* Filtering these data packets on the basis of layers which are:
    * ETH
    * ip
* Filtering these data packets and find out the length of each data packet.
* Saving the contents in a file.
* Reading a ".pcap" file.
* Displaying the data packets after reading from the file.
* Displaying the frame information for each packet which includes:
    * Protocol
    * Source Address
    * Source Port
    * Destination Address
    * Destination Port

### Requirements
* Python3 (pyshark does not work with python2)
* pyshark 


The following command can be used to install pyshark.
```
pip install pyshark

```
