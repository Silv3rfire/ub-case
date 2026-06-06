UB-Case Demo data
=================

{% for req in requirements %}
.. req:: {{req.id}}
    :id: {{req.id}}
    :status: {{req.status}}

    {{req.content}}
{% endfor %}

{% for spec in specifications %}
.. spec:: {{spec.id}}
    :id: {{spec.id}}
    :status: {{spec.status}}
    :specifies: {{spec.links}}

    {{spec.content}}
{% endfor %}

{% for test in tests %}
.. test:: {{test.id}}
    :id: {{test.id}}
    :status: {{test.status}}
    :tests: {{test.links}}

    {{test.content}}
{% endfor %}
