# Python CLI Monitor

A little CLI tool written in Python that can be told to take screenshots at regular intervals for a set duration and save them into a specified folder.
I've found something like this useful for setting jobs/downloads before heading to bed and wanting to see a history of how things progressed the next morning.
The code in this repo is a quick effort to formalize the tool a bit and make it nicer to use.

## Usage

```console
> python monitor.py -h
usage: monitor.py [-h] [-H [DURATION_HOURS]] [-m [DURATION_MINUTES]] [-s [DURATION_SECONDS]] [-o [OUTPUT_DIR]] interval_millis

positional arguments:
  interval_millis       Interval in milliseconds to take screenshots. Must be >= 100.

optional arguments:
  -h, --help            show this help message and exit
  -H [DURATION_HOURS], --duration_hours [DURATION_HOURS]
                        The duration in hours to run the monitor. Will be summed with other durations, if specified.
  -m [DURATION_MINUTES], --duration_minutes [DURATION_MINUTES]
                        The duration in minutes to run the monitor. Will be summed with other durations, if specified.
  -s [DURATION_SECONDS], --duration_seconds [DURATION_SECONDS]
                        The duration in seconds to run the monitor. Will be summed with other durations, if specified.
  -o [OUTPUT_DIR], --output_dir [OUTPUT_DIR]
                        Output directory to save screenshots.
```

Note that the durations can be specified as decimals e.g. 4.5 minutes to get 4 minutes and 30 seconds.

Note also that, as a safety, the tool prevents intervals less than 100 millis. This is mainly to protect the user from wrongfully thinking the interval is specified in seconds and flooding their directory with screenshots.

```console
> python monitor.py 2
2022-02-13 13:48:16.974 monitor ERROR: Safety triggered: interval is in milliseconds (not seconds), rejecting input (2) < 100ms. Quitting...
```

### Examples

*Below output may not reflect output of latest version.*

Take a screenshot every 5 seconds indefinitely into my current directory.

```console
> python monitor.py 5000
2022-02-13 13:35:34.758 monitor INFO: No duration specified, running monitor until stopped...
2022-02-13 13:35:34.814 monitor INFO: Saving screenshot to ./20220213-133534-814.png
2022-02-13 13:35:39.993 monitor INFO: Saving screenshot to ./20220213-133539-993.png
... <truncated>
```

Take a screenshot every 2 seconds indefinitely into a subdirectory 'test'.

```console
> python monitor.py 2000 -o ./test
2022-02-13 13:38:01.246 monitor INFO: No duration specified, running monitor until stopped...
2022-02-13 13:38:01.323 monitor INFO: Saving screenshot to ./test/20220213-133801-323.png
2022-02-13 13:38:03.528 monitor INFO: Saving screenshot to ./test/20220213-133803-528.png
... <truncated>
```

Take a screenshot every 2 seconds for the next 4 hours into a subdirectory 'test'.

```console
> python monitor.py 2000 -o ./test -H 4
2022-02-13 13:39:04.319 monitor INFO: Running monitor for 4:00:00 (hh:mm:ss). Estimated time of completion: 2022-02-13 17:39:04.319
2022-02-13 13:39:04.394 monitor INFO: Saving screenshot to ./test/20220213-133904-394.png
2022-02-13 13:39:06.615 monitor INFO: Saving screenshot to ./test/20220213-133906-615.png
... <truncated>
```

Take a screenshot every 2.5 seconds for 4 minutes and 30 seconds into my current directory.

```console
> python monitor.py 2500 -m 4.5
2022-02-13 13:40:41.328 monitor INFO: Running monitor for 0:04:30 (hh:mm:ss). Estimated time of completion: 2022-02-13 13:45:11.328
2022-02-13 13:40:41.398 monitor INFO: Saving screenshot to ./20220213-134041-398.png
2022-02-13 13:40:44.124 monitor INFO: Saving screenshot to ./20220213-134044-124.png
... <truncated>
```

Take a screenshot every 500 millis for 1 minute and 2 seconds into my current directory.

```console
> python monitor.py 500 -m 1 -s 2
2022-02-13 13:45:00.667 monitor INFO: Running monitor for 0:01:02 (hh:mm:ss). Estimated time of completion: 2022-02-13 13:46:02.667
2022-02-13 13:45:00.724 monitor INFO: Saving screenshot to ./20220213-134500-724.png
2022-02-13 13:45:01.442 monitor INFO: Saving screenshot to ./20220213-134501-442.png
... <truncated>
```
