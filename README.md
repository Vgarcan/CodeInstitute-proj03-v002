# Xemijobs - Job Search Website
![Main LOGO](/xemijobs/static/imgs/banner1.webp)




# Victor Garcia Cantalapidera 
-Slack:[@Victor Garcia](https://code-institute-room.slack.com/team/U0695HZA7FZ)

-GitHub: [Vgarcan](https://github.com/Vgarcan)

-LinkedIn: [Victor Garcia](https://www.linkedin.com/in/vgc89/)

>[Play me!!](https://vgarcan.github.io/CodeInstitute-proj02/assets/audio/xemai/docume.mp3)

## Check us out!

[XemiJobs - Heroku](https://xemijobs-616b41a185c0.herokuapp.com/) 



## Table of Contents

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
  - [PEP8 Validation](#pep8-validation)
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


## Introduction

XemiJobs is a job search platform designed to connect employers with potential candidates. This project was born out of my frequent personal use of job search websites, which sparked the idea to create a platform that could facilitate the hiring process more efficiently. The website allows companies to post job vacancies and manage applications, while job seekers can browse listings, apply for jobs, and manage their applications—all from a desktop interface.

The concept for XemiJobs emerged from my own experiences and the desire to build something that could help others in similar situations. I saw this as a great opportunity to deepen my understanding of web development and to create a functional tool that serves a real purpose. The goal of this project is simple: to create a platform that bridges the gap between job seekers and employers, making it easier for them to connect and communicate.

![AMIRESPONSE photo](/xemijobs/static/imgs/readme-pics/amir-pic.png)
>[Check AMIRESPONSE](https://ui.dev/amiresponsive?url=https://xemijobs-616b41a185c0.herokuapp.com/)

I'm incredibly proud of how this project has developed and hope it can serve as a useful resource for anyone involved in the job search or hiring process.

## Features

- **User Registration and Authentication:** Secure registration and login for job seekers and employers, with role-based access control to ensure users see only what they need.
![Responsive Jobs](/xemijobs/static/imgs/readme-pics/form-login.png)
- **Job Listings Management:** Employers can create, update, and delete job listings. The listings are displayed dynamically on the platform, allowing job seekers to browse through the latest opportunities.
- **Application Management:** Job seekers can apply for jobs directly through the platform, track the status of their applications, and receive updates as they progress through the hiring process.
- **Dynamic Dashboard for Employers:** The company dashboard provides a real-time overview of key metrics, such as the number of job postings, applications received, and interviews scheduled, helping employers manage their recruitment process effectively.
![Responsive Jobs](/xemijobs/static/imgs/readme-pics/dashboard.png)
- **Real-Time Job Count:** The platform features a hero section that displays the current number of job listings, updated in real-time, offering users an up-to-date view of available opportunities.
![Responsive Jobs](/xemijobs/static/imgs/readme-pics/jobs-resp.png)
- **Advanced Search and Filters:** Job seekers can search for positions based on various criteria like job title, location, and company, with results being dynamically updated.

## Development Tools

- **Custom Jinja Widgets:** A collection of reusable Jinja widgets has been created to streamline the development process. These widgets automatically adapt to the type of data being passed, ensuring a consistent aesthetic across the entire platform. This approach not only speeds up development but also maintains a high level of visual and functional uniformity throughout the site.
>[Preview all widgets included in this site](https://xemijobs-616b41a185c0.herokuapp.com/widgets/1)
- **Modular Design:** The platform is built using a modular architecture in Flask, which allows for easy extension and maintenance. Each module is self-contained, facilitating rapid development and testing of individual components without affecting the entire application.
- **Consistent Aesthetic:** By leveraging these custom widgets, the design remains consistent, providing a unified look and feel across all pages and components, which enhances the overall user experience.

## Technologies Used

### Backend
- <img src="xemijobs/static/imgs/readme-pics/flask-icon.ico" width="18px"> **Flask:** The core framework for the backend of the application, used for handling routing, sessions, and integrating with the database.
- <img src="xemijobs/static/imgs/readme-pics/login-icon.ico" width="18px"> **Flask-Login:** Employed to manage user sessions and authentication, ensuring secure access control throughout the platform.
- <img src="xemijobs/static/imgs/readme-pics/mongo-icon.ico" width="18px"> **Flask-PyMongo:** Utilized for integrating Flask with MongoDB, facilitating database operations directly from the Flask application.

### Database
- <img src="xemijobs/static/imgs/readme-pics/mongo-icon.ico" width="18px"> **MongoDB:** The primary database used to store user data, job listings, and application details, chosen for its flexibility and scalability.

### Frontend
- <img src="xemijobs/static/imgs/readme-pics/html_icon.ico" width="18px"> **HTML:** The foundation for structuring the web pages, providing the semantic markup needed for the site's content.
- <img src="xemijobs/static/imgs/readme-pics/css-icon.ico" width="18px"> **CSS:** Applied to style and layout the web pages, ensuring a consistent and visually appealing user interface across the application.
- <img src="xemijobs/static/imgs/readme-pics/js-icon.ico" width="18px"> **JavaScript:** Employed to add interactivity and dynamic elements to the site, enhancing the user experience with features like form validation and asynchronous content updates.
- <img src="xemijobs/static/imgs/readme-pics/bootstrap-icon.ico" width="18px"> **Bootstrap:** Integrated to utilize its responsive grid system and pre-built components, ensuring the site is mobile-friendly and adaptable to different screen sizes.


## Project Structure

- <img src="xemijobs/static/imgs/readme-pics/red-folder-icon.ico" width="18px"> **Root Directory**
    
    - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **xemijobs/** (Main application folder)

        - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the application)
        - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `extensions.py` (Handles extensions and configurations)
        - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `decorators.py` (Custom decorators for the application)
        
        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **static/** (Static assets like images, CSS, and JS files)
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **css/** (Contains CSS stylesheets)
                - <img src="xemijobs/static/imgs/readme-pics/css-filetype-icon.ico" width="18px"> `main.css` (Main stylesheet)
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
                - <img src="xemijobs/static/imgs/readme-pics/js-filetype-icon.ico" width="18px"> `main.js` (Main JavaScript file)
            - <img src="xemijobs/static/favicon.ico" width="18px"> `favicon.ico` (Favicon for the website)

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/** (Main templates directory)
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **widgets/** (Reusable widgets for the application)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `alert.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `cards.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `carousel.html`
                - <p>...</p>
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **xemijobs/** (Core templates for the application)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `base.html` (Base template for the application)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `temp-sheet.html` (Temporary template for the project)

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **users/** (Handles user-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the user module)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py` (Forms related to user interactions)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py` (User models and database interactions)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py` (User views and routes)
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/users/** (HTML templates for user-related views)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `dashboard.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `profile.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `login.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `register.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `show-user.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `user-list.html`

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **companies/** (Handles company-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the company module)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py` (Forms related to company interactions)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py` (Company models and database interactions)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py` (Company views and routes)
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/companies/** (HTML templates for company-related views)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `dashboard.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `adv-dash.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `profile.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `login.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `register.html`

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **applications/** (Handles applications-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the applications module)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py` (Forms related to applications)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py` (Application models and database interactions)
            - <img src="`xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py` (Application views and routes)
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/applications/** (HTML templates for application-related views)
                
        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **main/** (Handles main-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the main module)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py` (Forms related to the main module)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py` (Main module models and database interactions)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py` (Main module views and routes)
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/main/** (HTML templates for main-related views)
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `temp-sheet.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `404.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `403.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `401.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `tnc.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `about-us.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `index.html`
                - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `widgets-collection.html`

        - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **jobs/** (Handles job-related functionalities)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `__init__.py` (Initializes the jobs module)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `forms.py` (Forms related to job management)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `models.py` (Job models and database interactions)
            - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `views.py` (Job views and routes)
            - <img src="xemijobs/static/imgs/readme-pics/folder-icon.ico" width="18px"> **templates/jobs/** (HTML templates for job-related views)
              - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `create-job.html`
              - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `job-list.html`
              - <img src="xemijobs/static/imgs/readme-pics/html-filetype-icon.ico" width="18px"> `view-job.html`

    - <img src="xemijobs/static/imgs/readme-pics/git-icon.ico" width="18px"> `.gitignore` (Specifies files to be ignored by Git)
    - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `config.py` (Configuration settings for the application)
    - <img src="xemijobs/static/imgs/readme-pics/ic-info-outline.ico" width="18px"> `README.md` (Project README file)
    - <img src="xemijobs/static/imgs/readme-pics/procfile-filetipe-icon.ico" width="18px"> `Procfile` (Process file for Heroku deployment)
    - <img src="xemijobs/static/imgs/readme-pics/py-filetype-icon.ico" width="18px"> `run.py` (Main entry point to run the application)
    - <img src="xemijobs/static/imgs/readme-pics/txt-filetype-icon.ico" width="18px"> `requirements.txt` (List of Python dependencies)
    - <img src="xemijobs/static/imgs/readme-pics/txt-filetype-icon.ico" width="18px"> `runtime.txt` (Specifies Python version for deployment)

### CSS Management for Project Structure




## Wireframes

[Not ready yet]
### Wireframes for Desktop
<details>
  <summary>Wireframe for Homepage</summary>
  <img src="xemijobs/static/imgs/readme-pics/wf-home.png" style="display: block; margin: auto;" alt="Wireframe for index page - Desktop">
</details>

<details>
  <summary>Wireframe for Dashboard</summary>
  <img src="xemijobs/static/imgs/readme-pics/wf-dash.png" style="display: block; margin: auto;" alt="Wireframe for Dashboard pages - Desktop">
</details>

### Wireframes for Responsive Devices
<details>
  <summary>Wireframe for Homepage</summary>
  <img src="xemijobs/static/imgs/readme-pics/wf-home-resp.png" style="display: block; margin: auto;" alt="Wireframe for index page - Mobile">
</details>

<details>
  <summary>Wireframe for Dashboard</summary>
  <img src="xemijobs/static/imgs/readme-pics/wf-dash-resp.png" style="display: block; margin: auto;" alt="Wireframe for Dashboard pages - Mobile">
</details>


## Colors

The color palette for this project has been carefully selected to ensure a professional and clean aesthetic, aligning with the brand identity and enhancing user experience. Below is a breakdown of the primary colors used across the application:

![Color Palette](xemijobs/static/imgs/readme-pics/color-palette.png)

- **Primary Color:** `#1F2937` - A deep, rich grey used as the main color for text and primary elements, ensuring clarity and focus.
- **Warning Color:** `#d9a805d3` - A bold yellow-gold with transparency, used for alerts and warnings, drawing attention without being overwhelming.
- **Secondary Color:** `#1e97f3` - A vibrant blue utilized for secondary elements and highlights, adding a touch of brightness and modernity.
- **Accent Color:** `#10B981` - A fresh green applied for accents, buttons, and interactive elements, bringing a sense of vitality and positive action.
- **Background Color:** `#e2e3e4` - A soft grey used for background elements, creating a neutral canvas that allows content to stand out.
- **Main Text Color:** `#1F2937` - The same deep grey as the primary color, ensuring consistency and readability across all text elements.
- **Secondary Text Color:** `#020556f2` - A dark navy with a slight transparency, used for secondary text, providing a subtle contrast to the main text.
- **Alternative Text Color:** `#ffffffda` - A near-white color with transparency, used for text on darker backgrounds, ensuring readability.
- **White Color:** `#FFFFFF` - Pure white, used for backgrounds and text where maximum contrast is required.
- **Secondary Color Transparency:** `#2d69c9a8` - A semi-transparent version of the secondary blue, used for overlays and subtle highlights.
- **Accent Color Transparency:** `#0f9f7968` - A semi-transparent green, used for hover states and subtle accent effects, maintaining brand consistency.
- **Light Gray Color:** `#E5E7EB` - A light grey used for borders, dividers, and other UI elements, providing structure without drawing attention.
- **Hover Accent Color:** `#0F9F79` - A darker shade of the accent green, applied to buttons and interactive elements on hover, signaling action.
- **Hover Button Color:** `#cf8168` - A muted coral used for hover states on specific buttons, adding warmth and emphasis.
- **White Text Shadow:** `1px 1px 1px var(--secondary-text-color)` - A subtle text shadow used on light backgrounds to enhance readability and add depth.
- **Dark Text Shadow:** `1px 1px 4px var(--white-color)` - A bolder text shadow used on dark backgrounds, ensuring that text stands out clearly.
- **Transparent:** `#000000` - Black with full transparency, used to achieve various effects without adding color.

This color palette was chosen not only for its visual appeal but also for its contribution to a cohesive and user-friendly interface, reinforcing the professional and serious tone of the application.

### Color Customization Process

[Not ready yet]

## User-Friendly Approach

The user-centric approach was a key consideration throughout the design and development of this platform. The primary goal is to create an intuitive, accessible, and efficient experience for all users, whether they are job seekers or employers. The following principles and strategies were applied to achieve this:

- **Responsive Design:** The application was built with a mobile-first approach, ensuring it is fully responsive and functional across all devices, from smartphones to desktops. This guarantees that users can comfortably access the platform, regardless of the device they use.

- **Consistency in UI/UX:** Consistency in the user interface (UI) and user experience (UX) is a priority. This has been achieved by implementing reusable widgets throughout the platform. These widgets ensure that elements such as tables, forms, and feedback messages maintain a consistent style across both company dashboards and individual user dashboards. For example, the same tables are used in both types of dashboards, ensuring a uniform experience. The widgets have been designed to automatically adjust to the provided information or to allow customization as needed, using Jinja in some cases.

- **Clear and Simple Navigation:** The platform features a straightforward and intuitive navigation system. Menus, buttons, and links are clearly labeled, making it easy for users to find the information or tools they need without confusion. Unnecessary elements have been avoided, maintaining a clean and direct interface.

- **Real-Time Feedback:** To ensure consistency and clarity in system feedback, a widget based on Flash has been implemented to handle error and success messages. This widget ensures that feedback messages are uniform and automatically adapt to the context of the user's interaction, offering a more predictable and coherent experience.

![Alerts widget](/xemijobs/static/imgs/readme-pics/flash-msgs.png)

- **Optimized Performance:** The application has been optimized for fast loading times and smooth performance, which is crucial for retaining users and providing a positive experience. This includes efficient data handling and minimizing the use of large resources that could slow down the site.

- **Engaging Visuals:** The platform's design incorporates modern and appealing visual elements, such as icons, images, and animations, that enhance the user experience without overwhelming or distracting them. The simplicity and clarity in the visual presentation help users focus on the platform's key functions without being confused by unnecessary elements.

This user-focused approach ensures that the platform is not only functional but also enjoyable to use, encouraging users to return and engage with the service regularly.



## User Experience

### Key Principles

- **Intuitive Design:** Ensure the platform is easy to navigate for both job seekers and employers.
- **Responsive Interface:** Adapt the interface for various devices, providing a seamless experience across platforms.

## User Stories

### First-Time Users
1. **As a First-Time User,** I want to easily understand the purpose of the website, so I can decide if it meets my needs for job searching or posting job vacancies.
   - *Acceptance Criteria:* Upon landing on the homepage, I should see a clear and concise explanation of the platform's features and benefits.

2. **As a First-Time User,** I want to quickly register on the platform, so I can start using the available services without any hassle.
   - *Acceptance Criteria:* The registration process should be straightforward, with a simple form requiring only necessary information, and should be completed within a few steps.

### Job Seekers
1. **As a Job Seeker,** I want to search for jobs that match my skills and location, so I can find relevant opportunities quickly.
   - *Acceptance Criteria:* The search functionality should allow me to filter jobs by keywords, location, job type, and other relevant criteria.

2. **As a Job Seeker,** I want to view detailed information about job postings, so I can understand the job requirements and decide if I want to apply.
   - *Acceptance Criteria:* Each job listing should include a comprehensive description, including job responsibilities, requirements, and company details.

3. **As a Job Seeker,** I want to track the status of my job applications, so I can stay informed about the progress and next steps.
   - *Acceptance Criteria:* The dashboard should provide a clear overview of my submitted applications, including their status (e.g., pending, reviewed, interview scheduled).

### Employers
1. **As an Employer,** I want to post job vacancies quickly and efficiently, so I can attract potential candidates without unnecessary delays.
   - *Acceptance Criteria:* The job posting form should be user-friendly, allowing me to input all necessary details such as job title, description, requirements, and salary range.

2. **As an Employer,** I want to view analytics related to my job postings, so I can understand the effectiveness of my job ads and make informed decisions about future postings.
   - *Acceptance Criteria:* The platform should offer basic analytics, such as the number of views per job posting, number of applications received, and other relevant metrics.


### Customization and Flexibility

[Not ready yet]

### Future Enhancements

- **Recommendation System:** Suggest jobs to seekers based on their profile and application history.
- **Analytics for Employers:** Provide insights into job postings and applicant demographics.


## Testing

### HTML Validation

We ensured that the HTML structure of XemiJobs adheres strictly to web standards. We utilized the W3C Validator to validate our HTML code, striving to minimize and eliminate all possible errors. I'm proud to report that the validation results showed **zero errors**.

The most challenging part of this process was ensuring that our reusable widgets did not introduce any validation errors. After thorough adjustments and testing, we successfully resolved all issues, making the HTML structure robust and error-free.

Here’s the validation result:

<details>
  <summary>Click to view HTML Validation Result</summary>
  <img src="xemijobs/static/imgs/readme-pics/markup-val.png" style="display: block; margin: auto;" alt="HTML Validation Result showing zero errors">
</details>

---

**You can also view the validation result directly on the [W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fxemijobs-616b41a185c0.herokuapp.com).**


### CSS Validation

<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>

The CSS of XemiJobs has been carefully crafted and validated to ensure it adheres to the highest standards. We utilized the W3C CSS Validator to check for any errors, and I'm pleased to report that our stylesheets passed with **zero errors**.

This thorough validation process ensures that the user interface is both visually appealing and fully compliant with modern web standards. We took particular care to validate our responsive design elements to ensure consistency across all devices.

Here’s the validation result:

<details>
  <summary>Click to view CSS Validation Result</summary>
  <img src="xemijobs/static/imgs/readme-pics/css-val.png" style="display: block; margin: auto;" alt="CSS Validation Result showing zero errors">
</details>

---


**You can also view the validation result directly on the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fxemijobs-616b41a185c0.herokuapp.com&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).**

### Accessibility

Ensuring accessibility is a key priority for XemiJobs. We've taken great care to make sure our platform is inclusive and usable by as many people as possible, regardless of their abilities or the devices they are using.

Throughout the development process, we adhered to the Web Content Accessibility Guidelines (WCAG) to guarantee that our site meets accessibility standards. This includes:

- **Proper use of ARIA attributes:** We have utilized ARIA attributes effectively to enhance the accessibility of dynamic content and interactive elements, ensuring screen readers can accurately convey the information to users.
- **Keyboard Navigation:** All interactive elements, including forms, buttons, and navigation links, are fully accessible via keyboard navigation, making the site usable without a mouse.
- **Contrast Ratios:** We carefully selected our color scheme to ensure sufficient contrast between text and background colors, making the content readable for users with visual impairments.
- **Alt Text for Images:** All images include descriptive `alt` attributes, providing context to users who rely on screen readers.

These efforts help ensure that our site is not only compliant with accessibility standards but also provides an inclusive user experience. We continue to monitor and improve the accessibility of XemiJobs as we develop new features and enhancements.



### Wave Validation

We conducted a thorough accessibility audit using the WAVE (Web Accessibility Evaluation Tool). The results were highly satisfactory, especially for the main page, where we encountered zero errors. However, we did find a few contrast issues, primarily related to the navigation elements within the carousel.

To address these contrast issues, we added a transparent background to the carousel buttons. Despite this adjustment, the contrast warnings persist. We believe that these contrast issues do not significantly impact usability, as the primary goal for the carousel is to showcase images clearly. The transparency ensures that the images are visible while still allowing users to intuitively locate the buttons.

<img src="xemijobs/static/imgs/readme-pics/wave-carousel.png" style="display: block; margin: auto;" alt="Carousel showing controller buttons">
<br>

Additionally, contrast warnings were noted in the Flash messages—interestingly, all colors except yellow were flagged. While we understand that white text on a yellow background might pose a readability challenge, WAVE does not flag it as an issue. Conversely, other colors, which do not seem problematic to us, were marked for contrast errors.

<img src="xemijobs/static/imgs/readme-pics/wave-flash.png" style="display: block; margin: auto;" alt="Wave flash contrast errors">
<br>

We also identified contrast issues with the modal buttons, which follow a similar color pattern to the Flash Danger alerts. However, the inclusion of shadow effects and other design enhancements significantly aids visibility. We believe these design choices ensure the buttons remain accessible and visually clear, even if they do not fully meet WAVE’s contrast recommendations.

<img src="xemijobs/static/imgs/readme-pics/wave-button-alert.png" style="display: block; margin: auto;" alt="Wave button contrast error">
<br>

Overall, the WAVE validation confirms that our website adheres to accessibility standards, with only a few minor contrast issues that have been carefully considered in the design process. While we will continue exploring potential solutions to these issues, we have prioritized maintaining a visually cohesive and intuitive theme for the site.

We identified some contrast issues specifically related to the numbers displayed on our error pages (e.g., 404, 403, 401). On the 404 page, no changes were made, as we believe the background image sufficiently offsets any potential visibility issues with the numbers. However, on the 403 and 401 pages, we made deliberate changes to the color of certain numbers to enhance contrast and ensure readability. 

<img src="xemijobs/static/imgs/readme-pics/wave-403.png" style="display: block; margin: auto;" alt="Wave button contrast error 1">
<hr>
<img src="xemijobs/static/imgs/readme-pics/wave-404.png" style="display: block; margin: auto;" alt="Wave button contrast error 2">
<br>

Specifically, we altered the colors of the "4" and "3" on the 403 page and the "4" and "1" on the 401 page to address the contrast errors flagged by WAVE. We retained the original color of the "0" to maintain visual consistency and a playful design element, although it technically does not meet the strict contrast criteria set by WAVE. We do not consider this to be a significant issue, as the overall visual experience is still clear and user-friendly.

**Note:** We are fully aware of the contrast issues highlighted by the WAVE Validation Tool. Our team is committed to addressing these in future updates to ensure an even higher level of accessibility across the entire platform. We appreciate the insights provided by the tool and will use this feedback to guide our ongoing improvements.


### Lighthouse Validation

Our Lighthouse validation results have been very promising, with high scores across most categories. One area where we observed a slightly lower score is in SEO, and we are actively working on improvements in this area to achieve even better results. Lighthouse has been instrumental in guiding the organization of our files and optimizations for performance.

<img src="xemijobs/static/imgs/readme-pics/lighthouse-web.png" style="display: block; margin: auto;" alt="Wave button contrast error">
<br>

A specific recommendation from Lighthouse was to utilize WebP format for images to enhance load times. In response, we have ensured that all images served through the browser are in WebP format. However, we also recognize that excessive compression could detract from the user experience, particularly on larger screens. Therefore, we made a deliberate choice to balance performance with visual quality. After gathering feedback from a diverse group of users, we've confirmed that the image quality is well-received across different devices. Consequently, we decided to maintain slightly larger image sizes to prioritize a seamless and visually pleasing user experience, even if it means sacrificing a small amount of performance.

Additionally, Lighthouse suggested reducing the CSS payload, which we are considering. One approach we're exploring is to divide the main `styles.css` file into smaller files associated with individual widgets. This would allow us to send only the necessary CSS for each page, potentially reducing the overall size of the CSS file and improving page load times.

While our desktop version scores are very high, the mobile version, though still passing, shows some room for improvement. We are committed to enhancing these aspects to ensure an optimal user experience across all devices.


### JSHint Validation

[Not ready yet]


### PEP8 Validation

[Not ready yet]


### Device Testing

The website has undergone thorough testing across a variety of devices, including desktop computers, tablets, and smartphones. We focused on ensuring that the responsiveness of the site is consistent and effective across all screen sizes, providing an optimal user experience regardless of the device used.

To achieve this, we employed media queries to adapt the layout for different screen sizes. This approach ensures that when the device's dimensions fall within specific ranges, certain elements will reposition themselves, maintaining readability and proper alignment. 

For instance, on smaller screens, such as smartphones, we adjusted the distribution of content to ensure that all elements are easily accessible and clearly visible, avoiding any overlap or readability issues. The result is a fluid and intuitive experience across devices, meeting our goal of a responsive design that performs well on all tested platforms.


### Browser Compatibility

We have conducted extensive testing to ensure that the website is fully compatible across a range of web browsers. Specifically, the site has been tested on:

- <img src="xemijobs/static/imgs/readme-pics/google-icon.ico" width="18px"> **Google Chrome**
- <img src="xemijobs/static/imgs/readme-pics/edge-icon.ico" width="18px"> **Microsoft Edge**
- <img src="xemijobs/static/imgs/readme-pics/opera-icon.ico" width="18px"> **Opera**
- <img src="xemijobs/static/imgs/readme-pics/firefox-icon.ico" width="18px"> **Mozilla Firefox**
- <img src="xemijobs/static/imgs/readme-pics/safari-icon.ico" width="18px"> **Safari**

In each browser, the website performs smoothly, maintaining consistent functionality and appearance. We focused on ensuring that all features, from user registration to job application processes, operate seamlessly regardless of the browser used.

No significant issues were encountered during the tests, confirming that our site is accessible and reliable across these popular browsers. This ensures that users can interact with the platform without any unexpected disruptions, regardless of their preferred browser.


### User Stories Testing

#### First-Time Users

| **Feature** | **Action** | **Expected Result** | **Actual Result**|
|-------------|------------|---------------------|------------------|
| **Platform Introduction**| Visit the home page and read introductory content             | Clear understanding of the platform's purpose                     | Works as expected   |
| **User Registration**     | Complete the registration form and submit                    | Registration completed quickly with minimal steps                 | Works as expected   |

#### Job Seekers

| **Feature** | **Action** | **Expected Result** | **Actual Result**|
|-------------|------------|---------------------|------------------|
| **Job Search**           | Use the search bar to filter jobs by keyword, location, and job type | Display of relevant job listings that match the criteria            | Works as expected   |
| **Job Details View**     | Click on a job listing to view more details                   | Display of comprehensive job details, including requirements and company information | Works as expected   |
| **Application Tracking** | Navigate to the dashboard to view the status of job applications | Clear overview of application status (e.g., pending, reviewed, interview scheduled) | Works as expected   |

#### Employers

| **Feature** | **Action** | **Expected Result** | **Actual Result**|
|-------------|------------|---------------------|------------------|
| **Job Posting**          | Complete and submit the job posting form                     | Job vacancy is posted with all required details                   | Works as expected   |
| **Job Posting Analytics**| Access the dashboard to view analytics for job postings      | Display of basic analytics, such as views per job and number of applications received | Works as expected   |


## Collaborative Efforts

[Not ready yet]


## Current State and Future Plans

### Current State

The platform is currently in development with basic functionalities for user registration, job listing management, and application tracking implemented.

### Future Plans

- **Enhanced Security:** Implement two-factor authentication and other security measures.
- **Advanced Search:** Improve the search functionality with more filters and sorting options.
- **User Feedback:** Integrate a feedback system for continuous improvement.


## Deployment

### Prerequisites

Before you begin, make sure you have the following:

1. A **Heroku account**. If you don’t have one, you can sign up for free at [Heroku](https://www.heroku.com).
2. Your project should include the following files:
   - `Procfile`: Specifies the commands that are executed by the app on startup.
   - `requirements.txt`: Lists all the Python dependencies for your project.
   - `runtime.txt`: (optional) Specifies the Python version.
   - `.gitignore`: Ensures that unnecessary files aren’t uploaded to Heroku.
   - `config.py`: Your configuration file that holds essential settings, like database connection strings.

---

### Step-by-Step Deployment Instructions

1. **Create a New Heroku App:**
   - Log in to your Heroku account at [Heroku Dashboard](https://dashboard.heroku.com/).
   - Click on the **New** button in the upper right corner, then select **Create New App**.
   ![Heroku Dashboard](/xemijobs/static/imgs/readme-pics/heroku-1.png)
   - Enter a unique app name (Heroku will check the availability of the name) and choose your preferred region (United States or Europe).
   - Click **Create App**.
   ![Heroku Dashboard](/xemijobs/static/imgs/readme-pics/heroku-2.png)

2. **Connect Your GitHub Repository:**
   - Once your app is created, you’ll be taken to the app’s dashboard.
   - Navigate to the **Deploy** tab.
   ![Heroku Dashboard](/xemijobs/static/imgs/readme-pics/heroku-3.png)
   - In the **Deployment method** section, select **GitHub**.
   - You’ll be prompted to connect your GitHub account if you haven’t done so already.
   - Once connected, search for the repository you want to deploy (e.g., `XemiJobs`).
   - Click **Connect**.
   ![Heroku Dashboard](/xemijobs/static/imgs/readme-pics/heroku-4.png)


3. **Configure Deployment Settings:**
   - In the **Automatic Deploys** section, you can choose to enable automatic deployment from the `main` branch. This means that every time you push changes to `main`, Heroku will automatically redeploy your app.
   - For a first-time deployment, it’s often safer to start with **Manual Deploy**. In the **Manual Deploy** section, select the branch you want to deploy (usually `main`) and click **Deploy Branch**.
   ![Heroku Dashboard](/xemijobs/static/imgs/readme-pics/heroku-7.png)

4. **Setup Environment Variables:**
   - Navigate to the **Settings** tab in your Heroku app’s dashboard.
   ![Heroku Dashboard](/xemijobs/static/imgs/readme-pics/heroku-5.png)
   - Click on **Reveal Config Vars**.
   - Add any necessary environment variables that your app requires (e.g., `FLASK_APP`, `FLASK_ENV`, `SECRET_KEY`, `DATABASE_URL`).
   - These variables should match what’s defined in your `config.py` or `.env` file locally.
   ![Heroku Dashboard](/xemijobs/static/imgs/readme-pics/heroku-6.png)

5. **Heroku Build and Deployment:**
   - After you trigger a deploy (either manually or automatically), Heroku will start the build process.
   - You can view the build process in real-time within the Heroku dashboard.
   - If the deployment is successful, you’ll see a confirmation message and a **View** button that will take you to your live app.

6. **Check Your Application:**
   - Once the deployment is complete, visit the live app by clicking on the **View** button or navigating to `https://your-app-name.herokuapp.com/`.
   - Test the various features of your app to ensure everything is working as expected.

7. **Further Customization and Monitoring:**
   - Heroku provides a rich set of tools for monitoring your app’s performance, scaling the number of dynos (containers), and managing your app's logs.
   - You can explore these options within the Heroku dashboard to optimize and maintain your deployment.

---

### Troubleshooting Tips

- **Dependencies Issues:** Ensure that all your dependencies are correctly listed in `requirements.txt`. Any missing dependency could cause the deployment to fail.
- **Database Configuration:** If your app uses a database, make sure the `DATABASE_URL` is correctly configured in your environment variables.
- **Build Failures:** Check the build logs for any errors. Heroku provides detailed logs that can help identify where things went wrong.



## License

XEMIJOBS is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

![License](/xemijobs/static/imgs/readme-pics/license.jpg)

You are free to:

- **Share:** Copy and redistribute the material in any medium or format.

- **Adapt:** Remix, transform, and build upon the material.

Under the following terms:

- **Attribution:** You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

- **NonCommercial:** You may not use the material for commercial purposes.

- **ShareAlike:** If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

For more information about the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License, visit [here](https://creativecommons.org/licenses/by-nc-sa/4.0/).



## Bugs and Challenges

[Not ready yet]


## Acknowledgement

I feel incredibly fortunate to have had access to a wealth of information available on the internet throughout the development of XemiJobs. Over the course of this project, I’ve encountered countless resources, from videos to blog posts, that have been instrumental in guiding me through various challenges. Unfortunately, due to the sheer volume of content I’ve consumed, I’ve lost track of many of the specific links. Nonetheless, I want to express my gratitude to all the creators who have shared their knowledge and experiences online, making the learning process smoother.

A significant portion of the success of this project can be attributed to the excellent documentation provided for the tools and libraries I’ve used. The official documentation for Flask, Flask-WTF, and Flask-PyMongo has been particularly invaluable. These resources not only provided the in-depth knowledge I needed to implement features but also offered solutions to specific issues that arose during development. The documentation is well-written, clear, and incredibly useful, serving as a robust foundation for the project.

What made the documentation even more beneficial was the inclusion of code snippets directly within the documentation itself. Whenever I needed to perform a task, such as inserting data into a MongoDB collection using PyMongo, I could simply search through the documentation, find a relevant snippet, and copy-paste it into my project. This approach significantly sped up the development process and ensured that I was implementing best practices as recommended by the official sources. The convenience and reliability of these snippets reinforced just how critical high-quality documentation can be for a project.

While tutorials and videos have been helpful as introductory material, offering quick insights and practical examples, the real depth of understanding came from diving into the official documentation. The step-by-step guides, detailed explanations, and readily available snippets have been indispensable.

#### Key Documentation Resources:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)
- [Flask-PyMongo Documentation](https://flask-pymongo.readthedocs.io/)

#### Additional Resources:
- [Python Flask Authentication Tutorial - Learn Flask Login (by: Arpan Neupane)](https://www.youtube.com/watch?v=71EU8gnZqZQ)
- [Creating a User Login System Using Python, Flask and MongoDB (by: Pretty Printed)](https://www.youtube.com/watch?v=vVx1737auSE)
- [Flask and MongoDB w/ Flask-pymongo | Project Setup (by: Code With Prince)](https://www.youtube.com/watch?v=tJxMPvzkCyo&list=PLU7aW4OZeUzwN0TsZLZUuzhc0f7OVVBcT)
- [Flask Blueprints Make Your Apps Modular & Professional (by: NeuralNine)](https://www.youtube.com/watch?v=_LMiUOYDxzE)


---

This document serves as an initial guide for understanding the structure and goals of XemiJobs. It will be updated continuously as the project progresses and more details are finalized.