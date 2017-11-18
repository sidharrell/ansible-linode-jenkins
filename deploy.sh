#!/bin/bash
echo "Who am I?"
whoami

echo "Running python deploy.py, which builds the vm using the linode api"
python deploy.py

ip=`grep -v "\[" ip_address`
pw=`cat password`
gandalf=1
while [ "$gandalf" -ne "0" ];
do
    echo "Thou shalt not pass until the ssh daemon is spun from the fell depths!!!!"
    sleep 5
    status=$(ssh -o BatchMode=yes -o ConnectTimeout=5 $ip echo ok 2>&1)
    if [[ "$status" == *"Host key verification failed."* ]]; then gandalf=0; fi
done
echo "Clearing the foul stench of host key verification!!!"
ssh -o "StrictHostKeyChecking no"  root@$ip
echo "Planting the seed of my control over this new realm!!"
sshpass -f password ssh-copy-id root@$ip
echo "There can be only one!!!"
rm password
echo "My hand stretches forth!!!"
ansible-playbook -i ip_address playbook.yml