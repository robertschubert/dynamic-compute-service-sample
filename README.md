# Introduction
This sample is there to show how a Dockerfile needs to be structured to be able to run the dynamic-container-job pipeline in the [Gaia-X 4 Future Mobility / PLC-AAD project](https://www.gaia-x4plcaad.info/). This `Dockerfile` uses a simple python script that reads a file from the mounted volume and writes the result to another file. 

# Prerequisites
Docker installation or Docker daemon running or podman installed.

# Usage
## Python script 
- The python script `copy_file.py` is located in the `src` directory. It counts files from the mounted input volume and writes the result to another file located in the output volume.
- The script expects the input data in `/data/input`.
- The script writes the result to `/data/output`.

## Docker
### Docker build
`docker build -t dynamic-container-job-sample:1.0.0 .`

### Docker run
`docker run -v "/path/to/your/input-dir:/data/input" -v "/path/to/your/output-dir:/data/output" dynamic-container-job-sample:1.0.0`

## Docker-compose
### Docker-compose build
`docker-compose build`

### Docker-compose run
`docker-compose up -d`

### Docker-compose down
`docker-compose down`

> Note: Replace `/path/to/your/input-dir` and `/path/to/your/output-dir` with the paths to your input and output directories. 

> Note: You need to pass an absolute path to the directories. If running on windows make sure to use the correct path format (c:\path\to\your\input-dir).
 
