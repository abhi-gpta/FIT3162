// Sample data for categories and trending products
const categoriesData = [
  'Fruits', 'Vegetables', 'Dairy', 'Meat', 'Beverages',
  'Snacks', 'Bakery', 'Canned Goods', 'Frozen Foods', 'Personal Care',
  'Household', 'Pet Supplies', 'Health & Wellness', 'Cleaning Supplies',
  'Baby & Kids', 'Alcohol'
];
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

// Function to toggle the drawer open/close
function toggleDrawer() {
  const drawer = document.querySelector('.drawer');
  drawer.classList.toggle('open');
}

// Call the function to generate category buttons
generateCategoryButtons();

// Add event listener to the header to toggle the drawer
document.querySelector('header').addEventListener('click', toggleDrawer);
