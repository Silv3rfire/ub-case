import os
import sys
from pathlib import Path

from sphinx.application import Sphinx

project = "ub-case-demo"
author = "Lucas Silber"
needs_sphinx = "9.1.0"
sys.path.append(str(Path("../src").resolve()))
extensions = ["sphinx_needs", "sphinxcontrib.plantuml", "extensions"]

on_rtd = os.environ.get("READTHEDOCS") == "True"
if on_rtd:
    plantuml = "java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar"
else:
    plantuml = "java -jar %s" % os.path.join(
        os.path.dirname(__file__), "utils", "plantuml.jar"
    )

    plantuml_output_format = "png"

needs_links = {
    "specifies": {"incoming": "is specified by", "outgoing": "specifies"},
    "tests": {
        "incoming": "is tested by",
        "outgoing": "tests",
        "copy": False,
        "color": "#00AA00",
    },
}

csv_data_source = Path.cwd() / ".." / "uc_customer_project-1.csv"
needs_build_json = True


def setup(app: Sphinx):
    app.add_config_value("csv_data_source", csv_data_source, False)
