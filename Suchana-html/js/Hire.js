document.getElementById('jobForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Get form data
    const formData = new FormData(event.target);
    const jobTitle = formData.get('jobTitle');
    const jobDescription = formData.get('jobDescription');
    const contactName = formData.get('contactName');
    const contactEmail = formData.get('contactEmail');
  
    // Example: Sending form data to the server
    // Replace this with your own logic to handle the form submission
    // For example, you might want to use AJAX to send the form data to a server-side script
    // Here, we'll just show a message to indicate the form has been submitted
    const messageElement = document.getElementById('message');
    messageElement.textContent = 'Thank you for submitting the job request! We will contact you soon.';
    messageElement.style.color = '#007bff';
    clearForm();
  });
  
  function clearForm() {
    document.getElementById('jobForm').reset();
  }