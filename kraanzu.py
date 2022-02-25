from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🤓 Murli Tawari", guide_style="bold cyan")
python_tree = tree.add("🐍 Python dev", guide_style="green")
python_tree.add("💬 [link=https://github.com/kraanzu/gupshup]Gupshup")
python_tree.add("💻 [link=https://github.com/kraanzu/termtyper]Termtyper")

competitive_tree = tree.add("🔧 Competitive Programmer")
competitive_tree.add("⭐ [link=https://codeforces.com/profile/easedeath]Codeforces")
competitive_tree.add("⭐ [link=https://leetcode.com/easedeath/]Leetcode")

about = """\
I'm a sophomore pursuring BTECH-CSE. I love trying out new technologies.
I am currently developing different applications with [link=https://www.python.org/]Python[/] and I am learning [link=https://www.rust-lang.org/]Rust[/] and [link=https://www.typescriptlang.org/]Typescript[/].
Oh and, I use Arch btw
"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi there", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
