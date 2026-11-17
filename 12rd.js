const box = document.getElementById("box");

// Click event
box.addEventListener("click", function () {
  box.innerHTML = "Mouse clicked!";
});

// Double click event
box.addEventListener("dblclick", function () {
  box.innerHTML = "Mouse double clicked!";
});

// Mouseover event
box.addEventListener("mouseover", function () {
  box.innerHTML = "Mouse is over me!";
});

// Mouseout event
box.addEventListener("mouseout", function () {
  box.innerHTML = "Mouse is out!";
});