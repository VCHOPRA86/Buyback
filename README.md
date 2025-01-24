# Milestone Four

## Code Institute: Milestone Project 4 - Full Stack Development

## **CashThatGadget** - Buyback Recommerce Platform  

### [Live Site]()

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
![Responsive Site Example]()

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
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  * [Content](#content)
  * [Code](#code)

---

# User Experience  

## User Stories  

### Customer Stories  

1. **Search Functionality**: As a customer, I want to search for my gadget quickly so I can start the selling process efficiently.  
2. **Dynamic Pricing**: As a customer, I want to see prices update dynamically based on the condition and storage size, enabling me to make an informed decision.  
3. **Order History**: As a customer, I want access to my order history and the ability to reprint postage labels for convenience.  

### Site Owner Stories  

1. **Product Management**: As a site owner, I want to manage products, categories, and storage options to cater to a wide variety of devices.  
2. **Revised Offers**: As a site owner, I want to send custom revised offers with explanations to maintain transparency and resolve issues efficiently.  

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

### Mockups  

**Desktop Design**  
[Home Page Design](wireframes/Desktop-Mock-Up.jpg)  

**Mobile Design**  
[Home Page Design](wireframes/Mobile-Mock-Up.jpg)  

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

## APIs Used  

- [ShipEngine](https://www.shipengine.com/): Prepaid postage label integration.  

---

# Testing  

Details about testing can be found [here](TESTING.MD).  

---

# Deployment  

Instructions on local and live deployment can be found in the full documentation.  

---

# Credits  

### Content  
All content was written and developed by the project creator.  

### Code  
Resources for inspiration and debugging include:  
- [CSS Tricks](https://css-tricks.com/)  
- [Stack Overflow](https://stackoverflow.com/)  

---
