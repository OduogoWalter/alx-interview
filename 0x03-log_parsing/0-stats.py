#!/usr/bin/python3
import sys
import signal
import re


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


# Function to print statistics
def print_statistics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


# Regular expressions to match required log format
log_pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
)

status_codes = {}
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        result = log_pattern.search(line)
        if result:
            status_code = int(result.group(2))
            file_size = int(result.group(3))

            # Update the total file size
            total_file_size += file_size

            # Count the occurrences of status codes
            if status_code in status_codes:
                status_codes[status_codes] += 1
            else:
                status_codes[status_code] = 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    raise

except Exception as e:
    print(f"An error occurred: {e}")

# Ensure statistics are printed at the end if not already printed
if line_count % 10 != 0:
    print_statistics()
