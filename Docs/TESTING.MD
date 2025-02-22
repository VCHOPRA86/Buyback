
# CashThatGadget: Project Overview & Testing Documentation

The CashThatGadget website has been tested using the following methods:

## Table of Contents
- [Overview of the Project](#overview-of-the-project)
- [Key Features](#key-features)
- [Development Process](#development-process)
  - [Project Planning & Requirements Analysis](#1-project-planning--requirements-analysis)
  - [Project Setup & Environment Configuration](#2-project-setup--environment-configuration)
  - [Order Status Management](#3-order-status-management)
  - [Revised Offer Price Handling](#4-revised-offer-price-handling)
  - [4-Step Process](#5-4-step-process)
  - [Admin Panel Features with Jazzmin Integration](#6-admin-panel-features-with-jazzmin-integration)
- [Testing Documentation](#testing-documentation)
  - [Code Validation](#code-validation)
    - [W3C HTML Validator](#w3c-html-validator)
    - [W3C CSS Validator](#w3c-css-validator)
    - [JSHint JavaScript Code Quality Tool](#jshint-javascript-code-quality-tool)
    - [Python Validation using VSCode](#python-validation-using-vscode)
  - [Lighthouse](#lighthouse)
  - [Responsiveness](#responsiveness)
  - [Browser Compatibility](#browser-compatibility)
  - [Testing User Stories](#testing-user-stories)
    - [First-Time User](#first-time-user)
    - [Returning User](#returning-user)
    - [Business Owner](#business-owner)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Peer Review](#peer-review)
- [Bugs & Fixes](#bugs--fixes)
  - [Payments & Cart](#payments--cart)
  - [Profile Dashboard & Admin](#profile-dashboard--admin)
- [Conclusion](#conclusion)

---
## Overview of the Project
The **CashThatGadget** website is a user-friendly platform designed to help users sell their unwanted gadgets for cash. The platform simplifies the process into four easy steps: registering a sale, obtaining free postage/seller paid, sending the gadget, and receiving payment securely via bank transfer or PayPal. The project also includes a robust admin panel for managing orders, revising offers, and tracking order statuses.

## Key Features
1. **User-Friendly Workflow**: A seamless 4-step process for selling gadgets.
2. **Order Status Updates**: Real-time tracking of order statuses (e.g., Awaiting Delivery, Received, Processed, Completed).
3. **Pricing Flexibility**: Admins can revise the offer price based on gadget condition.
4. **Payment Options**: Secure payments via bank transfer or PayPal.
5. **Admin Panel**: Comprehensive tools for managing orders, updating statuses, and processing payments.
6. **Security**: Secure login and registration for both customers and admins.


## Development Process

### 1 **Project Planning & Requirements Analysis**
The development process began with a thorough analysis of the core functionalities required for the platform. Key requirements included:
- **Order Management**: A system to manage gadget sales from submission to payment.
- **Order Status Tracking**: Real-time updates for customers and admins to track the progress of each transaction.
- **Payment Processing**: Secure and flexible payment options for customers.
- **Admin Tools**: A comprehensive admin panel for managing orders, revising prices, and processing payments.

### 2 Project Setup & Environment Configuration
- A Django project was initialized with **Python 3.8** as the initial development environment. However, during the deployment phase, it was discovered that **Heroku no longer supported Python 3.8** as it had been deprecated. To resolve this, the project was upgraded to **Python 3.9**, which was the stable version supported by Heroku at the time.
- The environment was configured with necessary settings for security, database management, and deployment. This included setting up a virtual environment, installing dependencies, and configuring the `requirements.txt` file.
- Key dependencies such as **Django REST Framework**, **payment processing libraries**, and **email handling tools** were installed to support the platform's core functionalities.

### 3 **Order Status Management**
The order status system was designed to provide transparency for both customers and admins. Key statuses included:
- **Awaiting Delivery**: The gadget has not yet been received
- **Received**: The gadget has been received and is undergoing inspection.
- **Processed**: The gadget has been inspected, and its value is confirmed.
- **Completed**: Payment has been successfully processed.
- **Problem**: Problem with the order.
- **Rejected**: The gadget is not accepted for buyback.
- **Quarantined** IMEI flagged as blocked, lost or stolen.
- **Expired** We never recived your Gadget(s) - 14 days.
- **Rejected** Your order has been rejected.

Each status change triggers notifications to the customer, ensuring they are always informed about their order.

### 4 **Revised Offer Price Handling**
A key feature of the platform is the ability to revise the offer price based on the gadget's condition after inspection. The admin panel allows admins to:
- Adjust/revise the offer price.
- Provide a reason for the revision.
- Notify the customer of the revised offer.

Customers can then choose to accept or reject the new offer in their account dashboard or have their gadget returned.

### 5 **4-Step Process**
The platform guides users through a simple 4-step process:
1. **Register Sale**: Users select the category, brand & then product.
2. **Get Free Postage**: A prepaid postage label is generated for the user.
3. **Post Your Gadget**: The user sends the gadget.
4. **Get Fast Payment**: Payment is processed upon completion of the sale.

### 6 **Admin Panel Features with Jazzmin Integration**
The admin panel of this project has been customized using Jazzmin to improve the user experience, especially for site owners who need an intuitive and modern interface to manage various operations efficiently. Unlike the default Django admin, which can be a bit outdated and cumbersome, Jazzmin offers a more user-friendly and visually appealing design. This makes it easier for admins to navigate through the admin tools.

Key features enabled through Jazzmin include:
- **Customer Accounts** A list of users for easy account management.
- **View Orders**: A list of all orders with details such as order number, customer name, gadget description, number of trade-ins & status.
- **Update Status**: Admins can update the status of any order.
- **Revise Offers**: Admins can adjust the offer price and notify customers.
- **Process Payments**: Admins can mark orders as completed and process payments.
- **Contact Submissions** Contact submissions can be viewed and managed
- **Email templates** Email templates can be customised for order statuses
- **Brands** Brands can be added, edited or delected
- **Categories** Categories can be added, edited or deleted
- **Storage Options** Different storage options can be added
- **Global Settings** Where admins can activate the maintenance page and toggle postage options. Both have been activated through Heroku for demonstration purposes.

---
# Testing Documentation

## Code Validation

### W3C HTML Validator
The HTML code of the CashThatGadget website has been validated using the W3C HTML Validator. All pages passed without any critical errors or issues.

### Home Page
<h2 align="center"><img src="html-validation/Homepage.png"</h2>

### Sell My Gadget Page
<h2 align="center"><img src="html-validation/sell_my_gadget.png"</h2>

### How It Works Page
<h2 align="center"><img src="html-validation/How_it_works.png"</h2>

### Why Use Us Page
<h2 align="center"><img src="html-validation/why_use_us.png"</h2>

### Support Page
<h2 align="center"><img src="html-validation/support.png"</h2>

### Contact Us Page
<h2 align="center"><img src="html-validation/contact_us.png"</h2>

### Login Page
<h2 align="center"><img src="html-validation/login.png"</h2>

### Sign up Page
<h2 align="center"><img src="html-validation/sign_up.png"</h2>

### W3C CSS Validator
The CSS code has been validated using the W3C CSS Validator. The site passed all checks and there are no major CSS validation issues.

### base.css
<h2 align="center"><img src="css-vaildation/base-css.jpg"</h2>

### mediaqueries.css
<h2 align="center"><img src="css-vaildation/mediaqueries-css.jpg"</h2>

### JSHINT Javascript Code Quality Tool
JavaScript code quality has been validated using **JSHint**. No major issues were detected, ensuring that the scripts follow best practices.

### Python Validation using VSCode
The Python code was validated using VSCode. Python linting tools like **Pylint** and **Flake8** were used to ensure code quality, and there were no major issues reported.

## Lighthouse
Lighthouse was used to evaluate the website's performance, accessibility, SEO, and best practices. The website scored highly on performance and accessibility, with suggestions for further improvements.

### Homepage
<h2 align="center"><img src="lighthouse/homepage-desktop.png"</h2>

<h2 align="center"><img src="lighthouse/homepage-mobile.png"</h2>


## Responsiveness
The website was tested across various screen sizes to ensure it is fully responsive. All elements adjust properly, providing a seamless experience on desktops, tablets, and mobile devices.

## Browser Compatibility
The website was tested across multiple browsers, including:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

The website functions correctly in all major browsers without issues.

Responsivity tests were carried out using Google Chrome DevTools. Device screen sizes covered include:
- iPhone SE
- iPhone XR
- iPhone 12 Pro
- Pixel 5
- Samsung Galaxy S8+
- Samsung Galaxy S20 Ultra
- iPad Mini
- iPad Air
- Surface Pro 7
- Surface Duo
- Galaxy Fold
- Samsung Galaxy A51/71
- Nest Hub
- Nest Hub Max

I also personally tested the website on Cubot kingkong, Dell XPS 15 laptop and a Dell widescreen monitor.

## Testing User Stories

### First Time User
- **Test Case**: Visiting the site for the first time as a new user.
- **Expected Outcome**: The user should be able to easily navigate the site, register a sale, and post their gadget.

### Returning User
- **Test Case**: Logging into the site as a returning user.
- **Expected Outcome**: The user should be able to seamlessly log in and proceed with their sale process.

### Business Owner
- **Test Case**: Business owners should be able to manage their listings, monitor sales, and update their profile settings.
- **Expected Outcome**: All features work as expected without issues.

## Manual Testing
The site underwent manual testing to identify edge cases, user interaction patterns, and potential usability improvements. Testing focused on form submissions, navigation, and content display.

## 1. Login Process:
- **Test Objective:** Ensure users can log in to their accounts successfully.
- **Test Steps:**
  1. Navigate to the login page.
  2. Enter valid credentials (username/email and password).
  3. Click the "Login" button.
  4. Verify the user is redirected to the dashboard or homepage of product detail page (depending on authentication flow).
- **Edge Case Testing:**
  - **Invalid Credentials:** Tested with incorrect credentials (e.g., wrong password) and verified that an error message is displayed.
  - **Empty Fields:** Tested by submitting the form with empty fields and ensured the appropriate error message ("Please fill in fields") appears.
  - **Password Reset Flow:** Tested the "Forgot Password" link, confirming that the user can request a password reset email and follow the instructions.
- **Result:** Login works as expected, with correct error messages for invalid input and successful redirection upon valid credentials.

## 2. Sign-Up Process:
- **Test Objective:** Ensure new users can successfully create an account.
- **Test Steps:**
  1. Navigate to the registration page.
  2. Fill in the required fields (name, email, password, address, etc.).
  3. Click the "Sign Up" button.
  4. Verify that the user receives a confirmation email (if applicable) and is redirected to the dashboard or homepage.
- **Edge Case Testing:**
  - **Email Format:** Entered an invalid email (e.g., "invalidemail") and confirmed that the form returns an appropriate error message.
  - **Password Strength:** Entered weak passwords (e.g., "12345") and confirmed the system prompts the user for a stronger password.
  - **Duplicate Email:** Attempted to register with an email already in use and verified that the user receives an error message ("Email already registered").
- **Result:** Registration process works correctly with validation for email format, password strength, and duplicate accounts.

## 3. Gadget Submission Process:
- **Test Objective:** Ensure users can successfully submit their gadgets for evaluation.
- **Test Steps:**
  1. Log in to the platform.
  2. Navigate to the "product" section on the product details page.
  3. Select the options (e.g., Storage, condition, network) to generate a price.
  4. Click "Sell This Device."
  5. Product is then added to the review order cart section, allowing the user to select either bank transfer or PayPal and enter the necessary details.
  6. Click "Continue Sale," which takes the user to the checkout page.
  7. Select the postage option and click "Confirm Sale."
  8. The checkout success page appears with an order summary and a "Print Label" option.
- **Edge Case Testing:**
  - **Missing Information:** Attempted submission with missing required fields (e.g., missing storage or condition) to verify that the system displays appropriate error messages.
  - **Invalid Payment Details:** Tested by entering invalid payment information (e.g., incorrect PayPal details) to ensure that the system prompts for corrections.
  - **Postage Option:** Verified that an error message is displayed, prompting the user to choose a valid postage option.
  - **Multiple Devices Submission:** Attempted to submit multiple devices at once to verify that the system handles multiple entries correctly.
- **Result:** Gadget submission process works smoothly, with validations for missing information, and postage option. The process proceeds to checkout with the correct order summary and the ability to print a shipping label or paid by sender option.

## 5. Admin Dashboard Testing:

- **Test Objective:** Ensure admins can manage the site effectively via the admin dashboard, even when maintenance mode is activated.

- **Test Steps:**
  1. Log in as an admin user.
  2. Navigate to the Admin Dashboard.
  3. Verify that the admin can view and manage user accounts, check orders, and update statuses.
  4. Test CRUD operations (Create, Read, Update, Delete) on brands, categories, products, users, and orders.
  5. Test the global settings section for the maintenance page and the Prepaid Postage Label/Paid by Sender options, ensuring they can be toggled on/off.
  6. **Test Maintenance Mode:**
     - Ensure that the maintenance page can be activated and deactivated from the global settings section in the admin panel.
     - Verify that when maintenance mode is activated, the admin can still access and manage the site, while non-admin users are redirected to the maintenance page.
  
- **Edge Case Testing:**
  - **Unauthorized Access:** Attempted to access admin pages without admin credentials and ensured that unauthorized users are redirected to a login page.
  - **Invalid Data Entry:** Tested the admin's ability to handle invalid data input (e.g., adding a product with missing required fields or incorrect formatting).
  - **Simultaneous Admin Actions:** Simultaneously tested admin actions on multiple sections to verify there are no concurrency issues or errors during simultaneous updates.

- **Result:** Admin functionality works as expected, with proper access control and the ability to manage users and content. The settings for maintenance page and postage options are adjustable, and CRUD operations on various entities are functional. The maintenance page can be easily toggled in the admin settings, and admins can bypass it to manage the site effectively, while non-admin users are properly redirected to the maintenance page.

## Conclusion:
Manual testing has been carried out across critical user flows, including login, sign-up, gadget submission, order placement, and admin dashboard interactions. Edge cases were also considered to ensure the platform is robust and error-free under various scenarios. The results of manual testing confirm that the platform provides a seamless user experience with proper validation and error handling in place.


## Automated Testing
Automated tests were written for core functionalities like registration, posting a gadget, and completing a sale. These tests ensure that the website works reliably after updates.

* I had to disable email verification to allow my tests that required log in to work.

## Bugs

### Resolved

### Payments & Cart

### 1. Issue: Missing Payment Method Handling
**Description:**
The revieworder page allowed users to select a payment method, but the backend did not validate or process the selected method properly.

**Cause:**
The `payment_method` field in the form was not dynamically validated, and fields for the unselected payment method were not being disabled.

**Fix:**

Added JavaScript to dynamically enable and disable input fields based on the selected payment method:

```javascript
function selectPaymentMethod(method) {
    const paymentMethodInput = document.getElementById('payment-method');
    paymentMethodInput.value = method;

    const bankFields = document.getElementById('bank-transfer-fields');
    const paypalFields = document.getElementById('paypal-fields');

    if (method === 'bank-transfer') {
        bankFields.style.display = 'block';
        paypalFields.style.display = 'none';
    } else if (method === 'paypal') {
        bankFields.style.display = 'none';
        paypalFields.style.display = 'block';
    }
}
```

### 2. Issue: Sort Code Input Navigation
**Description:**
Entering the sort code fields manually was tedious due to the lack of automatic focus change between input fields.

**Fix:**

Added event listeners to automatically move focus to the next field when two digits are entered:

```javascript
document.querySelectorAll('.sort-code-container input').forEach((input, index, inputs) => {
    input.addEventListener('input', (e) => {
        if (e.target.value.length === 2 && index < inputs.length - 1) {
            inputs[index + 1].focus();
        }
    });
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Backspace' && e.target.value === '' && index > 0) {
            inputs[index - 1].focus();
        }
    });
});
```

### 3. Issue: AJAX Error in remove_from_cart
**Description:**
The "Remove" button on the revieworder page did not dynamically update the cart when an item was removed.

**Cause:**
The AJAX function was not properly handling the CSRF token or reloading the cart dynamically.

**Fix:**

Updated the `removeFromCart` function to include the CSRF token and refresh the page upon successful removal:

```javascript
function removeFromCart(itemId) {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    fetch(`remove-from-cart/${itemId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
    })
    .then(response => {
        if (response.ok) {
            location.reload();
        } else {
            alert('Failed to remove item. Try again.');
        }
    })
    .catch(error => console.error("Error removing item:", error));
}
```

### Profile Dashboard & Admin
## Issue 1: Buttons Not Disappearing After User Response

### Observed Behavior:
- The "Accept" and "Reject" buttons remained visible even after the user selected a response (Accepted/Rejected).

### Root Cause:
- The conditional logic in the template was not correctly checking for the presence of a `user_response` value.

### Solution:
Updated the template logic to:
```django
{% if order.user_response == "Accepted" or order.user_response == "Rejected" %}
    <p>You have already {{ order.user_response|lower }} the offer.</p>
{% else %}
    <form method="post" action="">
        {% csrf_token %}
        <input type="hidden" name="order_id" value="{{ order.id }}">
        <button type="submit" name="response" value="Accepted" class="btn btn-success">Accept</button>
        <button type="submit" name="response" value="Rejected" class="btn btn-danger">Reject</button>
    </form>
{% endif %}
```

---

## Issue 2: Frontend Buttons Not Updating Admin

### Observed Behavior:
- Clicking "Accept" or "Reject" on the frontend did not reflect changes in the admin panel.

### Root Cause:
- The POST request handling in the backend was incomplete, and the AJAX functionality was missing for seamless updates.

### Solution:
1. Updated the backend view to handle `POST` requests for updating the `user_response` field.
2. Added the following JavaScript to handle AJAX calls:
```javascript
function updateUserResponse(orderId, response) {
    fetch('/admin/update-user-response/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
      },
      body: JSON.stringify({
        'order_id': orderId,
        'response': response
      })
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        alert("User response updated successfully!");
        location.reload();
      } else {
        alert("Failed to update user response.");
      }
    })
    .catch(error => {
      alert("Error: " + error);
    });
}
```

---

## Issue 3: Buttons Showing on Orders Without Revised Price

### Observed Behavior:
- "Accept" and "Reject" buttons appeared on orders that did not have a revised price.

### Root Cause:
- Missing check for `revised_price` in the template logic.

### Solution:
Wrapped the button rendering logic inside a check for `revised_price`:
```django
{% if order.revised_price %}
    <td class="revised-price">
        <p>Revised Price: £{{ order.revised_price }}</p>
        <p>Reason: {{ order.revised_reason }}</p>
        <!-- Additional logic for buttons -->
    </td>
{% else %}
    <td>N/A</td>
{% endif %}
```





