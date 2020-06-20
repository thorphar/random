# Setting up a Zabbix Agent - Ubuntu

Firstly, download the zabbix agent packages

```
sudo apt install zabbix-agent -y
```
Then the zabbix agent needs to be configured. Open the configure file ready for editing.

```
sudo vim /etc/zabbix/zabbix_agentd.conf
```

Uncomment the following

- `DebugLevel=3`
- `EnableRemoteCommands=1`
- `LogRemoteCommands=1`
- `Server=192.168.1.232`
- `ListenPort=10050`
- `ServerActive=192.168.1.232`
- `HostnameItem=system.hostname`

Comment the following

- `Hostname=Zabbix server`

Then restart the zabbix agent service

`sudo systemctl restart zabbix-agent.service`

If `ufw` is enabled then you will need to create a firewall rule.

```
sudo ufw allow from 192.168.1.232 proto tcp to any port 10050
```