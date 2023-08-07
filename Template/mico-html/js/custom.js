// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

// nice select
$(document).ready(function () {
    $('select').niceSelect();
});

// date picker
$(function () {
    $("#inputDate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', new Date());
});

// owl carousel slider js
$('.team_carousel').owlCarousel({
    loop: true,
    margin: 15,
    dots: true,
    autoplay: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1,
            margin: 0
        },
        576: {
            items: 2,
        },
        992: {
            items: 3
        }
    }
})
const groceryData = [
    { item: 'Apples', price: '$1.29 per lb' },
    { item: 'Bananas', price: '$0.39 per lb' },
    { item: 'Carrots', price: '$0.99 per lb' },
    { item: 'Spinach', price: '$2.49 per bunch' },
    { item: 'Milk', price: '$2.99 per gallon' }
];

const tableBody = document.getElementById('tableBody');

function populateTable() {
    groceryData.forEach(item => {
        const row = document.createElement('tr');
        const itemName = document.createElement('td');
        const itemPrice = document.createElement('td');
        itemName.textContent = item.item;
        itemPrice.textContent = item.price;
        row.appendChild(itemName);
        row.appendChild(itemPrice);
        tableBody.appendChild(row);
    });
}

populateTable();
