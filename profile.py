import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
# Create a XenVM
#node = request.XenVM("node")
#node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
#node.routable_control_ip = "true"

node_webserver = request.XenVM("webserver")
node_webserver.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node_webserver.routable_control_ip = "true"
node_webserver.addService(rspec.Execute(shell="/bin/bash", command="sudo apt-get update && sudo apt-get install -y apache2 && sudo systemctl start apache2 && sudo apt -y install nfs-common"))
iface0 = node_webserver.addInterface('interface-1', rspec.IPv4Address('10.1.1.2','255.255.255.0'))

node_observer = request.XenVM("observer")
node_observer.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node_observer.routable_control_ip = "false"
node_observer.addService(rspec.Execute(shell="/bin/bash", command="sudo apt-get update && sudo apt -y install nfs-kernel-server"))
iface1 = node_observer.addInterface('interface-0', rspec.IPv4Address('10.1.1.1','255.255.255.0'))

# Link nfs-link
link_nfs_link = request.Link('nfs-link')
link_nfs_link.Site('undefined')
link_nfs_link.addComponentManager('urn:publicid:IDN+emulab.net+authority+cm')
iface1.bandwidth = 100000
link_nfs_link.addInterface(iface1)
iface0.bandwidth = 100000
link_nfs_link.addInterface(iface0)

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
