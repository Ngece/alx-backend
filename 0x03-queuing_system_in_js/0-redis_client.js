// Redis client that connects to a redis server

import redis from 'redis';

const Redis_Client = redis.createClient();

Redis_Client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
    });

    Redis_Client.on('connect', () => {
    console.log('Redis client connected to the server');
    });

export default Redis_Client;
