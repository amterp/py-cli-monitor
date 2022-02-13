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
2022-02-13 13:48:16.973 DEBUG monitor <module>:: Arguments: Namespace(interval_millis=2, duration_hours=0, duration_minutes=0, duration_seconds=0, output_dir='.')
2022-02-13 13:48:16.974 ERROR monitor <module>:: Safety triggered: interval is in milliseconds (not seconds), rejecting input (2) < 100ms. Quitting...
```

### Examples

*Below output may not reflect output of latest version.*

Take a screenshot every 5 seconds indefinitely into my current directory.

```console
> python monitor.py 5000
2022-02-13 13:35:34.757 DEBUG monitor <module>:: Arguments: Namespace(interval_millis=5000, duration_hours=0, duration_minutes=0, duration_seconds=0, output_dir='.')
2022-02-13 13:35:34.758 INFO monitor <module>:: No duration specified, running monitor until stopped...
2022-02-13 13:35:34.814 INFO monitor <module>:: Saving screenshot to ./20220213-133534-814.png
2022-02-13 13:35:39.993 INFO monitor <module>:: Saving screenshot to ./20220213-133539-993.png
... <truncated>
```

Take a screenshot every 2 seconds indefinitely into a subdirectory 'test'.

```console
> python monitor.py 2000 -o ./test
2022-02-13 13:38:01.246 DEBUG monitor <module>:: Arguments: Namespace(interval_millis=2000, duration_hours=0, duration_minutes=0, duration_seconds=0, output_dir='./test')
2022-02-13 13:38:01.246 INFO monitor <module>:: No duration specified, running monitor until stopped...
2022-02-13 13:38:01.323 INFO monitor <module>:: Saving screenshot to ./test/20220213-133801-323.png
2022-02-13 13:38:03.528 INFO monitor <module>:: Saving screenshot to ./test/20220213-133803-528.png
... <truncated>
```

Take a screenshot every 2 seconds for the next 4 hours into a subdirectory 'test'.

```console
> python monitor.py 2000 -o ./test -H 4
2022-02-13 13:39:04.319 DEBUG monitor <module>:: Arguments: Namespace(interval_millis=2000, duration_hours=4.0, duration_minutes=0, duration_seconds=0, output_dir='./test')
2022-02-13 13:39:04.319 INFO monitor <module>:: Running monitor for 4:00:00 (hh:mm:ss). Estimated time of completion: 2022-02-13 17:39:04.319
2022-02-13 13:39:04.394 INFO monitor <module>:: Saving screenshot to ./test/20220213-133904-394.png
2022-02-13 13:39:06.615 INFO monitor <module>:: Saving screenshot to ./test/20220213-133906-615.png
... <truncated>
```

Take a screenshot every 2.5 seconds for 4 minutes and 30 seconds into my current directory.

```console
> python monitor.py 2500 -m 4.5
2022-02-13 13:40:41.328 DEBUG monitor <module>:: Arguments: Namespace(interval_millis=2500, duration_hours=0, duration_minutes=4.5, duration_seconds=0, output_dir='.')
2022-02-13 13:40:41.328 INFO monitor <module>:: Running monitor for 0:04:30 (hh:mm:ss). Estimated time of completion: 2022-02-13 13:45:11.328
2022-02-13 13:40:41.398 INFO monitor <module>:: Saving screenshot to ./20220213-134041-398.png
2022-02-13 13:40:44.124 INFO monitor <module>:: Saving screenshot to ./20220213-134044-124.png
... <truncated>
```

Take a screenshot every 500 millis for 1 minute and 2 seconds into my current directory.

```console
> python monitor.py 500 -m 1 -s 2
2022-02-13 13:45:00.667 DEBUG monitor <module>:: Arguments: Namespace(interval_millis=500, duration_hours=0, duration_minutes=1.0, duration_seconds=2.0, output_dir='.')
2022-02-13 13:45:00.667 INFO monitor <module>:: Running monitor for 0:01:02 (hh:mm:ss). Estimated time of completion: 2022-02-13 13:46:02.667
2022-02-13 13:45:00.724 INFO monitor <module>:: Saving screenshot to ./20220213-134500-724.png
2022-02-13 13:45:01.442 INFO monitor <module>:: Saving screenshot to ./20220213-134501-442.png
... <truncated>
```
