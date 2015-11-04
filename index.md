---
layout: page
title: ABCD
//tagline : Supporting tagline
---
{% include JB/setup %}
{% include header.html %}

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>


{% include googleanalytics.html %}
{% include footer.html %}




