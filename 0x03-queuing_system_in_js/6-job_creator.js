const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue();

// Create a job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello from Kue!',
};

// Create a queue named push_notification_code
const pushNotificationJob = queue.create('push_notification_code', jobData);

// Event listener for successful job creation
pushNotificationJob.on('enqueue', () => {
  console.log(`Notification job created: ${pushNotificationJob.id}`);
});

// Event listener for job completion
pushNotificationJob.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for job failure
pushNotificationJob.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
pushNotificationJob.save((error) => {
  if (error) {
    console.error('Error creating job:', error);
  }
});
