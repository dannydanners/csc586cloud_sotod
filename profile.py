import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
# Create a XenVM
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node.routable_control_ip = "true"

node2 = request.XenVM("webserver")
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node2.routable_control_ip = "true"
node2.addService(rspec.Execute(shell="/bin/bash", command="sudo apt-get update && sudo apt-get install -y apache2 && sudo systemctl start apache2 && sudo apt -y install nfs-common"))

node3 = request.XenVM("observer")
node3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node3.routable_control_ip = "false"
node3.addService(rspec.Execute(shell="/bin/bash", command="sudo apt-get update && sudo apt -y install nfs-kernel-server"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
