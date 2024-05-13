function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        // Here you can simulate an asynchronous operation using setTimeout
        setTimeout(() => {
            resolve("Success");  // This will resolve the promise after a delay
            // If something goes wrong, you could call reject("Error") instead
        }, 1000); // Adjust time as needed for your simulation
    });
}

export default getResponseFromAPI;
