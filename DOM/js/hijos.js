const list = document.querySelector('ul');

console.log(list.childElementCount);

console.log(list.children);

for (var i = 0; i < list.children.length; i++) {
  console.log(list.children[i]);
}

// indice
console.log(list.children[1])
console.log(list.children[2])
console.log(list.children[3])

console.log("First child")
console.log(list.firstElementChild.innerHTML);

console.log("End")
console.log(list.lastElementChild.innerHTML)
