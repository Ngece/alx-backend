const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue();

// Function to send notifications
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from the queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

// Log when the processor starts
console.log('Job processor started');

// Log an error if the queue encounters an error
queue.on('error', (error) => {
  console.error('Queue error:', error);
});
