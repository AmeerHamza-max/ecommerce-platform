// Navigate to Microservices
function navigateTo(port) {
    window.location.href = `http://localhost:${port}`;
}

// To-Do App Functionality
document.addEventListener("DOMContentLoaded", loadTasks);

function addTask() {
    const taskInput = document.getElementById("todo-input");
    const taskText = taskInput.value.trim();
    
    if (taskText === "") return;

    const taskList = document.getElementById("todo-list");

    // Create list item
    const listItem = document.createElement("li");
    listItem.innerHTML = `${taskText} <button class="delete-btn" onclick="removeTask(this)">X</button>`;

    taskList.appendChild(listItem);

    // Save to Local Storage
    saveTask(taskText);

    // Clear Input
    taskInput.value = "";
}

function removeTask(button) {
    const listItem = button.parentElement;
    const taskText = listItem.firstChild.textContent;

    listItem.remove();
    deleteTask(taskText);
}

function saveTask(task) {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.push(task);
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function deleteTask(task) {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks = tasks.filter(t => t !== task);
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    const taskList = document.getElementById("todo-list");

    tasks.forEach(task => {
        const listItem = document.createElement("li");
        listItem.innerHTML = `${task} <button class="delete-btn" onclick="removeTask(this)">X</button>`;
        taskList.appendChild(listItem);
    });
}
