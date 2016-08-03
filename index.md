---
layout: page
title: 厚積
//tagline : Supporting tagline
---
<div id = "index-whole">

{% include JB/setup %}

{% include header.html %}

<ul class="posts">
  {% for post in site.posts %}
  <div class = "ind-posts">
    <li>
       <span>
       {% if post.icon %}
          <img src = "/assets/img/Icon/{{post.icon}}" height = "26"  width = "26">
       {% else %}
          <img src = "/assets/img/Icon/default.png" height = "26" width = "26">
       {% endif %}
          {{ post.date | date_to_string }}
       </span> 
     &raquo;
     <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}    </a>
    </li>
  </div>
  {% endfor %}
</ul>

{% include footer.html %}

{% include googleanalytics.html %}
</div>
