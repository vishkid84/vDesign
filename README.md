<div align="center">
<img src="media/Website_mockup.png" target="_blank" rel="noopener" alt="workspace-showcase">
<h2>workspace-showcase</h2>
</div>

# vDesign

I am a Digital Designer who is expanding his skillset in depth into the web development space. This website is intended as a personal freelance site where I can highlight my work, provide templates and also scribble down snippets of my thoughts as a blog. I Users have the option to get a quick quote for my work depending on their requirements from the Contact page. 

You can find the deployed site [here](https://vdesign.herokuapp.com/)

## Table of Contents

1. [**UX**](#ux)
- [**Strategy**](#strategy)
- [**Scope**](#scope)
- [**Structure**](#structure)
- [**Skeleton**](#skeleton)
- [**Surface**](#surface)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
2. [**Technologies**](#technologies-used)
3. [**Testing**](#testing)
4. [**Deployment**](#deployment)
5. [**Credits & Acknowledgements**](#credits)

## UX

### User stories

As the site admin: 
- One of the main purpose of the site is to showcase my two core skills - PowerPoint design and web design/development
- I need a shopping page to sell already designed PowerPoint and Bootstrap templates for those who are looking for a quick and simple solution
- I need a page to pen down my thoughts about the two areas - PowerPoint and web. This helps in building confidence among users about my skills and also aids in some interaction with the users
- I should have a contact page ready for people looking to ----------
As a user looking for freelancers:
- I need to see the previous work done by the individual to make sure he is capable of meeting my requirements
- I have some basic skills to carry out my work, so if there is anything that helps me to with my work without hiring the person full time, that would be an advantage
- Most of the freelancers need to be contacted to get their rates, if I can get a quick glance at their rates from their website for my requirements, that would be amazing

### Strategy

The idea of the project is to set up a website which serves as a personal portfolio while also helping me generate revenue. This needs to highlight my core skills, how knowledgable I am about those skills and also should be a place where people can hire me for work. 

### Scope

To understand what features needs to be included, I browsed the internet for other similar websites. I had a clear idea about what needs to be included from my side but I had to look at it from a client's perspective as well. For this, I did a quick interview with a couple of previous clients to understand what they would be looking for when searching for a freelancer. Based on all this, I identified these key areas:
1. A visually appealing home page which gives a quick glance at my core skill areas
2. An About page to give some understanding about my bakcgorund and journey
3. A portfolio page to showcase my previous work
4. A shop where users can buy prebuilt PowerPoint and Bootstrap templates
5. A profile page for users to login to update their details, this should also include details about their previous orders if any
6. A blog where I can talk about my thoughts about the two areas. Users should have the ability to add comments to have some level of interaction
7. A contact section for users to get in touch with me
8. A section where a quick quote is generated based on requirements entered by users

### Structure

There are 6 main pages including the home page and a login/registration page. Other than these, there is a base page which serves as the base for all the other pages. 

#### The home page
The home page gives gives a quick glance at my core skill areas and a link to the Portfolio page. 

#### About page

This page talks about who I am, what my background is and my journey till now. 

#### Portfolio page

This page showcases a few of my work in both Presentation Design and Web Development. Users can click into each which gives detailed information about the project and how I handled those with images of the project.

#### Shop page

This page provides a few prebuilt PowerPoint and Bootstrap templates which users can purchase. There is a filter to aid in the search. Once they click into a template, it takes them to a page which provides a bit more information about the template. From here, they can add this to the shopping bag. 

#### Shopping bag page

They can add this to cart and go to checkout or keep adding more products. There is a cart which shows the total which is calculated automatically based on the products they add. They can delete the products if no longer needed from this page or if they need to add more products, there is a button which takes them to the Shop page to buy more templates. Once they have added all the templates to the cart, they can go to the Checkout page by clicking on the Cart. <br>

#### Checkout page

Here the user can enter their billing details to complete the checkout. If they need to update the cart at any point before billing, they have the option to go back to the Shop by clicking on a button. In this page, the users are provided with an option to save their details by logging into the site. If they don't want that option, they can click on Complete Order button to complete the transaction which triggers an automatic mail to their email address provided with the necessary details. If they want to save the details for future, they can register or login from the page or from the navbar. 

#### Login page

The users are provided with the option to register/login to create an account. For new users, they can redirect to the Sign up page from here. They need to include their email address, name and password to sign up. Once that is done, a confirmation link will be sent to their email address. Once the email is confirmed, they can login to the site. Logged in users have the ability to navigate to the Profile page. 

#### Profile page

The logged in users can update their billing details from this page. If they have made any previous purchases, those details are also shown in this page. 

#### Logout page

For users logged in, they can click on the logout button which takes them to this page to confirm that they need to logout. Clicking on the Sign out button logs them out from the site. 

#### Blog page

This page as the name suggests consists of a list of blogs written by the admin. Users can search for a blog by entering the keyword. The latest 3 blog posts are also highligted in this page, this option is only available in bigger screens and not in mobiles. Users can click into each blog to read the blog. Logged in users have the option to add comments. If they have previously added any comment, they can edit or delete their own comments.  

#### Contact page

This page provides a form which they can fill in to contact me. It also provides an emai address and phone number for contact if they dont want to use the form. 
This page provides a quote section where the users are given the option for a quick quote by filling in their requirements. 

#### Quote section

There are two buttons in this section - Presentation Design quote and Web Develpoment quote. The Web Development quote is currently in progress and just takes them to a page mentioning that. The Presentation Design quote button when clicked on takes them to a form where in they can enter their name, project name and has a multiselect form with a few requirements. Once the selection is made they can click Submit which generates a quote for them based on their requirements. Once the submit button is clicked, it takes them to a page a page with the lates quotes listed. From here, they can click on their project named button to view the quote. 

#### Management section

This section is available only for admin. This is a dropdown button in the navbar, when clicked on provides with three options 
1. Add a template - To add a new template to the Shop section
2. Add portfolio - To add a new work to the portfolio
3. Add blog - To add a new blog


### Skeleton

You can see the wireframes saved as pdf below:

[Wireframe for desktop](/wireframes/Wireframe_desktop.pdf)<br>
[Wireframe for tablet](/wireframes/Wireframe_tablet.pdf)<br>
[Wireframe for mobile](/wireframes/Wireframe_mobile.pdf)

