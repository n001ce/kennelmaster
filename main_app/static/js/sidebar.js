let btn = document.querySelector("#btn")
let sidebar = document.querySelector(".sidebar")
let main = document.querySelector(".main")
let header = document.querySelector(".header")
let footer = document.querySelector(".footer")


btn.onclick = function(){
  sidebar.classList.toggle("active")
  main.classList.toggle("active")
  header.classList.toggle("active")
  footer.classList.toggle("active")
}
