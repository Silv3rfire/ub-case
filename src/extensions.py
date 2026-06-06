from dataclasses import asdict, dataclass
from typing import Optional

import polars as pl
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util import logging

logger = logging.getLogger(__name__)


@dataclass
class NeedItem:
    id: str
    content: str
    status: str
    links: Optional[str] = None


def csv_import(app: Sphinx, env: BuildEnvironment, docnames: list[str]):
    """
    Populate html_context for jinja rendering
    """
    csv_path = env.config["csv_data_source"]
    if not csv_path.exists():
        logger.error("Configured csv_path {csv_path} is not valid", csv_path)
        raise FileNotFoundError(csv_path)

    csv_data = pl.read_csv(csv_path, quote_char=None)

    requirements = []
    tests = []
    specification = []
    current_req = ""
    current_sepc = ""
    for row in csv_data.iter_rows(named=True):
        title = row["Title"]
        if not title:
            # skip empty lines
            continue
        title = title.replace("-", "_").replace(".", "_")  # convert to valid need_id
        item = NeedItem(id=title, content=row["Content"], status=row["Status"])
        match title:
            case title if "REQ" in title:
                current_req = title
                requirements.append(asdict(item))
            case title if "SPEC" in title:
                current_sepc = title
                item.links = current_req
                specification.append(asdict(item))
            case title if "TEST" in title:
                item.links = current_sepc
                tests.append(asdict(item))

    app.config["html_context"] = {
        "requirements": requirements,
        "specifications": specification,
        "tests": tests,
    }


def rstjinja(app: Sphinx, docname: str, source: list[str]):

    # Make sure we're outputting HTML
    if app.builder.format != "html":
        return
    src = source[0]
    rendered = app.builder.templates.render_string(src, app.config.html_context)
    source[0] = rendered


def setup(app: Sphinx):
    app.connect("env-before-read-docs", csv_import)
    app.connect("source-read", rstjinja)
