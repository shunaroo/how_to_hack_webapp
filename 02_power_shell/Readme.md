# Basic

## help
```
Get-Help xxxxx

Get-Command Verb-*
ex:
Get-Command New-*
Get-command | measure

```

## Object
```
show method and properties
Verb-Noun | Get-Member
ex:
Get-Command | Get-Member -MemberType Method

select view items
Select-Object
ex:
Get-ChildItem　| Select-Object -Property Mode, Name

pattern-match
Verb-Noun | Where-Object -Property PropertyName -operator Value
Verb-Noun | Where-Object {$_.PropertyName -operator Value}
ex:
Get-Service | Where-Object -Property status -eq Stopped

Verb-Noun | Sort-Object

sort
Verb-Noun | Sort-Object
ex:
Get-ChildItem | Sort-Object
```

## Net Environment Address
```
Address
Get-NetIPAddress

Open port
Get-NetTCPConnection | Where-Object State -EQ Listen

patch
Get-HotFix|Where-Object HotFixID -EQ KB4023834
```

## file manu
```
list and search files
Get-ChildItem -Path C:\ -Include *.txt -File -Recurse -ErrorAction SilentlyContinue

cat
Get-Content -Path xxxxx

pwd
Get-Location

check where the path exists
Test-Path "C:\xxxxx"
```


## encode
```
hash
Get-FileHash 'target' -Algorithm MD5
base64
$data = Get-Content 'target' 
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($data)) | Out-File -Encoding "ASCII" out.html
```

## Account
```
list user
Get-LocalUser | Select-Object Name, SID

Get-LocalGroup| Measure-Object
```


# ref
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-6
