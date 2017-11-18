import linode

client = linode.LinodeClient('%%%YOU_WILL_NEED_TO_SUBSTITUE_A_KEY_HERE%%%%%')
print "\nGetting Regions:"
print "================"
for r in client.get_regions():
  print(r.id)

types = client.linode.get_types()
print "\nGetting Types:"
print "=============="
for t in types:
  print(t.id)

distributions = client.linode.get_distributions()
print "\nGetting Distributions:"
print "======================"
for d in distributions:
  print(d.id)
type="g5-standard-1"
region="us-east-1a"
distribution="linode/centos7"
l, pw = client.linode.create_instance(type, region, distribution)
if not l:
  raise RuntimeError("it didn't work")
while not l.status == 'running':
  pass
ip = ' '.join(l.ipv4)
print "IP is:"
print ip
print "Password is:"
print pw
ip_file = open("ip_address", "w")
ip_file.write("[webservers]\n")
ip_file.write(ip)
ip_file.close()
pw_file = open("password", "w")
pw_file.write(pw)
pw_file.close()

