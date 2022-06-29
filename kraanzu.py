from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🤓 Murli Tawari", guide_style="bold cyan")
python_tree = tree.add("🐍 Python dev", guide_style="green")
python_tree.add("🗒️ [link=https://github.com/kraanzu/dooit]Dooit")
python_tree.add("💬 [link=https://github.com/kraanzu/gupshup]Gupshup")
python_tree.add("💻 [link=https://github.com/kraanzu/termtyper]Termtyper")

competitive_tree = tree.add("🔧 Sport Programmer")
competitive_tree.add("⭐ [link=https://codeforces.com/profile/kraanzu]Codeforces")
competitive_tree.add("⭐ [link=https://leetcode.com/kraanzu/]Leetcode")

about = """\
I'm a sophomore pursuring bachelors in Computer Science.
I love sport programming and tinkering with different techs.

I'm currently making TUI applications with [link=https://www.python.org/]Python[/] and will expand this to other languages as well
Oh and, I use Arch btw ;) \
"""

panel = Panel.fit(
    about,
    box=box.DOUBLE,
    border_style="green",
    title="[b]Hi there fellas!",
    width=60,
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
