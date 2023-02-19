# Feb 2023 hackathon

Run Development server:
`python3 manage.py runserver`

# Friends of Earth

## The mission of our website is to act as an NGO directory, where users can find information about many different NGOs worldwide, and be directed to more information about each one if they choose.

# Table of Contents

- [Scope](#scope)
- [Background](#background)
- [Scrum Master](#scrum-master)
- [Audience](#audience)
    - [User goals](#user-goals)
- [Wireframes](#wireframes)
- [Features](#features)
- [Development choices](#development-choices)
- [Design choices](#design-choices)
    - [Colour palette](#colour-palette)
    - [Font](#font)
    - [Images](#images)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Testing](#testing)
- [Credits](#credits)

# Scope


# Background

This project is part of the Code Institute February 2023 Hackathon. We researched World NGO Day and found that it aims to appreciate different NGOs across the world, and so decided that having a directory where users can browse different NGOs, perhaps filtering by region or type, would help users to find more specific information or bring awareness to different NGOs. It can also help users to find NGOs which they would like to be a part of or contribute towards.

**Repository:** [https://github.com/AdamBoley/Feb-2023-Hackathon](https://github.com/AdamBoley/Feb-2023-Hackathon)

**Final website:** [https://feb-2023-hackathon.herokuapp.com/](https://feb-2023-hackathon.herokuapp.com/)

# Scrum Master

As a Scrum Master our team had [Edmir Demaj](https://www.linkedin.com/in/edmir-demaj-42a501196/). As a Scrum Master my duties are:
- Work on Project idea together with the team.
- Plan how team members will work on this project.
- Keep notes for any suggestions, ideas, and changes on the project. 
- Find out which technologies will be used on this project to involve the whole team.
- Organise meetings via Slack for the team at suitable times for everyone.
- Provide a summary after each call on our Slack channel.
- Create and assign tasks to team members.
- Check the progress of each one at the end of day.
- Check the progress of the project to deploy before the deadline.
- Create a sprint goal for user stories, create To Do tasks and check their progress.
- Assist in any problems during project development.
- Make sure the product achieves its final goals.

Since this project is part of Hackathon February 2023 and the time is very limited to have a detailed plan, progress and final report all I could do is to implement all duties mentioned above. Below find the project board built on GitHub and the Sprint Goal made for user stories.

<details><summary>Project board on GitHub</summary>
<img src="static/project-img/project-board.png">
</details>
<details><summary>Sprint Goal</summary>
<img src="static/project-img/scrum-board.png">
</details>

# Audience

This project is aimed at anyone who wants to know more about NGOs worldwide. If the user wants to find out more or contribute directly to a specific NGO, they can find the link to take them directly to the NGO website itself.

## User goals

- To immediately determine the purpose of the site, so they can quickly decide whether or not to stay.
- To be able to easily access the site on a variety of devices - desktop, tablet, mobile.
- To be able to browse a variety of different NGOs in one place.
- To be able to filter NGOs by region.
- To be able to filter NGOs by type.
- To be able to read an overview of each NGO, e.g., purpose, founder and date it was founded, current director, location, etc.
- To be able to visit each NGO's website directly (opens in new tab).
- To find out information about World NGO day and when it is.

# Wireframes

Created using [Figma](https://www.figma.com/) (click to expand)

<details><summary>Homepage</summary>

![Homepage wireframe](documentation/wireframes/homepage.png)
</details>

<details><summary>About page</summary>

![About page wireframe](documentation/wireframes/about-page.png)
</details>

<details><summary>NGOs page</summary>

![NGOs page wireframe](documentation/wireframes/ngos-page.png)
</details>

<details><summary>Contact page</summary>

![Contact page wireframe](documentation/wireframes/contact-page.png)
</details>

# Features

### Logo

- Features an image of the Earth above the site name, 'Friends of Earth'.
- Uses green colours in-keeping with the site colour scheme and tying to nature and the Earth.

![Logo](documentation/design/logo.png)

### Navigation menu

- At the top of every page allows for easy site navigation.
-  Makes it clear to the user how they can access different pages or to return to a previous page without relying on browser forward/back buttons.

### Search bar

- Allows users to search for a specific element on the website, e.g., if they are looking for information on a particular NGO.

### Homepage

- Displays a slideshow of three random NGOs from the directory, above a button to check out more NGOs which takes the user to the directory page. This is above the fold so it is the first thing a user will see when visiting the site.
- Slideshow is over a hero image of a landscape, which clearly relates to the site name 'Friends of Earth' and also to environmental NGOs.
- It also features a short explanation of World NGO Day - when it is and what NGOs are.

### Directory (NGOs) page

- Each page features a brief overview of six different NGOs, including:
    - Name
    - Logo
    - Brief description
    - Internal link to more information on our site
    - External link to the NGO's site (opens in a new tab so the user can easily navigate back to our site)
- The user can navigate between the directory pages by using the 'first', 'previous', 'next' and 'last' buttons at the bottom of the screen.

### Contact page

- Features a short description of reasons a user might want to get in touch with us.
- Provides various contact details - phone number, email address and Google Maps location, as well as links to social media sites.
- User can fill out a form with their contact details and message, which will go to our database and allows us to get in touch with them to reply.
- Contact details and form are over a hero image of the Earth as seen from space, again relating to the site name 'Friends of Earth' but a different take on it, to provide variety and also to focus more on the worldwide/global aspect of the site.

### Random page

- Takes the user to a page with information about a random NGO in our database.

### About us page

- Explains who we are and why our website was created, along with images relating to different types of NGO.

### Footer

- Features Copyright, team name and social media links to feature at the bottom of every page.

### Favicon


# Development choices


# Design choices

## Colour palette

The chosen colour palette is symbolic of the Earth and uses complementing blues, green, grey and white:
![Colour palette](documentation/design/colour-palette.png)

## Font
The chosen font is Montserrat.
The font is white over the darker background of the header and footer, and dark over white and light backgrounds in the main body of each page to make sure it is accessible and can be easily read by users.

# Deployment


# Bugs


# Testing


# Credits