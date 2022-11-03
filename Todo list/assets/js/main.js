const inputNewTask = document.querySelector(".input-new-task"); // class do input
const btnAddTask = document.querySelector(".btn-add-task"); // class do botao adicionar
const tasks = document.querySelector(".tasks"); // class da tag <ul>

// Cria tag <li>
function createLi(){
  const li = document.createElement("li");
  return li;

}

// Poder adicionar com o "Enter" do teclado
inputNewTask.addEventListener("keypress", function(event){
  if (event.keyCode === 13){
    if (!inputNewTask.value) return;
    createTask(inputNewTask.value);

  }

});

// Limpa o imput quando adicionar
function cleanInput(){
  inputNewTask.value = " ";
  inputNewTask.focus();

}

// Cria button de apagar a cada novo <li> criado
function createCleanButton(li){
  li.innerText += " ";
  const cleanButton = document.createElement("button");
  cleanButton.innerText = "Apagar";
  cleanButton.setAttribute("class", "remove");
  li.appendChild(cleanButton);

}

function createTask(inputText){
  const li = createLi();
  li.innerText = inputText;
  tasks.appendChild(li);
  cleanInput();
  createCleanButton(li);
  saveTasks();

}

// Botao para adicionar novo li
btnAddTask.addEventListener("click", function(){
  if (!inputNewTask.value) return;
  createTask(inputNewTask.value);

});

//Apagar Tarefas
document.addEventListener("click", function(event){
  const element = event.target;
  if(element.classList.contains("remove")){
    element.parentElement.remove();
  }

})

// Salva o que foi pro <li> no navegador, entao as informacoes nao some com f5
function saveTasks(){
  const liTask = tasks.querySelectorAll("li");
  const tasksList = [];

  for (let task of liTask){
    let taskText = task.innerText;
    taskText = taskText.replace("Apagar", "").trim();
    tasksList.push(taskText);

  }

  const tasksJSON = JSON.stringify(tasksList);
  localStorage.setItem("tasks", tasksJSON);

}

function addSaveTasks(){
  const tasks = localStorage.getItem("tasks");
  const taskList = JSON.parse(tasks);

  for (let task of taskList){
    createTask(task);
    
  }
}

addSaveTasks();
