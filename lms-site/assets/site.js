
(function(){
var rb=document.getElementById('ribbon-x');if(rb)rb.addEventListener('click',function(){var r=document.getElementById('ribbon');if(r)r.remove();try{sessionStorage.setItem('rb','1')}catch(e){}});
try{if(sessionStorage.getItem('rb')){var r=document.getElementById('ribbon');if(r)r.remove()}}catch(e){}
var t=document.querySelector('.tilt');if(t&&!matchMedia('(prefers-reduced-motion:reduce)').matches){var s=t.parentNode;
s.addEventListener('mousemove',function(e){var b=s.getBoundingClientRect(),x=(e.clientX-b.left)/b.width-.5,y=(e.clientY-b.top)/b.height-.5;t.style.transform='rotateY('+(x*14)+'deg) rotateX('+(-y*14)+'deg)'});
s.addEventListener('mouseleave',function(){t.style.transform=''})}
var f=document.getElementById('kbq');if(f){var items=[].slice.call(document.querySelectorAll('[data-kb]')),c=document.getElementById('kbc');
function run(){var q=f.value.toLowerCase().trim(),n=0;items.forEach(function(d){var ok=!q||d.getAttribute('data-kb').indexOf(q)>-1;d.style.display=ok?'':'none';if(ok)n++});c.textContent=n+' of '+items.length+' answers'}
f.addEventListener('input',run);run()}
})();
