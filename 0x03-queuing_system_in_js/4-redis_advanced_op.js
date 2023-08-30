import redis from 'redis';

const Redis_Client = redis.createClient();

Redis_Client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

Redis_Client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function storeHash() {
    Redis_Client.hset('HolbertonSchools', 'Portland', 50, redis.print);
    Redis_Client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
    Redis_Client.hset('HolbertonSchools', 'New York', 20, redis.print);
    Redis_Client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
    Redis_Client.hset('HolbertonSchools', 'Cali', 40, redis.print);
    Redis_Client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

function displayHash() {
    Redis_Client.hgetall('HolbertonSchools', (err, result) => {
        if (err) {
            console.error(err);
        } else {
            console.log('Hash:', result);
        }
    });
}

storeHash();
displayHash();
