from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from data import CUPS

ROOT_PATH = Path(__file__).parent.absolute()
TEMPLATE_ENVIRONMENT = Environment(loader=FileSystemLoader(ROOT_PATH / 'data'))



def render() -> str:
    """
        Renders the full HTML page with all MKT favored/favorite courses.
    """

    template = TEMPLATE_ENVIRONMENT.get_template('index.html')
    return template.render(CUPS=CUPS)



if __name__ == '__main__':
    with open(ROOT_PATH / 'docs' / 'index.html', 'w') as render_file:
        render_file.write(render())

    print('Rendered!')
