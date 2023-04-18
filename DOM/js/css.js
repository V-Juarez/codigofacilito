
// reglas de ccs
const element3 = document.querySelector('div.row > ul.list-group > li');
console.log(element3);


// querySelectoAll
// par odd
// impart even
const items1 = document.querySelectorAll('li:nth-child(even)')
for (var i = 0; i < items1.length; i++){
  let element = items1[i]
  element.style.background = 'gray';
}
