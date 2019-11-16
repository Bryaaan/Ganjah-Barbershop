function validarCorreo(){
    var correo = document.getElementById("correo").value;
    if(correo==null||correo.lenght==0||!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/.test(correo))){
        alert("Correo Invalido")
    }
}