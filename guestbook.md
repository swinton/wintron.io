---
layout: guestbook
redirect_from: "/guestbook/"
---

## Please sign my guestbook

<form id="sign" method="post" action="https://api.wintron.io/guestbook">
<div>
<label for="name">Name:</label>
<input id="name" type="text" placeholder="Your name" autofocus />
</div>
<div>
<label for="message">Message:</label>
<textarea id="message" rows="8" placeholder="Your message"></textarea>
</div>
<input type="submit" value="Sign" />
</form>


___

## Previous entries

<ul id="entries">

</ul>
