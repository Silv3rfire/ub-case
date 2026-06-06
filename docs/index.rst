.. Sphinx-Needs Demo documentation master file, created by
   sphinx-quickstart on Mon Feb 12 16:32:39 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

UB-Case Demo
============

.. req:: The system shall control the front windshield wiper speed based on rain intensity,open
    :id: REQ_1
    :status: open

.. spec:: The system shall support at least three wiper speed levels (low medium high)
    :id: SPEC_1
    :status: open
    :links: REQ_1

.. test:: Verify that the system switches to low speed when light rain is detected,open
    :id: TEST_1
    :status: open
    :links: REQ_1

.. needflow:: Sample Needflow
    :alt: Sample Needflow
    :root_id: REQ_1
    :config: lefttoright
    :show_link_names:
    :border_color:
        [status == 'open']:FF0000,
        [status == 'in progress']:0000FF,
        [status == 'closed']:00FF00