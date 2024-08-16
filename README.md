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

#### CSS Management for Project Structure

[Not ready yet]

---

### Wireframes

[Not ready yet]

---

### Colors

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

#### Color Customization Process

[Not ready yet]

### User-Friendly Approach

The user-centric approach was a key consideration throughout the design and development of this platform. The primary goal is to create an intuitive, accessible, and efficient experience for all users, whether they are job seekers or employers. The following principles and strategies were applied to achieve this:

- **Responsive Design:** The application was built with a mobile-first approach, ensuring it is fully responsive and functional across all devices, from smartphones to desktops. This guarantees that users can comfortably access the platform, regardless of the device they use.

- **Consistency in UI/UX:** Consistency in the user interface (UI) and user experience (UX) is a priority. This has been achieved by implementing reusable widgets throughout the platform. These widgets ensure that elements such as tables, forms, and feedback messages maintain a consistent style across both company dashboards and individual user dashboards. For example, the same tables are used in both types of dashboards, ensuring a uniform experience. The widgets have been designed to automatically adjust to the provided information or to allow customization as needed, using Jinja in some cases.

- **Clear and Simple Navigation:** The platform features a straightforward and intuitive navigation system. Menus, buttons, and links are clearly labeled, making it easy for users to find the information or tools they need without confusion. Unnecessary elements have been avoided, maintaining a clean and direct interface.

- **Real-Time Feedback:** To ensure consistency and clarity in system feedback, a widget based on Flash has been implemented to handle error and success messages. This widget ensures that feedback messages are uniform and automatically adapt to the context of the user's interaction, offering a more predictable and coherent experience.

- **Optimized Performance:** The application has been optimized for fast loading times and smooth performance, which is crucial for retaining users and providing a positive experience. This includes efficient data handling and minimizing the use of large resources that could slow down the site.

- **Engaging Visuals:** The platform's design incorporates modern and appealing visual elements, such as icons, images, and animations, that enhance the user experience without overwhelming or distracting them. The simplicity and clarity in the visual presentation help users focus on the platform's key functions without being confused by unnecessary elements.

This user-focused approach ensures that the platform is not only functional but also enjoyable to use, encouraging users to return and engage with the service regularly.


---

### User Experience

#### Key Principles

- **Intuitive Design:** Ensure the platform is easy to navigate for both job seekers and employers.
- **Responsive Interface:** Adapt the interface for various devices, providing a seamless experience across platforms.

### User Stories

#### First-Time Users
1. **As a First-Time User,** I want to easily understand the purpose of the website, so I can decide if it meets my needs for job searching or posting job vacancies.
   - *Acceptance Criteria:* Upon landing on the homepage, I should see a clear and concise explanation of the platform's features and benefits.

2. **As a First-Time User,** I want to quickly register on the platform, so I can start using the available services without any hassle.
   - *Acceptance Criteria:* The registration process should be straightforward, with a simple form requiring only necessary information, and should be completed within a few steps.

#### Job Seekers
1. **As a Job Seeker,** I want to search for jobs that match my skills and location, so I can find relevant opportunities quickly.
   - *Acceptance Criteria:* The search functionality should allow me to filter jobs by keywords, location, job type, and other relevant criteria.

2. **As a Job Seeker,** I want to view detailed information about job postings, so I can understand the job requirements and decide if I want to apply.
   - *Acceptance Criteria:* Each job listing should include a comprehensive description, including job responsibilities, requirements, and company details.

3. **As a Job Seeker,** I want to track the status of my job applications, so I can stay informed about the progress and next steps.
   - *Acceptance Criteria:* The dashboard should provide a clear overview of my submitted applications, including their status (e.g., pending, reviewed, interview scheduled).

#### Employers
1. **As an Employer,** I want to post job vacancies quickly and efficiently, so I can attract potential candidates without unnecessary delays.
   - *Acceptance Criteria:* The job posting form should be user-friendly, allowing me to input all necessary details such as job title, description, requirements, and salary range.

2. **As an Employer,** I want to view analytics related to my job postings, so I can understand the effectiveness of my job ads and make informed decisions about future postings.
   - *Acceptance Criteria:* The platform should offer basic analytics, such as the number of views per job posting, number of applications received, and other relevant metrics.


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