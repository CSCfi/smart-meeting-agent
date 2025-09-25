# Smart Meeting Agent

Convert meeting audio to text and build downstream text processing (e.g., summarization).

- 💾 **Repo:** https://github.com/CSCfi/smart-meeting-agent

```bash
# Build docs locally (optional)
python3 -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
make -C docs html
open docs/_build/html/index.html

```````
:maxdepth: 2
:hidden:

usage
api
devnotes
```````


Notes:
- The `{toctree}` part **must be inside** a fenced code block starting with ```` ```{toctree} ```` and ending with ```` ``` ````.
- The last three bullet links are optional. If you don’t want them, delete those lines.  
- If you remove `:hidden:`, Sphinx will show the toctree on the page and you won’t need the manual links.
