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

## Get-ChildItem
list and search files
```
Get-ChildItem -Path C:\ -Include *.txt -File -Recurse -ErrorAction SilentlyContinue
```



# ref
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-6
