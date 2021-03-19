# ARIJIT BHOWMICK [sys41414141]


file = open('usb-ripper/auth.json', "r")
file_content = file.read()
file.close()

sys_log_ = open('usb-ripper/syslog', 'r')
sys_log = sys_log_.readlines()
sys_log_.close()

checked_serial = []

def serial_checker(serial):

		
	global checked_serial
	global invalid_serials

	if (serial not in checked_serial):
	
		checked_serial+=[serial]
		
		if (serial not in file_content):
			
			print(f"Invalid Serial : {serial}")

			invalid_serials_file = open("invalid_serials.txt", "a")
			invalid_serials_file.write(serial+"\n")
			invalid_serials_file.close()

		else:
			pass

	else:
		pass


for line in sys_log:
	if ("SerialNumber: " in line) == True:

		serial_checker(line.split("SerialNumber: ")[1].replace("\n", ""))
	else:
		continue

print("""Serial Checking Completed

Invalid serials are noted in \'invalid_serials.txt\' file""")