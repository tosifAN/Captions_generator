document.getElementById('processButton').addEventListener('click', () => {
    const fileInput = document.getElementById('videoUpload');
    const videoFile = fileInput.files[0];
    
    if (videoFile) {
        const videoURL = URL.createObjectURL(videoFile);
        document.getElementById('videoPreview').src = videoURL;

        // Here you would add code to send the video to the backend for processing
        // Example: using Fetch API to post the video file to the backend
    }
});
