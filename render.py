from pathlib import Path
from jinja2 import Environment, FileSystemLoader, StrictUndefined

from data.models import Driver
from data import TOURS

ROOT_PATH = Path(__file__).parent.absolute()
TEMPLATE_ENVIRONMENT = Environment(loader=FileSystemLoader(ROOT_PATH / 'data'), undefined=StrictUndefined)



def most_favored_driver() -> Driver:
    """
        Returns the most favored driver.
    """

    counts = {}

    for tour in TOURS:
        for cups in tour.cups:
            for course in cups.courses:
                for driver in course.three_item_slot_drivers:
                    try:
                        counts[driver.name] += 1

                    except KeyError:
                        counts[driver.name] = 1
    
    return max(counts, key=counts.get)



def render() -> str:
    """
        Renders the full HTML page with all MKT favored/favorite courses.
    """

    template = TEMPLATE_ENVIRONMENT.get_template('index.html')
    return template.render(TOURS=TOURS, most_favored_driver=most_favored_driver())



if __name__ == '__main__':
    with open(ROOT_PATH / 'docs' / 'index.html', 'w') as render_file:
        render_file.write(render())

    print('Rendered!')
