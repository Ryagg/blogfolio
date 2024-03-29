const by = Object.freeze({
    q: (query) => document.querySelector(query),
    qAll: (queryAll) => document.querySelectorAll(queryAll),
    id: (id) => document.getElementById(id),
    class: (className) => document.getElementsByClassName(className),
    tag: (tag) => document.getElementsByTagName(tag),
    name: (name) => document.getElementsByName(name),
});

// update Copyright date
document.addEventListener("DOMContentLoaded", () => {
    let currentYear = new Date().getFullYear();
    let createdIn = 2022;
    let yearID = by.id("year");
    console.log(yearID);
    if (currentYear > createdIn) {
        yearID.innerHTML = `${createdIn} - ${currentYear}`;
    }
  });
