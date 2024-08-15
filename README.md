![Main LOGO](xemijobs/assets/imgs/banner1.webp)

# Victor Garcia Cantalapidera 
-Slack:[@Victor Garcia](https://code-institute-room.slack.com/team/U0695HZA7FZ)

-GitHub: [Vgarcan](https://github.com/Vgarcan)

-LinkedIn: [Victor Garcia](https://www.linkedin.com/in/vgc89/)

## Check us out!

[XemiJobs - Heroku](https://xemijobs-616b41a185c0.herokuapp.com/) 


---

### Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Development Tools](#development-tools)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
  - [CSS Management for Project Structure](#css-management-for-project-structure)
- [Wireframes](#wireframes)
- [Colors](#colors)
  - [Color Customization Process](#color-customization-process)
  - [User-Friendly Approach](#user-friendly-approach)
- [User Experience](#user-experience)
  - [Key Principles](#key-principles)
  - [User Stories](#user-stories)
  - [Customization and Flexibility](#customization-and-flexibility)
  - [Future Enhancements](#future-enhancements)
- [Testing](#testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Accessibility](#accessibility)
  - [Wave Validation](#wave-validation)
  - [Lighthouse Validation](#lighthouse-validation)
  - [JSHint Validation](#jshint-validation)
  - [Device Testing](#device-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [User Stories Testing](#user-stories-testing)
- [Collaborative Efforts](#collaborative-efforts)
- [Current State and Future Plans](#current-state-and-future-plans)
  - [Current State](#current-state)
  - [Future Plans](#future-plans)
- [Deployment](#deployment)
- [License](#license)
- [Bugs and Challenges](#bugs-and-challenges)
- [Acknowledgement](#acknowledgement)

---

### Introduction

XemiJobs is a job search platform designed to connect employers with potential candidates. This project was born out of my frequent personal use of job search websites, which sparked the idea to create a platform that could facilitate the hiring process more efficiently. The website allows companies to post job vacancies and manage applications, while job seekers can browse listings, apply for jobs, and manage their applications—all from a desktop interface.

The concept for XemiJobs emerged from my own experiences and the desire to build something that could help others in similar situations. I saw this as a great opportunity to deepen my understanding of web development and to create a functional tool that serves a real purpose. The goal of this project is simple: to create a platform that bridges the gap between job seekers and employers, making it easier for them to connect and communicate.

I'm incredibly proud of how this project has developed and hope it can serve as a useful resource for anyone involved in the job search or hiring process.

---


### Features

- **User Registration and Authentication:** Secure registration and login for job seekers and employers, with role-based access control to ensure users see only what they need.
- **Job Listings Management:** Employers can create, update, and delete job listings. The listings are displayed dynamically on the platform, allowing job seekers to browse through the latest opportunities.
- **Application Management:** Job seekers can apply for jobs directly through the platform, track the status of their applications, and receive updates as they progress through the hiring process.
- **Dynamic Dashboard for Employers:** The company dashboard provides a real-time overview of key metrics, such as the number of job postings, applications received, and interviews scheduled, helping employers manage their recruitment process effectively.
- **Real-Time Job Count:** The platform features a hero section that displays the current number of job listings, updated in real-time, offering users an up-to-date view of available opportunities.
- **Advanced Search and Filters:** Job seekers can search for positions based on various criteria like job title, location, and company, with results being dynamically updated.

---

### Development Tools

- **Custom Jinja Widgets:** A collection of reusable Jinja widgets has been created to streamline the development process. These widgets automatically adapt to the type of data being passed, ensuring a consistent aesthetic across the entire platform. This approach not only speeds up development but also maintains a high level of visual and functional uniformity throughout the site.
- **Modular Design:** The platform is built using a modular architecture in Flask, which allows for easy extension and maintenance. Each module is self-contained, facilitating rapid development and testing of individual components without affecting the entire application.
- **Consistent Aesthetic:** By leveraging these custom widgets, the design remains consistent, providing a unified look and feel across all pages and components, which enhances the overall user experience.

---

### Technologies Used

#### Backend
- <img src="xemijobs/static/imgs/readme-pics/flask-icon.ico" width="18px"> **Flask:** The core framework for the backend of the application, used for handling routing, sessions, and integrating with the database.
- <img src="xemijobs/static/imgs/readme-pics/flask-login-icon.ico" width="18px"> **Flask-Login:** Employed to manage user sessions and authentication, ensuring secure access control throughout the platform.
- <img src="xemijobs/static/imgs/readme-pics/flask-pymongo-icon.ico" width="18px"> **Flask-PyMongo:** Utilized for integrating Flask with MongoDB, facilitating database operations directly from the Flask application.

#### Database
- <img src="xemijobs/static/imgs/readme-pics/mongodb-icon.ico" width="18px"> **MongoDB:** The primary database used to store user data, job listings, and application details, chosen for its flexibility and scalability.

#### Frontend
- <img src="xemijobs/static/imgs/readme-pics/html_icon.ico" width="18px"> **HTML:** The foundation for structuring the web pages, providing the semantic markup needed for the site's content.
- <img src="xemijobs/static/imgs/readme-pics/css-icon.ico" width="18px"> **CSS:** Applied to style and layout the web pages, ensuring a consistent and visually appealing user interface across the application.
- <img src="xemijobs/static/imgs/readme-pics/js-icon.ico" width="18px"> **JavaScript:** Employed to add interactivity and dynamic elements to the site, enhancing the user experience with features like form validation and asynchronous content updates.
- <img src="xemijobs/static/imgs/readme-pics/bootstrap-icon.ico" width="18px"> **Bootstrap:** Integrated to utilize its responsive grid system and pre-built components, ensuring the site is mobile-friendly and adaptable to different screen sizes.


---

### Project Structure

- <img src="xemijobs/static/imgs/readme-pics/red-folder-icon.ico" width="18px"> **Root Directory**
    
    - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **xemijobs/** (Main application folder)

        - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py`
        - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `extensions.py`
        - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `decorators.py`
        
        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **static/** (Static assets like images, CSS, and JS files)
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **css/** (Contains CSS stylesheets)
                - <img src="xemijobs/static/imgs/readme-pics/css-filetype-icon.ico" width="18px"> `main.css`
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **imgs/** (Contains images)
                - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **comp-pics/** (Company images)
                    - <img src="xemijobs/static/imgs/readme-pics/image-con.ico" width="18px"> `comp-1.webp`
                    - <img src="xemijobs/static/imgs/readme-pics/image-con.ico" width="18px"> `comp-2.webp`
                    - <img src="xemijobs/static/imgs/readme-pics/image-con.ico" width="18px"> `comp-3.webp`
                    - <p>...</p>
                - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **testimonials/** (Testimonial images)
                    - <img src="xemijobs/static/imgs/readme-pics/image-con.ico" width="18px"> `user1.webp`
                    - <img src="xemijobs/static/imgs/readme-pics/image-con.ico" width="18px"> `user2.webp`
                    - <p>...</p>
                - <img src="xemijobs/static/imgs/readme-pics/image-con.ico" width="18px"> `banner1.webp`
                - <p>...</p>
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **js/** (Contains JavaScript files)
                - <img src="xemijobs/static/imgs/readme-pics/js-filetype-icon.ico" width="18px"> `main.js`
            - <img src="xemijobs/static/favicon.ico" width="18px"> `favicon.ico`

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/** (Main templates directory)
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **widgets/** (Reusable widgets for the application)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `alert.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `cards.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `carousel.html`
                - <p>...</p>
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **xemijobs/** (Core templates for the application)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `base.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `temp-sheet.html`

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **users/** (Handles user-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py`
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/users/** (HTML templates for user-related views)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `dashboard.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `profile.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `login.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `register.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `show-user.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `user-list.html`

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **companies/** (Handles company-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py`
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/companies/** (HTML templates for company-related views)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `dashboard.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `adv-dash.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `profile.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `login.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `register.html`

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **applications/** (Handles applications-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py`
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/applications/** (HTML templates for application-related views)
                
        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **main/** (Handles main-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py`
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/main/** (HTML templates for main-related views)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `temp-sheet.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `index.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `widgets-collection.html`

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **jobs/** (Handles job-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py`
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py`
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/jobs/** (HTML templates for job-related views)
              - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `create-job.html`
              - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `job-list.html`
              - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `view-job.html`

    - <img src="xemijobs/static/imgs/readme-pics/git-icon.ico" width="18px"> `.gitignore`
    - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `config.py`
    - <img src="xemijobs/static/imgs/readme-pics/ic-info-outline.ico" width="18px"> `README.md`
    - <img src="xemijobs/static/imgs/readme-pics/procfile-filetipe-icon.ico" width="18px"> `Procfile`
    - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `run.py`
    - <img src="xemijobs/static/imgs/readme-pics/txt-filetype-icon.ico" width="18px"> `requirements.txt`
    - <img src="xemijobs/static/imgs/readme-pics/txt-filetype-icon.ico" width="18px"> `runtime.txt`

#### CSS Management for Project Structure

[Not ready yet]

---

### Wireframes

[Not ready yet]

---

### Colors

#### Color Customization Process

[Not ready yet]

#### User-Friendly Approach

[Not ready yet]

---

### User Experience

#### Key Principles

- **Intuitive Design:** Ensure the platform is easy to navigate for both job seekers and employers.
- **Responsive Interface:** Adapt the interface for various devices, providing a seamless experience across platforms.

#### User Stories

[Not ready yet]

#### Customization and Flexibility

[Not ready yet]

#### Future Enhancements

- **Recommendation System:** Suggest jobs to seekers based on their profile and application history.
- **Analytics for Employers:** Provide insights into job postings and applicant demographics.

---

### Testing

#### HTML Validation

[Not ready yet]

#### CSS Validation

[Not ready yet]

#### Accessibility

[Not ready yet]

#### Wave Validation

[Not ready yet]

#### Lighthouse Validation

[Not ready yet]

#### JSHint Validation

[Not ready yet]

#### Device Testing

[Not ready yet]

#### Browser Compatibility

[Not ready yet]

#### User Stories Testing

[Not ready yet]

---

### Collaborative Efforts

[Not ready yet]

---

### Current State and Future Plans

#### Current State

The platform is currently in development with basic functionalities for user registration, job listing management, and application tracking implemented.

#### Future Plans

- **Enhanced Security:** Implement two-factor authentication and other security measures.
- **Advanced Search:** Improve the search functionality with more filters and sorting options.
- **User Feedback:** Integrate a feedback system for continuous improvement.

---

### Deployment

[Not ready yet]

---

### License

[Not ready yet]

---

### Bugs and Challenges

[Not ready yet]

---

### Acknowledgement

[Not ready yet]

---

This document serves as an initial guide for understanding the structure and goals of XemiJobs. It will be updated continuously as the project progresses and more details are finalized.