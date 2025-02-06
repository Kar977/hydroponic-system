# Hydroponic System Management App

An application for managing a hydroponic system, allowing remote control and monitoring of various hydroponic systems. The app provides an API that enables managing systems and adding sensor readings, such as water temperature, tds and pH.

## Features

- **Hydroponic system management**: Create, edit, and delete systems.
- **Sensor monitoring**: Readings from sensors such as temperature, humidity, pH, and water level.
- **API**: Integration with the system through an API that allows:
  - Adding sensor readings.
  - Updating hydroponic system settings.

## Setup

1. Clone the repository:
   ```git clone https://github.com/Kar977/hydroponic-system.git```

2. Change to the project directory:
   ```cd hydroponic```
   
3. Build and run the application with Docker-Compose:
   ```docker-compose up --build```

## Technologies
<ul>
<li>Python 3.11</li>
<li>Django 5.1.5</li>
<li>PostgreSQL 15</li>
<li>Django REST Framework 3.15.2</li>
<li>Docker 24.0.7</li>
<li>drf-yasg 1.21.8 (Yet another Swagger generator)</li>
</ul>
