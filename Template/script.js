// Sample data for categories and trending products
const categoriesData = ['Fruits', 'Vegetables', 'Dairy', 'Meat', 'Beverages'];
const trendingProductsData = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'];

// Function to generate category buttons dynamically
function generateCategoryButtons() {
  const categoriesSection = document.querySelector('.categories');

  categoriesData.forEach(category => {
    const button = document.createElement('button');
    button.textContent = category;
    categoriesSection.appendChild(button);

    // Add event listener to handle button clicks (you can add more functionality here)
    button.addEventListener('click', () => {
      alert(`You clicked on ${category} category!`);
    });
  });
}

// Function to generate trending product list dynamically
function generateTrendingProducts() {
  const trendsSection = document.querySelector('.trends');

  trendingProductsData.forEach(product => {
    const listItem = document.createElement('div');
    listItem.textContent = product;
    trendsSection.appendChild(listItem);
  });
}

// Event listener for product search input
document.getElementById('product-search').addEventListener('input', function () {
  // Here, you can implement product search functionality and update the #product-info section accordingly
  const searchTerm = this.value;
  const productInfoSection = document.getElementById('product-info');

  // For now, we'll just display the search term entered
  productInfoSection.textContent = `Searching for: ${searchTerm}`;
});

// Call the functions to generate category buttons and trending product list
generateCategoryButtons();
generateTrendingProducts();
