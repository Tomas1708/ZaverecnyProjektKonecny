const alerts = document.querySelectorAll(".alert-success");

alerts.forEach((alert) => {
    setTimeout(() => {
        const bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
    }, 3000);
});