#!/usr/bin/python3
""" Module for log parsing """

import sys
import signal
from typing import List

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_count = {code: 0 for code in status_codes}
total_file_size = 0
line_count = 0

def print_stats():
    """Print the current statistics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_count.keys()):
            print(f"{code}: {status_count[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)"""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def reader():
    """Reader function to process log lines from stdin"""
    global total_file_size, line_count

    try:
      for line in sys.stdin:
          parts = line.strip().split()
          
          if len(parts) < 7:
              continue
          
          ip = parts[0]
          date = parts[1].strip('[]')
          method = parts[2].strip('"')
          url = parts[3]
          protocol = parts[4].strip('"')
          status = parts[5]
          size = parts[6]

          if method != "GET" or url != "/projects/260" or protocol != "HTTP/1.1":
              continue

          try:
              status = int(status)
              size = int(size)
          except ValueError:
              continue

          if status in status_codes:
              status_count[status] += 1
              total_file_size += size

          line_count += 1

          if line_count % 10 == 0:
              print_stats()
    
    except BrokenPipeError:
        try:
            sys.stderr.close()
        except Exception:
            pass
        finally:
            sys.exit(0)

if __name__ == "__main__":
    reader()