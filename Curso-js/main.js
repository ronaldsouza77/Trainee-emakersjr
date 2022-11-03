function adicionarlinha(){
    var input = document.querySelector("#task")
    var task = input.value
    console.log(task)

    var rowElement = document.getElementById("table").insertRow(-1)
    var checkbox = rowElement.insertCell(0)
    var linha = rowElement.insertCell(1)
    linha.innerHTML = task
    checkbox.innerHTML = `<input type="checkbox" id="mycheck" onclick="myfunction()">`
   
    //document.querySelector("#newline").innerHTML="<tr><TD>teste</TD></tr>"
    //document.querySelector("#newline").innerHTML = `<tr><td>${task}</td></tr>`
}


