document.addEventListener("DOMContentLoaded",()=>{

    const toggle=document.getElementById("menu-toggle");
    const sidebar=document.getElementById("sidebar");

    if(toggle && sidebar){

        toggle.addEventListener("click",()=>{

            sidebar.classList.toggle("show-sidebar");

            if(sidebar.classList.contains("show-sidebar")){

                toggle.innerHTML="✕";

            }else{

                toggle.innerHTML="☰";

            }

        });

    }

});