document.addEventListener('DOMContentLoaded', function () {
    let suggestions = document.getElementById('suggestions');
    let searchBox = document.getElementById('search-box');
    let searchButton = document.getElementById('search-button');
    let suggestionBg = document.querySelector('.suggestion-bg'); // Assuming this targets a single element
    
    // Function to clear suggestions and suggestion background
    function clearSuggestions() {
        suggestions.innerHTML = ''; // Clear suggestions
        suggestions.classList.remove('active'); // Hide suggestion list
        suggestionBg.classList.remove('active'); // Hide suggestion background
    }

    // Function to hide suggestions if clicked outside
    function handleClickOutside(event) {
        if (!searchBox.contains(event.target) && !suggestions.contains(event.target)) {
            clearSuggestions(); // Hide suggestions if clicked outside
        }
    }

    // Event listener to handle typing in the search box
    searchBox.addEventListener('input', function() {
        let query = searchBox.value.trim(); // Trim any extra spaces

        if (query.length > 0) {
            fetch(`/search?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    console.log('Fetched data:', data); // Log data to inspect the structure
                    clearSuggestions(); // Clear previous suggestions
                    
                    if (Array.isArray(data) && data.length > 0) {
                        data.forEach(item => {
                            let li = document.createElement('li');
                            let name = item.name || 'Unnamed'; // Use 'name' instead of 'Name'
                            li.textContent = name;
                            li.addEventListener('click', function() {
                                window.location.href = item.url; // Use URL from the backend
                            });
                            suggestions.appendChild(li);
                        });
                        suggestions.classList.add('active'); // Show suggestions
                        suggestionBg.classList.add('active'); // Show suggestion background
                    } else {
                        clearSuggestions(); // Hide suggestions if none
                    }
                })
                .catch(error => {
                    console.error('Error fetching suggestions:', error);
                });
        } else {
            clearSuggestions(); // Hide and clear suggestions if input is empty
        }
    });

    // Redirect to the results page when the Enter key is pressed
    searchBox.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            window.location.href = `/results?q=${encodeURIComponent(this.value.trim())}`;
        }
    });

    // Search button click functionality
    searchButton.addEventListener('click', function() {
        let query = searchBox.value.trim(); // Trim any extra spaces
        if (query) {
            window.location.href = `/results?q=${encodeURIComponent(query)}`;
        }
    });

    // Add event listener to handle clicks outside the search box and suggestions
    document.addEventListener('click', handleClickOutside);
});
