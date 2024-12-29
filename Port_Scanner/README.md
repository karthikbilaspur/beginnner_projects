# Port Scanner

A multi-threaded port scanner tool.

## Features

1. Scans TCP ports
2. Identifies open ports and services
3. Saves results to JSON file
4. Verbose mode for detailed output
5. Timestamped results

## Requirements

See [requirements.txt](requirements.txt)

## Installation

1. Clone repository.
2. Install requirements: `pip install -r requirements.txt`
3. Run: `python port_scanner.py`

## Usage

`python port_scanner.py -t <target> -p <port_range> [-s] [-v]`

## Options

* `-t`, `--target`: Target IP or hostname
* `-p`, `--ports`: Port range (e.g., 1-1024)
* `-s`, `--save`: Save results to file
* `-v`, `--verbose`: Increase verbosity

## Examples

* `python port_scanner.py -t example.com -p 1-1024`
* `python port_scanner.py -t 192.168.1.1 -p 1-1024 -s -v`

## Security Considerations

1. Use responsibly.
2. Avoid scanning unauthorized targets.
3. Comply with local laws.