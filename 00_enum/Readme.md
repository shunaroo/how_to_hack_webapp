## Finding SUID Binaries
```
find / -perm -u=s -type f 2>/dev/null
```
## Create Salt Passwd
```
openssl passwd -1 -salt [salt] [password]
```
