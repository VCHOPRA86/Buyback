# Milestone Four

## Code Institute: Milestone Project 4 - Full Stack Development

## **CashThatGadget** - Buyback Recommerce Platform  

### [Live Site](https://cashthatgadget-6181349c7e0a.herokuapp.com/)

---

## Overview

**CashThatGadget** is a buyback recommerce platform built with Django. It allows users to sell gadgets such as mobile phones, tablets, laptops, and gaming consoles. Designed for simplicity and efficiency, the platform provides a seamless experience for both customers and administrators with robust features for dynamic pricing, product management, and order handling.

---

## Project Goal

The primary goal of **CashThatGadget** is to create a user-friendly platform that simplifies the process of selling used gadgets. By offering competitive pricing, advanced features, and intuitive tools, the platform seeks to foster customer trust while enabling scalable business growth.

The repository containing the website's source code and assets is available at:  
[Code Repository]()

The site was developed with a responsive design, ensuring usability across desktop, tablet, and mobile devices.  
**Preview Example:**  
![Responsive Site Example](Docs/readme/cashthatgadget_mockup.png)

---

# Table of Contents

- [User Experience](#user-experience)
  * [User Stories](#user-stories)
    + [Customer Stories](#customer-stories)
    + [Site Owner Stories](#site-owner-stories)
- [Site Features](#site-features)
  * [Current Features](#current-features)
  * [Future Features](#future-features)
- [UX/UI Design](#ux-ui-design)
- [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries, and Programs](#frameworks-libraries-and-programs)
  * [APIs Used](#apis-used)
- [Why I Chose Certain Tools and Technologies](#Why-I-Chose-Certain-Tools-and-Technologies)
- [Testing](#testing)
- [Deployment](#deployment)
- [Resources Used](#resources-used)
- [Credits](#credits)
  * [Content](#content)
  * [Code](#code)

---

# User Experience  

## User Stories  

### Customer Stories  

1. **Search Functionality**: - **As a customer**, I want to search for my gadget quickly so I can start the selling process efficiently.  
2. **Dynamic Pricing**: - **As a customer**, I want to see prices update dynamically based on the condition and storage size, enabling me to make an informed decision.
3. **Easy Checkout**: - **As a customer**, I want a quick and simple checkout process so that I can complete my sale with minimal effort.
4. **Order History**: - **As a customer**, I want access to my order history and the ability to reprint postage labels for convenience.
5. **Multiple Payment Options:** - **As a customer**, I want to choose from various payment methods (e.g., PayPal, bank transfer) to complete my transaction in the way that works best for me.
6. **Notifications and Updates:** - **As a customer**, I want to receive notifications about the status of my sale (e.g., gadget received, payment processed) so I’m always informed.

### Site Owner Stories  

1. **Product Management**: - **As a site owner**, I want to manage products, categories, and storage options to cater to a wide variety of devices.
2. **Order Management**: - **As a site owner**, I want to view, manage, and process customer orders so that I can efficiently handle multiple sales at once.
3. **Order Status Management:** - **As a site owner**, I want to manage and update the status of orders with options like Awaiting Delivery, Received, Processed, Completed, Expired, Problem, Quarantined, Accepted, Rejected, Returned, and Cancelled so I can keep track of the order lifecycle and provide accurate updates to customers.
4. **Trade-in Value Tracking**: - **As a site owner**, I want to track the total trade-in values for customers so I can monitor overall sales and better understand customer transactions.
5. **Counter Offer Functionality**: - **As a site owner**, I want an easy-to-use admin interface for sending counter offers to customers, allowing me to adjust offers based on device condition and market trends, ensuring fair negotiations.
6. **Revised Offers**: - **As a site owner**, I want to send custom revised offers with explanations to maintain transparency and resolve issues efficiently.
7. **Maintenance Page**: - **As a site owner**, I want a dedicated maintenance page so I can easily make changes, updates, or perform site maintenance without disrupting user experience.
8.  **Prepaid Postage / Seller-Paid Postage Option**: - **As a site owner**, I want to have the option of either offering a free prepaid postage option or require the customer to pay for postage, depending on the business, to help keep costs down when setting up a free postage service, providing flexibility in my services.
9.  **Order History Overview:** **As a site owner**, I want to quickly view a comprehensive overview of all customer orders, including status, values, and any actions taken, to monitor platform performance efficiently.

---

# Site Features  

## Current Features  

### User Features  

1. **Dynamic Pricing**:  
   - Product prices update automatically based on storage size (e.g., 64GB, 128GB, 1TB) and device condition (Working or Faulty).  

2. **Search Suggestions**:  
   - A real-time search bar narrows results dynamically.  
   - Example: Typing "iPhone" displays all relevant models.  

3. **Product Options**:  
   - Customers can select options for working/faulty conditions, network compatibility, and storage size.  

4. **Customer Dashboard**:  
   - Displays order history with options to:  
     - Reprint postage labels.  
     - Accept or reject revised offers (e.g., due to missing accessories).  

5. **Payment Options**:  
   - Customers can choose bank transfer or PayPal for payouts, offering flexibility and security.  

6. **Postage Options**:  
   - Free prepaid postage via ShipEngine or customer-paid shipping options.  

7. **Contact Form**:  
   - Messages are emailed directly to the admin and stored in the admin panel for tracking and improved communication.  

### Admin Features  

1. **Product Management**:  
   - Admin can add, edit, and delete brands, categories, and products.  
   - Custom storage options (e.g., 128GB, 256GB, 1TB) are supported.  
   - Separate pricing for working and faulty devices, with customizable descriptions for clarity.  

2. **Order Management**:  
   - Status updates include: Awaiting Delivery, Received, Processed, Completed, Expired, Problem, Quarantined, Accepted, Rejected, Returned, Cancelled.  
   - Track total trade-in values for customers.  

3. **Counter Offer Functionality**:  
   - Admins can revise offers with custom messages explaining price changes (e.g., missing accessories).  
   - Customers can accept/reject counter-offers via their dashboard.  

4. **Email Templates**:  
   - Admin can customize email templates using CKEditor for better communication.  

5. **Postage Settings**:  
   - Toggle prepaid or customer-paid postage options.  

6. **Maintenance Mode**:  
   - Enable/disable site maintenance mode with a single toggle.  

7. **Enhanced Admin UI (Jazzmin)**:  
   - A modern, intuitive admin interface for streamlined management.  

---

## Future Features  

1. **Real-Time Price Updates**:  
   - Integrate with external APIs (e.g., Amazon) to adjust prices dynamically based on market trends.  
   - Ensures competitive pricing by fetching live data.  

2. **Coupons/Voucher Codes**:  
   - Allows customers to redeem discounts, fostering loyalty and repeat business.  

3. **Affiliate Program**:  
   - Introduce referral incentives to attract new users through existing customers.  

---

# UX/UI Design  

## Mockups  

### Desktop Design

#### General Pages:
- [Home Page Design](ui/ux/Homepage.png)
- [Sell My Gadgets](ui/ux/Sell_mobile-gadget.png)  
- [How It Works](ui/ux/How_it_works.png)  
- [Why Use Us](ui/ux/Why_use_us.png)  
- [Support](ui/ux/Support.png)
- [Contact Us](ui/ux/Contact.png)

#### Authentication Pages:
- [Login](ui/ux/login.png)
- [Signup](ui/ux/signup.png)

#### Checkout Flow:
- [Cart](ui/ux/Checkout_flow/Review-cart-sale.png)
- [Checkout](ui/ux/Checkout_flow/Confirm_sale.png)
- [Checkout Success - Paid Postage Option](ui/ux/Checkout_flow/checkout-success-paid-postage-option.png)
- [Checkout Success - Prepaid Postage Option](ui/ux/Checkout_flow/checkout-success-prepaid-postage-option.png)

#### User Dashboard:
- [User Dashboard](ui/ux/User_account_dashboard/User-Dashboard.png)
- [User Edit Details](ui/ux/User_account_dashboard/User-edit-details.png)
- [User Order Details](ui/ux/User_account_dashboard/User-order-details.png)
- [User Password Change](ui/ux/User_account_dashboard/User-password-change.png)

---

### Mobile Design

#### General Pages:
- [Home Page Design](ui/ux/mobile/Homepage.png)
- [Sell My Gadgets](ui/ux/mobile/Sell_my_gadget.png)  
- [How It Works](ui/ux/mobile/How_it_works.png)  
- [Why Use Us](ui/ux/mobile/Why_use_us.png)  
- [Support](ui/ux/mobile/Support.png)
- [Contact Us](ui/ux/mobile/Contact.png)

#### Authentication Pages:
- [Login](ui/ux/mobile/login.png)
- [Signup](ui/ux/mobile/signup.png)

#### Checkout Flow:
- [Cart](ui/ux/mobile/Checkout_flow/Review-cart-sale.png)
- [Checkout](ui/ux/mobile/Checkout_flow/Confirm_sale.png)
- [Checkout Success - Paid Postage Option](ui/ux/mobile/Checkout_flow/checkout-success-paid-postage-option.png)
- [Checkout Success - Prepaid Postage Option](ui/ux/mobile/Checkout_flow/checkout-success-prepaid-postage-option.png)

#### User Dashboard:
- [User Dashboard](ui/ux/mobile/User_account_dashboard/User-Dashboard.png)
- [User Edit Details](ui/ux/mobile/User_account_dashboard/User-edit-details.png)
- [User Password Change](ui/ux/mobile/User_account_dashboard/User-password-change.png)

---

# Technologies Used  

## Languages Used  

- [HTML5](https://en.wikipedia.org/wiki/HTML5)  
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)  
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)  
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))  

## Frameworks, Libraries, and Programs  

- [Django](https://www.djangoproject.com/): Backend framework for building the platform.  
- [CKEditor](https://ckeditor.com/): Rich text editor for email and product description customization.  
- [Jazzmin](https://django-jazzmin.readthedocs.io/): Enhances admin UI with modern styling.
- [Whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html):Serves static files directly in production without requiring a separate web server.    
  

## APIs Used  

- [ShipEngine](https://www.shipengine.com/): Prepaid postage label integration.
- [Cloudinary](https://cloudinary.com/): Manages and delivers media assets with automatic optimization, ensuring fast loading times and scalable performance. 

---

# Why I Chose Certain Tools and Technologies

I selected Cloudinary and WhiteNoise for the project instead of using AWS for a few key reasons. Both solutions fit the specific needs of my project, offering a more streamlined setup without unnecessary complexity.

- **Cloudinary**: For handling media uploads, Cloudinary was the most suitable choice due to its simplicity and ease of integration with Django. I didn't need the full set of services offered by AWS S3, and Cloudinary provides an efficient, user-friendly way to handle image and file uploads while offering powerful features like automatic resizing and format conversion. This saved me a lot of time on both development and setup, which was critical for this project.

- **WhiteNoise**: For static file management, WhiteNoise was a better option compared to other complex solutions like Amazon S3 or custom server setups. WhiteNoise seamlessly integrates with Django, allowing static files to be served efficiently, even when deployed to platforms like Heroku. It’s also a lightweight solution that requires minimal configuration, and it served my purpose of delivering static files quickly without needing a more heavyweight solution.

These tools were chosen for their simplicity, ease of integration, and ability to provide robust features without overcomplicating the setup from services like AWS.


# Testing  

Details about testing can be found [TESTING.MD](Docs/TESTING.MD).  

---

# Deployment  

Instructions on local and live deployment can be found in the full documentation [here](Docs/DEPLOYMENT.md).   

---

# Resources Used

### Tutorials Followed


- [Jazzmin Setup](https://www.youtube.com/watch?v=zx4LSW0QBq0)  

- [Cloudinary Integration](https://www.youtube.com/watch?v=gj8bs2lf86A)

- **Maintenance Mode:** Referenced [django-maintenance-mode](https://github.com/fabiocaccamo/django-maintenance-mode) but implemented a custom version.

# Credits  

### Content  
All content was written and developed by me.

### Code  
Resources for inspiration and debugging include:  
- [CSS Tricks](https://css-tricks.com/)  
- [Stack Overflow](https://stackoverflow.com/)  

---
