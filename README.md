# **CineCritic - The house of tasteful cinema critique!**

## **Introduction**

CineCritic is a profile based movie review web application dedicated to movie enthousiasts that enjoy sharing thoughts around their favorite films.

*Welcome to [CineCritic](https://cine-critic-0310d8ee3de7.herokuapp.com/)*

![CineCritic mockup](static/images/readme/cine-critic-mockup.png)

# **Contents**

- [**CineCritic - The house of tasteful cinema critique!**](#cinecritic---the-house-of-tasteful-cinema-critique)
    - [**Introduction**](#introduction)
- [**Contents**](#contents)
- [**User Experience (UX)**](#user-experience-ux)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
    - [**Site Structure**](#site-structure)
  - [**Design**](#design)
- [**Features**](#features)
  - [**Existing features**](#existing-features)
- [**Technologies Used**](#technologies-used)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
- [**Acknowledgements**](#acknowledgements)

  

# **User Experience (UX)**

## **User Stories**

- User Authentication:
    - As a new user, I want to be able to create a user profile with a unique username and password, so that I can access app features.
    - As a new user, I want a user-friendly registration page with clear formatting rules for my creadetials.
    - As a registered user, I want to be able to log in securely using my username and password, so that I can access my account and its features.
- User Profile:
    - As a user, I want to have a dedicated profile page with all my reviews, so that I have immediate access to my personal user ativity.
- Movie Management:
    - As a user, I want to be able to search for movies from an external API using keywords, so that I can find movies to review.
    - As a user, I want to be able to automatically retrieve details for the movies I am reviewing, so that I have a clear idea of the film I am discussing.
    - As a user, I want to be able to see a list of all movies added to the app, so that I can browse through them.
    - As a user, I want movies without any review to be automatically removed from the movie list, so I am aware of the films already reviwed in the app.
- Review Management:
    - As a user, I want to be able to add a review for a movie, so that I can share my thoughts and opinions with other users.
    - As a user, I want to be able to view all reviews for a specific movie, so that I can see what other users have said about it.
    - As a user, I want to be able to update or edit my own review for a movie, in case I want to make any changes.
    - As a user, I want to be able to delete my own review for a movie, if I no longer want it to be visible on the app.
- Upvoting/Downvoting:
    - As a user, I want to be able to upvote or downvote a review made by another user based on my preference, so that I can show my appreciation for it.
    - As a user, I want to be limited to upvoting/downvoting each review only once, to ensure fair voting.
- Admin User:
    - As an admin user, I want to have access to all reviews added in the application, so that I can efficiently manage any potential unwanted activity such as offensive reviews.
- Additional Features:
    - As a user, I want to be able to access the IMDB page of a movie directly from the app, so that I can learn more about it.
    - As a user, I want the app to have a responsive design, so that I can use it seamlessly on different devices.

  
[Back to top](<#contents>)

## **Wireframes**

The wireframes for ArtMatch were produced in [Balsamiq](https://balsamiq.com). Inclued below, frames can be found for all distinct pages (home, rules, board) in desktop, mobile and tablet view as they were initially envisioned.

- Home Page

    - *Laptop*

    ![Laptop](static/images/readme/wireframe-laptop.png)

    - *Tablet*

    ![Tablet](static/images/readme/wireframe-tablet.png)

    - *Mobile*
    
    ![Mobile](static/images/readme/wireframe-mobile.png)

- Login/Register Page

    - *login/Register*

    ![Login/REgister](static/images/readme/login-register-page-wireframe.png)

- Profile Page

    - *Profile*

    ![Profile](static/images/readme/profile-wireframe.png)
  

- Movie Card Page

    - *Movie Card*

    ![Movie Card](static/images/readme/movie-card-wireframe.png)

- Add/Edit Review Page

    - *Add/Edit Review*

    ![Add/Edit Review](static/images/readme/add-review-wireframe.png)

[Back to top](<#contents>)

## **Site Structure**

The site consists of 7 main pages (plus a [404](https://cine-critic-0310d8ee3de7.herokuapp.com/404) error page) with the main landing page being the [movies_list](https://cine-critic-0310d8ee3de7.herokuapp.com) where registered and unregistered users can see a list of the movies being reviewed in the app. The user can either click on a movie to see details about the movie and reviews written by other users in the movie_card page, or they can use the navigation links on the side to [login](https://cine-critic-0310d8ee3de7.herokuapp.com/login) or [register](https://cine-critic-0310d8ee3de7.herokuapp.com/register).
Once logged in, a user can now access more pages, such as the [add_movie](https://cine-critic-0310d8ee3de7.herokuapp.com/search) page, where they can add a new movie to review by requesting the movie from the [OMDB](https://www.omdbapi.com) API to review. Additionally, a user can visit their profile page, where they can see all their reviews, visit specific movie cards and edit their reviews or delete them.

Some pages are not linked since they require specific permissions or are subject to constant change.

[Back to top](<#contents>)

## **Design**

- *Typography*

All text on the website is using a variation of the "Mulish" font family found on [Google Fonts - Mulish](https://fonts.google.com/specimen/Mulish)

- *Colour palette*

The color pallete chosen for the website consists of four main colors: Bone, Liver Chestnut (Horses), White Coffee and Platinum. All colors are solf and pale to profide for a calming, elegant and welcoming experience.

![CinCritic - Colour Pallete](static/images/readme/color-palette.png)

[Back to top](<#contents>)

# **Features**

The CineCritic wesite is designed to be simple to navigate and easy to use. It includes a variety of features to support a profile based experience, CRUD functionality for reviews and extenral API requests to a movie database.

## **Existing features**

- ### **Navigation Menu**

    Can be found on the side of all pages of the website pages below the logo. Makes navigation through pages easy and intuitive.
    The navigation menu is fully responsive to accomodate users of all decvces. The active page is always highlighted. All other menu items are changing color when hovered over to increase usability.

    - *Navigation Menu*

        ![Navigation Menu](static/images/readme/nav.png)

- ### **User Profiles**

    Users can create a personalized profile on CineCritic by registering with a unique username and password. This feature enables users to access exclusive content, CRUD functionality for movie reviews and interact with the community. The login interface allows existing users to securely sign in to their accounts, while the registration form enables new users to create an account by providing necessary details.

    - *login*

        ![Login](static/images/readme/login.png)

    - *Register*

        ![Register](static/images/readme/register.png)
    
    - *Admin User*

        An admin user has access to an exclusive admin profile where they can monitor all reviews made on the website. This includes the ability to view, edit, delete, and create reviews as necessary, providing comprehensive control over user-generated content.

        - *Admin*

            ![Admin](static/images/readme/admin.png)
    
    - *Profile Page*

        - *Personalized Profile Page*

            Each user has their own personalized profile page where they can view a comprehensive list of all their reviews. This page serves as a centralized hub for users to manage and track their contributions to the platform.
        
        - *Review Details and Edit Mode*

            Users have the ability to access additional details and enter edit mode for each review. By clicking on a specific review entry, users are redirected to the movie card page corresponding to their particular review. Here, they can view comprehensive information about the movie and make edits to their review if necessary.
        
        - *Profile Page*

            ![Profile Page](static/images/readme/admin.png)

- ### **Movie Card**

    The movie card page provides comprehensive details about a specific movie, including its title, plot synopsis, director, actors, release year, and other relevant information. Additionally, users can view a list of all reviews submitted for that particular movie. Furthermore, users can edit/delete their own reviews as weill as upvote or downvote reviews created by other users. Last but not least, a user can redirect themselves to IMDB page of the specific movie they are looking for in order to access more infomation about it.

    - *Movie Card*

        ![Movie Card-movie](static/images/readme/movie-card.png) 
        ![Movie Card-reviews](static/images/readme/movie-card1.png) 

- ### **Header and Footer**

    - *Header*

        The header section of the website contains the name and slogan, providing users with a quick and clear identification of the website. This minimalistic design approach ensures that the header remains uncluttered and focused on conveying the core identity of the platform.
    
    ![Header](static/images/readme/header.png)
    
    - *Footer*

        The footer section of the website displays credits, acknowledging the contributors and creators of the platform. This section serves as a gesture of appreciation towards those who have contributed to the development and maintenance of the website.
    
    ![Footer](static/images/readme/footer.png)


- ### Reviewing A Movie**

    - **Movie Search and Database Integration**

        Users can search for movies by title through an integrated communication with an external movie API - OMDB (Open Movie Database). Upon finding the desired movie, users can add it to the website's database along with essential details like plot synopsis, director, actors, poster image, and year of release. 

        - *Search and Add Movie*

            ![Search and Add Movie](static/images/readme/search.png)
    
    - **Review Functionality**

        Once a movie is added to the database, users can review it. All users have the ability to review movies listed on the website. Users can share their opinions, ratings, and comments, contributing to the community's collective feedback on the movie. Movies with no reviews will automatically be removed from the database.

        - *Review a Movie*

            ![Review a Movie](static/images/readme/add-review.png)
    
    - **User Review Management**

        Users have control over their own reviews. They can edit or delete their reviews as needed, allowing them to update their opinions or remove outdated content. Additionally, users can interact with reviews from other users by upvoting or downvoting them, expressing their agreement or disagreement with the provided feedback.

        - Edit/Delete Review

        - Upvote/Downvote Review

        - *Review a Movie*

            ![Review a Movie](static/images/readme/edit-review.png)


[Back to top](<#contents>)

# **Technologies Used**

- [Python](https://www.python.org) - backend
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - templating framework
- [MongoBD](https://www.mongodb.com) - database
- [HTML5](https://html.spec.whatwg.org) - content and structure of the website via templating
- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) - styling
- [JavaScript](https://www.w3schools.com/js/) - browser functionality
- [OMDB](https://www.omdbapi.com) -  movie db extrenal API
- [Wireframe.cc](https://wireframe.ccm) - wireframes
- [GitHub](https://github.com) - hosting and storing
- [Heroku](dashboard.heroku.com) - deployment
- [Gitpod](https://gitpod.io/) - coding workspace
- [GIMP](https://www.gimp.org) - image editing
  
[Back to top](<#contents>)

# **Testing**

Please follow this [link](./TESTING.md) to learn more about testing CineCritic.

[Back to top](<#contents>)

# **Deployment**

### **Project Deployment Instructions**

This website is deployed on Heroku pages. Follow these steps to deploy a project:

- **Local Setup**

    - **Clone the Project:** Log in to GitHub, navigate to the repository, and click on the "Code" button. Select "Open with GitHub Desktop" and follow the instructions to clone the repository locally.
    - **Install Requirements:** In your local workspace, open a terminal window and navigate to the project directory. Use the command pip3 install -r requirements.txt to install all necessary dependencies.
    - **Set Up MongoDB:** Sign up or log in to your MongoDB account. Create a cluster and a database, then create four collections: categories, recipes, subscribers, and users. Populate these collections with the appropriate string values according to the project's Information architecture.
    - **Create Environment Variables:**
        - Create a .gitignore file in the project's root directory.
        - Add env.py to the .gitignore.
        - Create the env.py file and define the required environment variables using the os module.
    - **Run the App:** In your terminal window, run the command python3 app.py to start the application locally.

- **Heroku Deployment:** 

    - **Set Up Local Workspace for Heroku:**

        - Generate requirements.txt by running pip3 freeze --local > requirements.txt.
        - Create a Procfile specifying the entry point for Heroku using the command python app.py > Procfile.
    
    - **Set Up Heroku:**

        - Create a Heroku account and a new app, selecting your preferred region.
        - Choose the "GitHub" deployment method and connect your repository to Heroku.
    
    - **Configure Environment Variables:**

        - In Heroku, navigate to the app's settings and find "Config Vars."
        - Enter the variables from your env.py file: IP, PORT, SECRET_KEY, MONGO_URI, and MONGO_DBNAME.
    
    - **Push Files to Repository:**

        - Add and commit requirements.txt and Procfile to your Git repository.
    
    - **Automatic Deployment:**

        - In the Heroku dashboard, go to the deploy tab and enable automatic deployments.
        - Heroku will fetch the code from GitHub and deploy the app using the specified packages. 
        - Click "Open app" to access the live version.

  You can access the live link to the GitHub deployed version - [https://cine-critic-0310d8ee3de7.herokuapp.com](https://cine-critic-0310d8ee3de7.herokuapp.com)


[Back to top](<#contents>)

# **Credits**

- Font: [Google Fonts](https://fonts.google.com)
- Icons: [Fontawesome](https://fontawesome.com)
- Movie DB: [OMDB](https://www.omdbapi.com)
- Logo: [LOGO](https://logo.com)
- Wireframes: [Wireframe.cc](https://wireframe.cc)
- Image Editing: [GIMP 2.10.34](https://www.gimp.org)
- Color Palette: [Coolors](https://coolors.co)
- GeeksForGeeks: [geeksforgeeks](https://www.geeksforgeeks.org/python-404-error-handling-in-flask/)
- StackOverflow: [Yann Dìnendal](https://stackoverflow.com/questions/13643417/how-to-validate-pattern-matching-in-textarea)


[Back to top](<#contents>)

# **Acknowledgements**

This website was developed as a part of my Portfolio 3 Project for the Web Application Developemnt Diploma at the [Code Institute](https://codeinstitute.net/). I want to express my gratitude to my mentor, [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/), as well as the Slack community and everyone at the Code Institute for their valuable assistance and support throughout this project.

Sergios Papastergiou
2024