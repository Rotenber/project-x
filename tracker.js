(async function() {
    const data = {
        userAgent: navigator.userAgent,
        platform: navigator.platform,
        language: navigator.language,
        screenWidth: screen.width,
        screenHeight: screen.height,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
    };

    try {
        const response = await fetch("https://your-app.up.railway.app/collect", { // Замените на URL вашего Flask-сервера
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            console.error("Ошибка при отправке данных:", response.statusText);
        } else {
            console.log("Данные успешно отправлены.");
        }
    } catch (error) {
        console.error("Ошибка при подключении к серверу:", error);
    }
})();
