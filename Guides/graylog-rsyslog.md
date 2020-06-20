# Graylog rsyslog setup

Edit the following file.
```
sudo vim /etc/rsyslog.d/90-default.conf
```
adding
```
*.* @192.168.1.225:8514;RSYSLOG_SyslogProtocol23Format
```
alternativly for convienance 

``` 
echo "*.* @192.168.1.225:8514;RSYSLOG_SyslogProtocol23Format" > /etc/rsyslog.d/90-default.conf
```

then restart the rsyslog service

``` 
sudo systemctl restart rsyslog.service
```