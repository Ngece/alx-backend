import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Create a Redis client
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Reserve seat
function reserveSeat(number) {
  return setAsync('available_seats', number);
}

// Get current available seats
async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync('available_seats');
  return parseInt(availableSeats) || 0;
}

// Initialize the number of available seats
reserveSeat(50);

// Initialize reservationEnabled
let reservationEnabled = true;

// Create a Kue queue
const queue = kue.createQueue();

// Middleware to parse JSON requests
app.use(express.json());

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

// Route to process the queue and decrease available seats
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats <= 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      await reserveSeat(availableSeats - 1);
      if (availableSeats === 1) {
        reservationEnabled = false;
      }
      done();
    }
  });
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Log an error if the queue encounters an error
queue.on('error', (error) => {
  console.error('Queue error:', error);
});

// Log when the processor starts
console.log('Seat reservation processor is running');

export default app;
