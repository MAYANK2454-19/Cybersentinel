document.addEventListener("DOMContentLoaded",()=>{

    const overlay=document.getElementById("loading-overlay");

    const forms=document.querySelectorAll("form");

    const steps=document.querySelectorAll(".step");

    forms.forEach(form=>{

        form.addEventListener("submit",()=>{

            overlay.classList.add("active");

            let index=0;

            steps[0].classList.add("active");

            setInterval(()=>{

                if(index<steps.length-1){

                    steps[index].classList.remove("active");

                    index++;

                    steps[index].classList.add("active");

                }

            },700);

        });

    });

});