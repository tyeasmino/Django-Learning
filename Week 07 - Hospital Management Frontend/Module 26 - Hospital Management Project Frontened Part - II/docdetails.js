const getParams = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId")

    loadTime(param)
    
    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
    .then(res => res.json())
    .then(data => displayDetails(data))
    
    
    fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
    .then(res => res.json())
    .then(data => doctorReview(data))
}

const displayDetails = (doctor) => {
    const parent = document.getElementById("doc-details") 
    parent.innerHTML = `
    <div class="doctor-img">
        <img src=" ${doctor.image} " alt="">
    </div>
    <div class="doc-info">
        <h1> ${doctor.full_name} </h1>
        ${doctor.designation.map(item => {
            return `<h6 > ${item} </h6>`
            })
        }
        ${doctor.specialization.map(item => {
            return `<button class="btn btn-sm btn-secondary m-1"> ${item} </button>`
            })
        }
        <p class="w-75">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Explicabo dicta necessitatibus nobis sed repellat nihil.</p>
        <h4>Fees: ${doctor.fee} BDT</h4>
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Take Appointment
        </button>
    </div>
    `
}

const doctorReview = (reviews) => {
    reviews.forEach(review => {
        const parent = document.getElementById("doc-details-review")
        const div = document.createElement("div")
        div.classList.add("review-card")
        div.innerHTML = `
            <img class="mt-3" src="img/girl.png" alt="">
            <h4> ${review.reviewer} </h4>
            <p>${review.body.slice(0,100)} </p>
            <h6> ${review.rating} </h6>
        `
        parent.appendChild(div) 
    })
}


const loadTime = (id) => {
    fetch(`https://testing-8az5.onrender.com/doctor/availabletime/?doctor_id=${id}`)
    .then(res => res.json())
    .then(data => {
        data.forEach(item => {
            const parent = document.getElementById('time-container')
            const option = document.createElement("option")
            option.value = item.id
            option.innerText = item.name 
            parent.appendChild(option)
        })
    })
}

const handleAppointment = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId")


    const status = document.getElementsByName("status")
    const selectedStatus = Array.from(status).find(button => button.checked)
    
    const symptom = document.getElementById("symptom").value
    const time = document.getElementById("time-container")
    const selectedTime = time.options[time.selectedIndex].value  
    
    const info = {
        appointment_type: selectedStatus.value, 
        appointment_status: "Pending",
        time: selectedTime,
        symptom: symptom,
        cancel: false,
        patient: 1,
        doctor: param,
    }

    fetch(`https://testing-8az5.onrender.com/appointment/`, {
        method: "POST",
        headers: {"content-type": "application/json"},
        body: JSON.stringify(info)
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
    })
}


getParams()