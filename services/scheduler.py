import sched, time, requests
from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)
from font_fredoka_one import FredokaOne
from PIL import Image, ImageFont, ImageDraw
from yr.libyr import Yr
import json
import logging

s = sched.scheduler(time.time, time.sleep)
logger = logging.getLogger(__name__)


def e_paper_content_producer(sc):
    # Ruter data:
    try:
        r = requests.get('http://0.0.0.0:4000/6369?direction=inbound')

        # Yr data Oslo:
        weather = Yr(location_name='Norge/Oslo/Oslo/Oslo')
        now = weather.now(as_json=True)
        weather_metrics = json.loads(now)

        # Yr data Skeikampen:
        skei_weather = Yr(location_name='/Norge/Innlandet/Gausdal/Skeikampen')
        now = skei_weather.now(as_json=True)
        skei_metrics = json.loads(now)

        # Pihole metrics:
        pihole_api = requests.get('http://192.168.0.17/admin/api.php/stats/summary')
        pihole_metrics = pihole_api.json()

    except ConnectionError:
        logger.error('api not running')

    # Content producer:
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FredokaOne, 12)
    a = r.text.split('\n')
    try:
        message = a[0] + '\n' + a[1] + '\n' + 'Status: ' + pihole_metrics.get('status') + 'Running on: ' + str(
            pihole_metrics.get('unique_clients')) + ' clients' + '\n' + 'Weather: ' + weather_metrics.get('symbol').get(
            '@name') + ' temp: ' + weather_metrics.get('temperature').get(
            '@value') + '\n' + 'Skei: ' + skei_metrics.get('symbol').get('@name') + ' ' + skei_metrics.get(
            'temperature').get('@value')

    except ValueError:
        logger.error('missing parameters from api calls')
        message = 'Missing data from api'

    w, h = font.getsize(message)
    x = 0  # (inky_display.WIDTH / 2) - (w / 2)
    y = 0  # (inky_display.HEIGHT / 2) - (h / 2)
    draw.text((x, y), message, inky_display.BLACK, font)
    inky_display.set_image(img)
    inky_display.show()

    s.enter(30, 1, e_paper_content_producer, (sc,))


s.enter(30, 1, e_paper_content_producer, (s,))
s.run()
