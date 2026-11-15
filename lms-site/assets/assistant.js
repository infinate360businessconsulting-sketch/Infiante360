
/* Search-based help assistant. Finds the closest published answer; it does not generate text and stores nothing. */
(function(){
var WA=window.__WA||'',KB=[];
var STOP='a an the and or of to in on for with is are was be it this that what how why when where do does can i you my me we our about from at as by not no if then so'.split(' ');
function tok(s){return (s.toLowerCase().match(/[a-z0-9_]+/g)||[]).filter(function(w){return STOP.indexOf(w)<0&&w.length>1})}
var btn=document.createElement('button');btn.id='asst-btn';btn.type='button';btn.textContent='Ask the LMS assistant';btn.setAttribute('aria-expanded','false');
var box=document.createElement('div');box.id='asst';box.setAttribute('role','dialog');box.setAttribute('aria-label','LMS help assistant');
var hd=document.createElement('div');hd.className='hd';hd.textContent='LMS assistant (answers from published pages)';
var log=document.createElement('div');log.className='log';log.setAttribute('aria-live','polite');
var form=document.createElement('form');var inp=document.createElement('input');inp.type='text';inp.placeholder='Ask about access, simulators, AEP...';inp.setAttribute('aria-label','Your question');
var go=document.createElement('button');go.className='btn pri';go.type='submit';go.textContent='Ask';form.appendChild(inp);form.appendChild(go);
box.appendChild(hd);box.appendChild(log);box.appendChild(form);document.body.appendChild(btn);document.body.appendChild(box);
function add(cls,node){var d=document.createElement('div');d.className='m '+cls;d.appendChild(node);log.appendChild(d);log.scrollTop=log.scrollHeight}
function txt(s){return document.createTextNode(s)}
function link(h,t){var a=document.createElement('a');a.href=h;a.textContent=t;a.rel='noopener';return a}
add('',txt('Hi. I answer from the pages and knowledge base on this site. I am a search tool, not a person, and I can be wrong. Check Adobe documentation for product details.'));
fetch((window.__ROOT||'')+'assets/kb.json').then(function(r){return r.json()}).then(function(j){KB=j}).catch(function(){});
btn.addEventListener('click',function(){var o=box.classList.toggle('open');btn.setAttribute('aria-expanded',o);if(o)inp.focus()});
form.addEventListener('submit',function(e){e.preventDefault();var q=inp.value.trim();if(!q)return;inp.value='';
var u=document.createDocumentFragment();u.appendChild(txt(q));add('u',u);
var qt=tok(q),sc=KB.map(function(k){var t=tok(k.q+' '+k.a+' '+k.t),n=0;qt.forEach(function(w){if(t.indexOf(w)>-1)n++;if(k.q.toLowerCase().indexOf(w)>-1)n+=1});return {k:k,n:n}}).filter(function(x){return x.n>=2}).sort(function(a,b){return b.n-a.n}).slice(0,2);
var f=document.createDocumentFragment();
if(!sc.length){f.appendChild(txt('I could not find a close answer. '));f.appendChild(link(WA+'?text='+encodeURIComponent('Hi, I need help: '+q),'Ask the team on WhatsApp'))}
else sc.forEach(function(x,i){var p=document.createElement('p');var b=document.createElement('strong');b.textContent=x.k.q;p.appendChild(b);p.appendChild(document.createElement('br'));p.appendChild(txt(x.k.a+' '));p.appendChild(link(x.k.u,'Open'));f.appendChild(p)});
add('',f)})
})();
