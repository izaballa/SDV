FROM python:3.12-slim-bookworm

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY z_fleet_connector.py ./

CMD [ "python", "-u", "./z_fleet_connector.py" ]
