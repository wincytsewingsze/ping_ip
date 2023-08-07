import os

# Read hostnames from txt file and transform to a list
with open("Hostnames.txt") as file:
  hostnames = file.read().splitlines()
  # print(hostnames)

for hostname in hostnames:
  res = os.popen(f"ping {hostname}").read()

  if("Received = 4" in res):
    print(hostname, "is UP")
  else:
    print(hostname, “is DOWN")
