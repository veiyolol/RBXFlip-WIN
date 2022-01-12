import time, requests, json

def main(tid):
	headers = {"Content-Type": "application/json"}
	datas = {"jsonrpc":"2.0","method":"getTicket","params":{"ticketId":tid},"id":2623}
	dataj = json.dumps(datas)

	req = requests.post("https://api.random.org/json-rpc/4/invoke", data=dataj, headers=headers)
	res = req.text
	resjson = json.loads(res)
	#print(res)

	if "The ticket you specified does not exist" in res:
		print("Invalid Ticket ID.")
		return
	elif resjson["result"]["serialNumber"] == None:
		#print("Waiting for the match to start...")
		time.sleep(1.5)
		main(tid)
		return
	else:
		try:
			if float(resjson["result"]["result"]["random"]["data"][0]) >= 0.5:
				print("Tix Wins!")
			else:
				print("Bux Wins!")
		except:
			print("Error!")

while True:
	tid = input("Ticket ID: ")
	main(tid)
	time.sleep(1)
