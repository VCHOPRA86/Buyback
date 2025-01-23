window.addEventListener('load', function() {
    // Log to check if the page is loaded correctly
    console.log('Page Loaded');
    
    const filterSection = document.getElementById('changelist-filter');  // Target the filter section by id
    if (!filterSection) {
        console.log('Filter section not found!');
        return;  // Exit if filter section is not found
    }
    
    const toggleButton = document.createElement('button');
    toggleButton.textContent = 'Show Filters';  // Default text when collapsed
    toggleButton.style.marginLeft = '10px';  // Add some space to the left of the button
    toggleButton.style.padding = '5px 10px';  // Padding for a better button size
    toggleButton.style.fontSize = '14px';  // Font size for better readability
    toggleButton.style.cursor = 'pointer';  // Change cursor to pointer to indicate it is clickable
    toggleButton.style.border = '1px solid #ccc';  // Border around the button
    toggleButton.style.backgroundColor = '#f0f0f0';  // Light background color for the button
    toggleButton.style.borderRadius = '4px';  // Rounded corners for the button
    toggleButton.style.transition = 'background-color 0.3s';  // Smooth background color transition on hover
    
    // Add hover effect
    toggleButton.addEventListener('mouseover', function() {
        toggleButton.style.backgroundColor = '#e0e0e0';  // Change background on hover
    });

    toggleButton.addEventListener('mouseout', function() {
        toggleButton.style.backgroundColor = '#f0f0f0';  // Reset background on mouse out
    });


    filterSection.parentNode.insertBefore(toggleButton, filterSection.nextSibling);  // Insert button next to the filter section

    // Log to check if the button is inserted correctly
    console.log('Toggle button added');
    
    // Toggle visibility of the filter section on button click
    toggleButton.addEventListener('click', function() {
        if (filterSection.style.display === 'none') {
            filterSection.style.display = 'block';  // Show the filter section
            toggleButton.textContent = 'Hide Filters';  // Change button text when expanded
        } else {
            filterSection.style.display = 'none';  // Hide the filter section
            toggleButton.textContent = 'Show Filters';  // Change button text when collapsed
        }
        
        // Log to see the state change
        console.log('Filter section toggled');
    });
});
