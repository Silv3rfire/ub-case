UB-Case Demo visualization
==========================

|Here we can see the various visualization options that sphinx-needs provides with a X-as-Code approach out of the box. 

Table
-----

.. needtable::
   :style: table
   :columns: id, type, title

.. needpie:: Requirement status
   :labels: open
   :legend:
   :shadow:
   :explode: 0   
   :text_color: crimson

   type == 'req' and status == 'open'

Needflow
--------

.. needflow:: Sample Needflow
    :alt: Sample Needflow
    :config: lefttoright
    :show_link_names:
    :border_color:
        [status == 'open']:FF0000,
        [status == 'in progress']:0000FF,
        [status == 'closed']:00FF00