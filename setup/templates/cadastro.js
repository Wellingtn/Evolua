const urlParams = new URLSearchParams(window.location.search);
const status = urlParams.get("status");

if (status === "success") {
    showAlert("Cadastro realizado com sucesso!", "green");
} else if (status === "error") {
    showAlert("Erro ao realizar cadastro. Verifique os dados informados.", "red");
}

function showAlert(message, color) {
    const alertBox = document.getElementById("alert-box");
    const alertMessage = document.getElementById("alert-message");
    alertBox.style.backgroundColor = color;
    alertMessage.textContent = message;
    alertBox.style.display = "block";
    setTimeout(() => {
        alertBox.style.display = "none";
    }, 5000);
}
