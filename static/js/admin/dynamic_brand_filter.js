window.addEventListener('load', function () {
    (function ($) {
        $(document).ready(function () {
            const categoryField = $('#id_category');
            const brandField = $('#id_brand');
            const networkFields = [
                '#id_unlocked_price_adjustment',
                '#id_ee_price_adjustment',
                '#id_o2_price_adjustment',
                '#id_vodafone_price_adjustment',
                '#id_three_price_adjustment',
            ];

            if (!categoryField.length) {
                console.error('Category field not found. Check the field ID.');
                return;
            }

            console.log('Script loaded successfully. Category field detected:', categoryField);

            function toggleNetworkFields(categoryName) {
                console.log('Toggling network fields for category:', categoryName);
                if (categoryName === 'Phones' || categoryName === 'Tablets') {
                    networkFields.forEach(function (field) {
                        $(field).closest('.form-row').show(); // Ensure the closest form-row (or equivalent container) is shown
                    });
                } else {
                    networkFields.forEach(function (field) {
                        $(field).closest('.form-row').hide(); // Ensure the closest form-row is hidden
                    });
                }
            }

            function updateBrands(categoryId) {
                console.log('Fetching brands for category ID:', categoryId);
            
                if (!categoryId) {
                    brandField.empty().append('<option value="">---------</option>');
                    console.log('Category not selected. Brand dropdown reset.');
                    return;
                }
            
                const selectedBrandId = brandField.val(); // Save the currently selected brand ID
                console.log('Currently selected brand ID:', selectedBrandId);
            
                $.ajax({
                    url: '/admin/products/product/filter_brands/',
                    data: { category_id: categoryId },
                    success: function (response) {
                        console.log('Brands fetched successfully:', response.brands);
                        brandField.empty().append('<option value="">---------</option>');
            
                        response.brands.forEach(function (brand) {
                            const isSelected = brand.id === parseInt(selectedBrandId); // Check if this is the selected brand
                            brandField.append(
                                `<option value="${brand.id}" ${isSelected ? 'selected' : ''}>${brand.name}</option>`
                            );
                        });
            
                        console.log('Brand dropdown updated. Selected brand preserved:', selectedBrandId);
                    },
                    error: function (xhr, status, error) {
                        console.error('Failed to fetch brands:', status, error);
                    }
                });
            }

            // Ensure category change triggers the proper visibility of network fields
            function initPage() {
                const initialCategoryId = categoryField.val();
                if (initialCategoryId) {
                    const initialCategoryName = categoryField.find('option:selected').text();
                    console.log('Initial category detected:', initialCategoryId, initialCategoryName);
                    updateBrands(initialCategoryId);
                    toggleNetworkFields(initialCategoryName);  // Trigger toggling network fields immediately based on the pre-selected category
                }
            }

            // Delay running the initPage function slightly after page load to ensure form fields are populated
            setTimeout(initPage, 100);

            // Update brands and toggle network fields when the category changes
            categoryField.change(function () {
                const selectedCategoryId = $(this).val();
                const selectedCategoryName = $(this).find('option:selected').text();
                console.log('Category changed to:', selectedCategoryId, selectedCategoryName);
                updateBrands(selectedCategoryId);
                toggleNetworkFields(selectedCategoryName);
            });

            // Initially hide network fields until the category is set
            networkFields.forEach(function (field) {
                $(field).closest('.form-row').hide();
            });
        });
    })(jQuery); // Use standard jQuery instance
});
