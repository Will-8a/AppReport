function ocultarInicio() {
    document.getElementById("elementosPrincipales").hidden = true;
    document.getElementById("camposReportes").hidden = false;
}
function mostrarInicio() {
    document.getElementById("elementosPrincipales").hidden = false;
    document.getElementById("camposReportes").hidden = true;
}

function editarBotonSubmit(metodo, url){
    document.addEventListener("DOMContentLoaded", function() {
        document.querySelector("form").addEventListener("submit", function(e) {
            // deshabilita el boton de subida 
            document.getElementById('btn_subir').disabled = true
            
            // Evita que el formulario se envíe de la manera predeterminada
            e.preventDefault();

            // Crea un objeto FormData con los datos del formulario
            var formData = new FormData(this);

            // Configura la petición AJAX
            var xhr = new XMLHttpRequest();
            xhr.open(metodo, url, true);

            // Configura lo que sucede cuando se recibe la respuesta
            xhr.onload = function() {
                if (xhr.readyState == 4 && xhr.status === 200) {
                    // La petición fue exitosa, puedes procesar la respuesta aquí
                    // console.log(xhr.responseText);
                    // Guardar respuesta en sessionStorage
                    sessionStorage.setItem("respuesta_api", xhr.responseText);
                    // Recarga la página
                    location.reload();
                } else {
                    // Para manejar si ocurre un error
                    console.error("Error: " + xhr.status);
                }
            };
            // Envía la petición
            xhr.send(formData);
        });

        // Obtener respuesta guardada de session
        let respuesta_api = sessionStorage.getItem("respuesta_api");
        // Mostrar notificacion en front
        sessionStorage.removeItem("respuesta_api");
    });
}
