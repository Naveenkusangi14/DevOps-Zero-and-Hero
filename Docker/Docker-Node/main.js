const express = require('express');
const app = express();

const PORT = process.env.PORT || 8000;

// Define a route
app.get('/', (req, res) => {
    return res.json({ message: "I am node in container" });
});

// Start the server
app.listen(PORT, () => console.log(`Service started on PORT: ${PORT}`));
