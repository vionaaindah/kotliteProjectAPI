<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/SVeeIS/kotliteProjectAPI">
    <img src="assets/kotlite_logo.png" alt="kotliteLogo" height="150">
  </a>

  <p align="center">
    <img src="https://img.shields.io/badge/Team-Brillante-9e83fc">
    <img src="https://img.shields.io/badge/ID-BA21_CAP0176-9e83fc?">
  </p>

  <h3 align="center">Kotlite (Angkot Elite) REST-API</h3>

  <p align="center">
    A Part of Kotlite Ridesharing Application
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the Projects »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/github_username/repo_name">View Demo</a>
    · -->
    <a href="https://github.com/SVeeIS/kotliteProjectAPI/issues">Report Bug</a>
    ·
    <a href="https://github.com/SVeeIS/kotliteProjectAPI/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

<!-- Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo_name`, `twitter_handle`, `email`, `project_title`, `project_description` -->

Kotlite is here as a breakthrough idea that answers the need of users to find drivers or passengers from and going to the same routes. It is designed to optimistically accelerate the transformation of the citizens' lifestyle to rideshare and network, eliminating incurable rush hour traffic and provide practicality for user's mobility from one place to another.

<!-- ini bagian teknisnya -->

### Built With

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Tensorflow](https://www.tensorflow.org/)
- [JSON Web Token](https://jwt.io/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and run, follow these simple steps.

### Prerequisites

This project requires several resources to be prepared and installed on the local computer, including:

- [Python ver 3.5.x - 3.8.x](https://www.python.org/downloads/) (we use python version 3.8.5)
- [Google Maps API Key](https://developers.google.com/maps)

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/SVeeIS/kotliteProjectAPI.git
   cd kotliteProjectAPI
   ```
2. Install the required environment with virtualenv **(recommendation)**

   - Linux/macOs
     ```sh
     virtualenv env
     source env/bin/activate
     pip install -r requirements.txt
     ```
   - Windows
     ```sh
     python -m venv env
     env\scripts\activate
     pip install -r requirements.txt
     ```

3. Setup the database configuration in `KotliteProjectAPI/settings.py`

   If you want to run a local server then uncomment this part of the `settings.py`

   ```python
   # UNCOMMENT THIS CODE FOR LOCAL TESTING
   # Use a in-memory sqlite3 database when testing in CI systems
   # DATABASES = {
   #     'default': {
   #         'ENGINE': 'django.db.backends.sqlite3',
   #         'NAME': BASE_DIR / 'db.sqlite3',
   #     }
   # }
   ```

   to be like this

   ```python
   # UNCOMMENT THIS CODE FOR LOCAL TESTING
   # Use a in-memory sqlite3 database when testing in CI systems
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

4. Setup Google Maps Client in `maps_env.py`

   open file `maps_env.py`, and change `[YOUR API KEY]` with your API Key.

5. Migrate the model to create databases

   ```sh
   python manage.py makemigrations
   python manage.py makemigrations drivers
   python manage.py makemigrations passengers
   python manage.py makemigrations users
   python manage.py migrate
   ```

6. Create a super user account. **You need to define a username and password**

   ```sh
   python manage.py createsuperuser
   ```

7. Start on the local webserver

   ```sh
   python manage.py runserver
   ```

   Now, your local webserver is running in `http://localhost:8000/`. You can also open the Django admin site in `http://localhost:8000/kotliteadm` and log in using the superuser account.

<!-- USAGE EXAMPLES -->

## Usage

Our Rest API is the way for computer systems to communicate over HTTP in a similar way to web browsers and servers. We share databases between systems to enable our application, working effectively for our users.

_For more usage, please refer to the [Documentation](https://example.com)_.

<!-- CONTRIBUTING -->

## Deployment

Deployment REST API to Google Cloud Platform so that it can be accessed by android apps. We deploy using compute engine, but we also have various options how to deployment

1. Deployment using Google [Compute Engine](https://github.com/SVeeIS/kotliteProjectAPI/blob/master/GCE.md)
2. Deployment using Google [Compute Engine with port 8000](https://github.com/SVeeIS/kotliteProjectAPI/blob/master/GCE%20with%20port%208000.md)
3. Deployment with Google [App Engine Standard](https://github.com/SVeeIS/kotliteProjectAPI/blob/master/GAE.md)

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<!-- CONTACT -->

## Contact

How can we help you? While we're occupied for the Capstone Project, there are simpler ways for us to get in touch! Please do visit us at

<!-- Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name) -->

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Bangkit Academy 2021]()
- []()
- []()

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/SVeeIS/kotliteProjectAPI.svg?style=flat
[contributors-url]: https://github.com/SVeeIS/kotliteProjectAPI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SVeeIS/kotliteProjectAPI.svg?style=flat
[forks-url]: https://github.com/SVeeIS/kotliteProjectAPI/network/members
[issues-shield]: https://img.shields.io/github/issues/SVeeIS/kotliteProjectAPI.svg?style=flat
[issues-url]: https://github.com/SVeeIS/kotliteProjectAPI/issues
[license-shield]: https://img.shields.io/github/license/SVeeIS/kotliteProjectAPI.svg?style=flat
[license-url]: https://github.com/SVeeIS/kotliteProjectAPI/blob/master/LICENSE.md

<!-- https://github.com/SVeeIS/kotliteProjectAPI -->
