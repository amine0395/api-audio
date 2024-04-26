# SNRT RESTful API

Welcome to the SNRT RESTful API!

## Introduction

This RESTful API provides access to audio data and information stored in the SNRT database. It allows users to retrieve fingerprint and waveform data, as well as information about audio titles.

## Getting Started

To get started with using the SNRT API, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python and Flask installed on your system.
3. Install the required Python dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
4. Start the Flask server by running:
    ```bash
    python app.py
    ```
5. The API will now be accessible at `http://localhost:5000`.

## Endpoints

### 1. Welcome Endpoint

- **URL:** `/`
- **Method:** `GET`
- **Description:** Provides a welcome message to indicate that the API is up and running.

### 2. Fingerprint Data Endpoint

- **URL:** `/fingerprint/<id>`
- **Method:** `GET`
- **Description:** Retrieves fingerprint data for a given audio title ID.

### 3. Waveform Data Endpoint

- **URL:** `/waveform/<id>`
- **Method:** `GET`
- **Description:** Retrieves waveform data for a given audio title ID.

### 4. Information Endpoint

- **URL:** `/info/<id>`
- **Method:** `GET`
- **Description:** Retrieves detailed information about an audio title based on its ID.

### 5. All Data Endpoint

- **URL:** `/all`
- **Method:** `GET`
- **Description:** Retrieves all data stored in the SNRT database.

## Dependencies

- Flask: Web framework for building the API.
- PyMongo: Python driver for MongoDB.
- GridFS: MongoDB specification for storing large files.

## Usage

To use the API, send HTTP requests to the appropriate endpoints with the required parameters. For example:

- To retrieve fingerprint data:

  GET /fingerprint/id

- To retrieve waveform data:

  GET /waveform/id

- To retrieve information about an audio title:

  GET /info/id

- To retrieve all data:

  Get /all


