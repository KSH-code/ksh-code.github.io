---
title: Review
layout: page
pagination:
    enabled: true
---

<section class="list">
	{% if site.posts.size == 0 %}
		<p class="text-center">Nothing published yet!</p>
	{% elsif site.pagination.enabled %}
		{% for post in paginator.posts %}
			{% if post.category == 'review' %}
				{% if post.hidden != true %}
					{% include blog-post.html %}
				{% endif %}
			{% endif %}
		{% endfor %}

    	{% include pagination.html%}
    {% else %}
    	{% for post in site.posts %}
    		{% if post.category == 'review' %}
    			{% if post.hidden != true %}
    				{% include review-post.html %}
    			{% endif %}
    		{% endif %}
    	{% endfor %}
    {% endif %}

</section>