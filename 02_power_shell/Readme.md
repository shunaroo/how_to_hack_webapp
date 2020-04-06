# Basic

## help
show help
```
Get-Help xxxxx
```

## Get-Command
list commands
```
Get-Command Verb-*
ex:
Get-Command New-*
Get-command | measure
```

## Get-Member
show method and properties
```
Verb-Noun | Get-Member
ex:
Get-Command | Get-Member -MemberType Method
```

## Select-Object
select view items
```
Select-Object
ex:
Get-ChildItem　| Select-Object -Property Mode, Name
```
## Where-Object
pattern-match
```
Verb-Noun | Where-Object -Property PropertyName -operator Value
Verb-Noun | Where-Object {$_.PropertyName -operator Value}
ex:
Get-Service | Where-Object -Property status -eq Stopped

Verb-Noun | Sort-Object
```
## Sort-Object
sort
```
Verb-Noun | Sort-Object
ex:
 Get-ChildItem | Sort-Object
```

## IP Address
```
Get-NetIPAddress
```

## Get-ChildItem
list and search files
```
Get-ChildItem -Path C:\ -Include *.txt -File -Recurse -ErrorAction SilentlyContinue
```

## Get-Contet
cat
```
 Get-Content -Path xxxxx
```

## Hash
```
Get-FileHash 'target' -Algorithm MD5
```
## base64
```
$data = Get-Content 'target' 
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($data)) | Out-File -Encoding "ASCII" out.html
```

## Get-LocalUser
list user
```
Get-LocalUser
Get-LocalUser | Select-Object Name, SID
```

## Group
```
Get-LocalGroup| Measure-Object
```



 ## Get-Location
pwd
```
Get-Location
```

## Test-Path
check where the path exists
```
Test-Path "C:\xxxxx"
```

# ref
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-6
