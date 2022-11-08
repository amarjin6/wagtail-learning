let content = document.getElementById("content")
let show = document.getElementsByClassName("w-field__input")
let hide = document.getElementById("hideContent")

show.addEventListener("click", () => {
    content.style.display = "block"

})

hide.addEventListener("click", () => {
    content.style.display = "none"
})
