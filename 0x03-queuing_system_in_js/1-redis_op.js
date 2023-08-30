// Redis client that connects to a redis server

import redis from 'redis';

const Redis_Client = redis.createClient();

Redis_Client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
    });

    Redis_Client.on('connect', () => {
    console.log('Redis client connected to the server');
    });

function setNewSchool(schoolName, value) {
    Redis_Client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    Redis_Client.get(schoolName, (err, res) => {
        console.log(res);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');