jQuery(document).ready(function($) {
    var productsFound = false;

    // Prevent empty search submissions for the first form
    $("#search-form").submit(function(event) {
        var searchInput = $("#search-input").val().trim();
        var errorMessage = $("#error-message");

        if (searchInput === "") {
            errorMessage.text("Please enter a search term.");
            errorMessage.show();  // Show error message
            $("#search-input").addClass("error");  // Add error class to input
            event.preventDefault();  // Prevent form submission
        } else {
            errorMessage.text("");
            errorMessage.hide();
            $("#search-input").removeClass("error");
        }
    });

    // Make error message disappear while typing
    $("#search-input").on("keyup", function() {
        var searchInput = $(this).val().trim();
        var errorMessage = $("#error-message");

        // Hide the error message if the input is not empty
        if (searchInput !== "") {
            errorMessage.text("").hide();
            $("#search-input").removeClass("error");
        }
    });

    // Prevent empty search submissions for the second form
    $("#search-form2").submit(function(event) {
        var searchInput2 = $("#search-input2").val().trim();
        var errorMessage2 = $("#error-message2");

        if (searchInput2 === "") {
            errorMessage2.text("Please enter a search term.");
            errorMessage2.show();  // Show error message
            $("#search-input2").addClass("error");  // Add error class to input
            event.preventDefault();  // Prevent form submission
        } else {
            errorMessage2.text("");
            errorMessage2.hide();
            $("#search-input2").removeClass("error");
        }
    });

      // Make error message disappear while typing
      $("#search-input2").on("keyup", function() {
        var searchInput2 = $(this).val().trim();
        var errorMessage2 = $("#error-message2");

        // Hide the error message if the input is not empty
        if (searchInput2 !== "") {
            errorMessage2.text("").hide();
            $("#search-input").removeClass("error");
        }
    });

    // Handle input event for search field in the first form
    $('#search-input').on('input', function() {
        var query = $(this).val();  // Get the input value

        // Only trigger AJAX if the query has more than 1 character
        if (query.length > 1) {
            searchProducts(query, '#suggestions-list');  // Pass #suggestions-list for the first form
        } else {
            resetSearchResults('#suggestions-list');  // Hide suggestions and reset error message
        }
    });

    // Handle input event for search field in the second form
    $('#search-input2').on('input', function() {
        var query = $(this).val();  // Get the input value

        // Only trigger AJAX if the query has more than 1 character
        if (query.length > 1) {
            searchProducts(query, '#suggestions-list2');  // Pass #suggestions-list2 for the second form
        } else {
            resetSearchResults('#suggestions-list2');  // Hide suggestions and reset error message
        }
    });

    // Handle search button click event for the first form
    $('#search-button').on('click', function(event) {
        var query = $('#search-input').val();  // Get the search query value

        // If no products are found, prevent form submission
        if (query.length > 2 && !productsFound) {
            event.preventDefault();
        }
    });

    // Handle search button click event for the second form
    $('#search-button2').on('click', function(event) {
        var query = $('#search-input2').val();  // Get the search query value

        // If no products are found, prevent form submission
        if (query.length > 2 && !productsFound) {
            event.preventDefault();
        }
    });

    // Handle product suggestion click event for the first form
    $('#suggestions-list').on('click', 'li a', function() {
        $('#suggestions-list').empty().hide();
    });

    // Handle product suggestion click event for the second form
    $('#suggestions-list2').on('click', 'li a', function() {
        $('#suggestions-list2').empty().hide();
    });

    // Function to make AJAX request for product search
    function searchProducts(query, suggestionsListId) {
        $.ajax({
            url: searchUrl,  // URL for the search_results view
            data: { 'search': query },  // Send the search query as a GET parameter
            success: function(data) {
                console.log(data);  // Log the response to see what is returned
                $(suggestionsListId).empty().show();  // Clear previous suggestions

                if (data.products.length > 0) {
                    productsFound = true;
                    data.products.forEach(function(product) {
                        var productUrl = '/sell/' + product.slug + '/';
                        $(suggestionsListId).append('<li><a href="' + productUrl + '">' + product.name + '</a></li>');
                    });
                } else {
                    productsFound = false;
                    $(suggestionsListId).append('<li>No products found</li>');
                }
                
            },
            error: function(xhr, status, error) {
                console.error('AJAX request failed:', status, error);
            }
        });
    }

    // Function to reset search results and hide suggestions
    function resetSearchResults(suggestionsListId) {
        $(suggestionsListId).hide();
        $('#error-message').empty();
        productsFound = false;
    
    }


});
