
import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral
 
temp_uuid = UUID(0x0001)

p = Peripheral("CA:34:A7:E4:DF:50", "random")
 
try:
    print("hello")
    ch = p.getCharacteristics(uuid=temp_uuid)
    #print(ch)
    for i in ch:
        print(i)
        if (i.supportsRead()):
            while 1:
                print("ayyyy")
                val = binascii.b2a_hex(ch.read())
                val = binascii.unhexlify(val)
                val = struct.unpack('f', val)[0]
                print(str(val) + " ay")
                time.sleep(1)
    print("after")
 
finally:
    p.disconnect()
