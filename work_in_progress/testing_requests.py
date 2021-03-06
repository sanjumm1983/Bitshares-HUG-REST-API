import requests
import json

full_node_list_http = [
	"https://bitshares.crypto.fans/ws", #location: "Munich, Germany"
	"https://bit.btsabc.org/ws", #location: "Hong Kong"
	"https://api.bts.blckchnd.com", #location: "Falkenstein, Germany"
	"https://openledger.hk/ws", #location: "Hong Kong"
	"https://bitshares-api.wancloud.io/ws", #location:  "China"
	"https://dex.rnglab.org", #location: "Netherlands"
	"https://dexnode.net/ws", #location: "Dallas, USA"
	"https://kc-us-dex.xeldal.com/ws", #location: "Kansas City, USA"
	"https://la.dexnode.net/ws", #location: "Los Angeles, USA"
	"https://eu.nodes.bitshares.works", #location: "Central Europe - BitShares Infrastructure Program"
	"https://us.nodes.bitshares.works", #location: "U.S. West Coast - BitShares Infrastructure Program"
	"https://sg.nodes.bitshares.works" #location: "Singapore - BitShares Infrastructure Program"
]

def request_json(input_data):
	"""Request JSON data from full node, given request data input.
	   More info: http://docs.python-requests.org/en/master/"""
	requested_data = None # Prevent no state if all servers fail!

	for full_node_url in full_node_list_http:
		try:
			requested_data = requests.get(full_node_url, data=input_data)
		except requests.exceptions.ConnectionError as err:
			print("...")
			print("Error: {}".format(full_node_url))
			print(err)
			print("...")
			continue

		if requested_data.status_code is not 200:
			# Fail! Move onto the next URL!
			print("./\/\/\.")
			print("Not online: {}".format(full_node_url))
			print(".\/\/\/.")
			continue
		else:
			print("---")
			print("Online: {}".format(full_node_url))
			print(requested_data)
			num_workers = json.loads(json.dumps(requested_data.text))
			print(num_workers)
			print("===")
			continue

	return requested_data

num_workers_request = request_json('{"jsonrpc": "2.0", "method": "get_worker_count", "params": [], "id": 1}')
