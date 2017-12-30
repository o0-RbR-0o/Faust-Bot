from lxml import html
import requests
import sys
if len(sys.argv)>2:
	arg_command=sys.argv[1]
	arg_parameter=sys.argv[2]
else:
	print("Wrong argument count.")
	exit()
	
if arg_command=="add":
	print("Add parcel");
	exit()
	
if arg_command=="status":
	if arg_parameter=="all":
		print("Status for all shipments")
		exit()
	print("Status for shipment "+arg_parameter)
	exit()


url='https://nolp.dhl.de/nextt-online-public/de/search?piececode='+str(sys.argv[1])
tree = html.fromstring((requests.get(url)).content)

status_date=tree.xpath('//div[@class="well well-status"]/h2/text()')
status_filiale=tree.xpath('//div[@class="well well-status"]/p/a/text()')
status_message=tree.xpath('//div[@class="well well-status"]/p/text()')

status= "No information for this shipment available"
if  len(status_date) > 0 and len(status_message) > 0 :
	status=''.join(status_message)
	if len(status_filiale) > 0:
		status= status_date[0]+" : "+status_message[0]+status_filiale[0]+status_message[1];
print(status)