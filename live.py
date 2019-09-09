import pyshark
print("Live Capture")
cap=pyshark.LiveCapture(interface='en1')
cap.sniff(packet_count=20,timeout=50)
print(cap)
for pkt in cap:
	print(pkt)

def apply_filter(cap):
	print()
	n=int(input("1.Display layers available in each packet\n2.length of the packets\n"))
	print()
	if n==1:
		for i in range(20):
			print()
			print("Layer available in packet:",i)
			print(cap[i].layers)
			print()
		print("Filter on layers")
		m=int(input("1. ip\n2. ETH\n"))
		if m==1:
			for i in range(20):
				print()
				print("Packet: ",i)
				print(cap[i].ip)
				print()
		if m==2:
			for i in range(20):
				print()
				print("Packet: ",i)
				print(cap[i].eth)
				print()
		
	if n==2:
		for i in range(20):
			print()
			print("Packet:" ,i)
			print(cap[i].length ,"bytes")
			print()


def file_write(cap):
	out_string = ""
	i = 1
	for pkt in cap:
		out_file = open("Live_capture.txt", "w")
		out_string += "Packet #         " + str(i)
		out_string += "\n"
		out_string += str(pkt)
		out_string += "\n"
		out_file.write(out_string)
		i = i + 1
	cap.close()
	
n=int(input("1. Filter \n2. Write in a file\n"))
if n==1:
	apply_filter(cap)
elif n==2:
	file_write(cap)
