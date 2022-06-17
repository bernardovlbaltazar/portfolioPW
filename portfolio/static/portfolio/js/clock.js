document.addEventListener('DOMContentLoaded', ()=> {
    let clock = document.getElementById('datetime');

    setInterval(function () {
        let date = new Date();
        let am_pm = "";

        if (date.getHours() >= 12){
            am_pm = "PM";
        }else {
            am_pm = "AM"
        }

        clock.innerHTML = date.toLocaleTimeString() +" " + am_pm;
    },1000);
})