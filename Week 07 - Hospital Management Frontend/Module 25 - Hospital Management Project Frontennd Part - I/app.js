const loadServices = () => {
    fetch("https://testing-8az5.onrender.com/services/")
    .then((res) => res.json())
        .then((data) => console.log(data))
    .catch((err) => console.log(err))
}

loadServices()