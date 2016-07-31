---
layout: page
title: 厚積
//tagline : Supporting tagline
---
{% include JB/setup %}

{% include header.html %}

<ul class="posts">
  {% for post in site.posts %}
  <div class = "ind-posts">
    <li>
    <span>
    <img src = "/assets/img/icon.png" >
    {{ post.date | date_to_string }}
    </span> 
    &raquo;
     <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}
    </a>
    </li>
    </div>
  {% endfor %}
</ul>

{% include footer.html %}

{% include googleanalytics.html %}
