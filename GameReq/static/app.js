document.querySelector('#btnn').addEventListener('click', searchName);
const api = `http://127.0.0.1:8000/viewsets/requirements/`;


function searchName(e){
    e.preventDefault();
    var input = document.querySelector('input');
    if(input.value != '')
    {
        addActivity(input.value);
    }
    input.value = '';
}

function addActivity(input){

    fetch(api)
    .then(response => {
        return response.json();
    })
    .then(data =>{
        console.log(data);

        for(var i = 0; i<data.length; i++){
            if(data[i].name == input){
                var x = i;
                break;
            }
        }
        const {img} = data[x];
        const {name} = data[x];
        const {CPU} = data[x];
        const {RAM} = data[x];
        const {GPU} = data[x];
        const {HDD} = data[x];
        const {OS} = data[x];

        console.log(img);

        document.querySelector('.heading').style.visibility = "visible";
        document.querySelector('.image').src = `${img}`;
        document.querySelector('.name').innerHTML = `Name : ${name}`;
        document.querySelector('.cpu').innerHTML = `CPU : ${CPU}`;
        document.querySelector('.ram').innerHTML = `RAM : ${RAM}`;
        document.querySelector('.gpu').innerHTML = `GPU : ${GPU}`;
        document.querySelector('.hdd').innerHTML = `HDD : ${HDD}`;
        document.querySelector('.os').innerHTML = `OS : ${OS}`;
        
    })
}