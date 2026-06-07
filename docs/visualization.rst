UB-Case Demo visualization
==========================

Here we can see some of the various visualization options that sphinx-needs provides with a X-as-Code approach out of the box. 

Table
-----

.. needtable::
   :style: table
   :columns: id, type, content

Needpies
--------

.. needpie:: Requirement status
   :labels: open
   :legend:
   :shadow:
   :text_color: crimson

   type == 'req' and status == 'open'

.. needpie:: All Types
   :labels: requirements, specifications, tests
   :legend: 

   type == 'req'
   type == 'spec'
   type == 'test'

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