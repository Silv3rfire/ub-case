import os

extensions = ["sphinx_needs", "sphinxcontrib.plantuml"]

on_rtd = os.environ.get("READTHEDOCS") == "True"
if on_rtd:
    plantuml = "java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar"
else:
    plantuml = "java -jar %s" % os.path.join(
        os.path.dirname(__file__), "utils", "plantuml.jar"
    )

    plantuml_output_format = "png"
