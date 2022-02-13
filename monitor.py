from argparse import ArgumentParser
from pyautogui import screenshot
import logging
from datetime import timedelta, datetime
from time import sleep, time

NO_TIME = timedelta(0)

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(module)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

arg_parser = ArgumentParser()

arg_parser.add_argument(
    "interval_millis",
    type=int,
    help="Interval in milliseconds to take screenshots. Must be >= 100.",
)
arg_parser.add_argument(
    "-H",
    "--duration_hours",
    dest="duration_hours",
    nargs="?",
    type=float,
    help="The duration in hours to run the monitor. Will be summed with other durations, if specified.",
    default=0,
)
arg_parser.add_argument(
    "-m",
    "--duration_minutes",
    dest="duration_minutes",
    nargs="?",
    type=float,
    help="The duration in minutes to run the monitor. Will be summed with other durations, if specified.",
    default=0,
)
arg_parser.add_argument(
    "-s",
    "--duration_seconds",
    dest="duration_seconds",
    nargs="?",
    type=float,
    help="The duration in seconds to run the monitor. Will be summed with other durations, if specified.",
    default=0,
)
arg_parser.add_argument(
    "-o",
    "--output_dir",
    dest="output_dir",
    nargs="?",
    type=str,
    help="Output directory to save screenshots.",
    default=".",
)

args = arg_parser.parse_args()

LOGGER.debug("Arguments: %s", args)

interval_millis: int = args.interval_millis
if interval_millis < 100:
    LOGGER.error(
        f"Safety triggered: interval is in milliseconds (not seconds), rejecting input ({interval_millis}) < 100ms. Quitting..."
    )
    exit(1)
interval_seconds = interval_millis / 1000

hours: timedelta = timedelta(hours=args.duration_hours)
minutes: timedelta = timedelta(minutes=args.duration_minutes)
seconds: timedelta = timedelta(seconds=args.duration_seconds)

duration_sum: timedelta = hours + minutes + seconds

stop_time = time() + duration_sum.total_seconds()
if duration_sum == NO_TIME:
    LOGGER.info("No duration specified, running monitor until stopped...")
else:
    LOGGER.info(
        f"Running monitor for {duration_sum} (hh:mm:ss). Estimated time of completion: {datetime.fromtimestamp(stop_time).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}"
    )
while True:
    snapshot = screenshot()
    save_path = (
        f"{args.output_dir}/{datetime.now().strftime('%Y%m%d-%H%M%S-%f')[:-3]}.png"
    )
    LOGGER.info("Saving screenshot to %s", save_path)
    snapshot.save(save_path)

    if duration_sum != NO_TIME and (time() + interval_seconds) > stop_time:
        break

    sleep(interval_seconds)

LOGGER.info("Monitoring finished.")
