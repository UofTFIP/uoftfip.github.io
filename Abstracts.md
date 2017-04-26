---
layout:     page
title:      Abstracts
subtitle:   Abstracts in this year's FIP
header-img: "img/home-bg.jpg"
category: abstracts
---
{% for post in site.posts %}
{% if post.category == page.category %}
<div class="post-preview">
    <a href="{{ post.url | prepend: site.baseurl }}">
        <h2 class="post-title">            {{ post.title }}
        </h2>
        {% if post.subtitle %}
        <h3 class="post-subtitle">
            {{ post.subtitle }}
        </h3>
        {% endif %}
    </a>
</div>
<hr>
{% endif %}
{% endfor %}
