const loadServices = () => {
    fetch("https://testing-8az5.onrender.com/services/")
    .then((res) => res.json())
        .then((data) => displayService(data))
    .catch((err) => console.log(err))
}

const displayService = (services) => { 
    services.forEach((service) => {
        const parent = document.getElementById('service-container')
        const li = document.createElement('li')
        li.innerHTML = `
        <div class="card shadow h-100">
            <div class="ratio ratio-16x9">
                <img src=" ${service.image} " loading="lazy" alt="...">
            </div>
            <div class="card-body p-3 p-xl-5">
                <h3 class="card-title h5"> ${service.name} </h3>
                <p class="card-text"> ${service.description.slice(0,200)}... </p>
                <div><a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
        </div>
        `

        parent.appendChild(li) 
    });
}


const loadDoctors = (search) => {
    fetch(`https://testing-8az5.onrender.com/doctor/list/?search=${
        search?search:"" 
    }`)
    .then((res) => res.json())
    .then((data) => displayDoctors(data?.results))
}

const displayDoctors = (doctors) => {
    doctors?.forEach((doctor) => { 
        const parent = document.getElementById("doctors")
        parent.innerHTML = ''
        const div = document.createElement("div")
        div.classList.add("doc-card")
        div.innerHTML = `
            <img class="doc-img" src=" ${doctor?.image} " alt="">
            <h4> ${doctor?.full_name} </h4>
            <h6> ${doctor?.designation[0]} </h6>
            <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt labore culpa, distinctio assumenda facere, aut, ullam dolorem adipisci?  </p>
            <p> 
                ${doctor?.specialization.map((item) => {
                    return `<button class="btn btn-primary mx-1"> ${item} </button>`
                })} 
            </p>
            
            <button class="btn btn-secondary mx-1">Details</button>
        `
        parent.appendChild(div) 
    })
}



const loadDesignation = () => {
    fetch("https://testing-8az5.onrender.com/doctor/designation/")
    .then((res) => res.json())
    .then((data) => {
        data.forEach((item) => {
            const parent = document.getElementById("drop-deg")
            const li = document.createElement("li")
            li.classList.add("dropdown-item")
            li.innerHTML = item.name
            parent.appendChild(li) 
        })
    })
}


const loadSpecialization = () => {
    fetch("https://testing-8az5.onrender.com/doctor/specialization/")
    .then((res) => res.json())
    .then((data) => {
        data.forEach((item) => {
            const parent = document.getElementById("drop-spe")
            const li = document.createElement("li")
            li.classList.add("dropdown-item")
            li.innerHTML = item.name
            parent.appendChild(li) 
        })
    })
}


const handleSearch = () => {
    const value = document.getElementById("search").value
    loadDoctors(value)
}




// `https://testing-8az5.onrender.com/doctor/list/?search=${
//         search ? search : ""
//       }`


loadServices()
loadDoctors()
loadDesignation() 
loadSpecialization() 