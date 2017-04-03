import binascii
import array

def createPckt(src, dest, seq, acknum, syn, ack, end, window, payload):
	hdr = "%s|%i|%i|%i|%r|%r|%r|%i" % (str(src), int(dest), int(seq), int(acknum), syn, ack, end, int(window))
	hdrPart = str(hdr.split('|'))
	checksum = makeChecksum(hdrPart + payload)
	pckt = "%s|%s|%s" % (hdr, payload, checksum)
	return pckt

def unPack(pckt):
	parts = pckt.split('|')
	hdr = parts[0:8]
	payload = parts[8]
	checksum = parts[-1]
	return hdr, payload, checksum

def makeChecksum(pckt):
	return str(binascii.crc32(pckt) & 0xffffffff)

def checksum(pckt):
	hdr, payload, checksum = unPack(pckt)
	return makeChecksum(str(hdr) + str(payload)) == str(checksum)

def openFile(filename):
	try:
		f = open(filename, 'r')
	except:
		print "file not found"
		return None
	x = True
	l = []
	while(x):
		div = f.read(512)
		if (div != ""):
			l.append(div)
		else:
			x = False
	return l
