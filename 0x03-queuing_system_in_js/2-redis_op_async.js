import redis from 'redis';
import { promisify } from 'util';

const Redis_Client = redis.createClient();

Redis_Client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

Redis_Client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Convert Redis_Client.get to a promise-based function
const getAsync = promisify(Redis_Client.get).bind(Redis_Client);

async function setNewSchool(schoolName, value) {
    Redis_Client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    try {
        const res = await getAsync(schoolName);
        console.log(res);
    } catch (err) {
        console.error(err);
    }
}

(async () => {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');

    // Close the Redis client when done
    Redis_Client.quit();
})();
