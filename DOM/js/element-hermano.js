const element = document.querySelector('div.row > ul.list-group > li');

console.log(element.parentElement.parentElement);

console.log(element.parentElement);

console.log(element.nextElementSibling.nextElementSibling)

console.log(element.nextElementSibling.nextSibling)

const last_element = document.getElementById('last-course');

console.log(last_element);
console.log(last_element.previousElementSibling);
