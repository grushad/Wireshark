import pyshark
print("File Capture")
cap = pyshark.FileCapture('data.pcap')
n=int(input("1. Display\n2. Frame_info\n"))

def display(cap):
	for pkt in cap:
		print(pkt)

def filters(pkt):
	try:
		protocol =  pkt.transport_layer
		src_addr = pkt.ip.src
		src_port = pkt[pkt.transport_layer].srcport
		dst_addr = pkt.ip.dst
		dst_port = pkt[pkt.transport_layer].dstport
		print ('%s  %s:%s --> %s:%s' % (protocol, src_addr, src_port, dst_addr, dst_port))
	except AttributeError as e:
	#ignore packets that aren't TCP/UDP or IPv4
		pass


if n == 1:
	display(cap)
elif n ==2 :
	cap.apply_on_packets(filters)
