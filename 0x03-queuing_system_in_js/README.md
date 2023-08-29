0-redis_client.js           Connects to the redis server running on the local machine:
    It logs to the console the message 'Redis client connected to the server' when the connection to Redis works correctly
    It logs to the console the message 'Redis client not connected to the server: ERROR_MESSAGE' when the connection to Redis does not work




1-redis_op.js               Contains same contents as 0-redis_client.js with two added functions:
    setNewSchool:
        It accepts two arguments schoolName, and value.
        It sets in Redis the value for the key schoolName
        It displays a confirmation message using redis.print
    displaySchoolValue:
        It accepts one argument schoolName.
        It logs to the console the value for the key passed as argument
    At the end of the file, call:
        displaySchoolValue('Holberton');
        setNewSchool('HolbertonSanFrancisco', '100');
        displaySchoolValue('HolbertonSanFrancisco');




2-redis_op_async.js           Contains same content as 1-redis_op.js and uses promisify to modify the function displaySchoolValue to use ES6 async / await 





4-redis_advanced_op.js          Stores hash values for a key called HolbertonSchools, Values: 
    Portland=50
    Seattle=80
    New York=20
    Bogota=20
    Cali=40
    Paris=2





5-subscriber.js                 Contains a redis client that:
    On connect, it logs the message 'Redis client connected to the server'
    On error, it logs the message 'Redis client not connected to the server: ERROR MESSAGE'
    It should subscribe to the channel holberton school channel
    When it receives message on the channel 'holberton school channel', it logs the message to the console
    When the message is 'KILL_SERVER', it should unsubscribe and quit




5-publisher.js                  Contains a redis client that:
    On connect, it logs the message 'Redis client connected to the server'
    On error, it logs the message 'Redis client not connected to the server: ERROR MESSAGE'
    function named publishMessage:
        takes two arguments: message (string), and time (integer - in ms)
        After time millisecond:
            The function logs to the console 'About to send MESSAGE'
            The function publishes to the channel 'holberton school channel', the message passed in argument after the time passed in arguments




6-job_creator.js                 Contains a queue created with using Kue with job data of the following format:
    {
    phoneNumber: string,
    message: string,
    }




6-job_processor.js               Contains a Kue queue with function named sendNotification: 
    takes two arguments phoneNumber and message
    logs to the console 'Sending notification to PHONE_NUMBER', with message: 'MESSAGE'
    Has a queue process that will listen to new jobs on push_notification_code:
        Every new job calls the sendNotification function with the phone number and the message contained within the job data




7-job_creator.js                 Contains an array 'jobs' with data inside
    Has a queue created with Kue:
        Has a loop that will go through the array jobs and for each object:
            Creates a new job to the queue push_notification_code_2 with the current object
            If there is no error, logs to the console Notification job created: JOB_ID
            On the job completion, logs to the console Notification job JOB_ID completed
            On job failure, logs to the console Notification job JOB_ID failed: ERROR
            On the job progress, logs to the console Notification job JOB_ID PERCENTAGE% complete





7-job_processor.js                  Has an array that will contain the blacklisted phone numbers. 4153518780 and 4153518781 will be blacklisted by the jobs processor.
    Has a function sendNotification that takes 4 arguments: phoneNumber, message, job, and done:
        When the function is called, it tracks the progress of the job of 0 out of 100
        If phoneNumber is included in the “blacklisted array”, fails the job with an Error object and the message: 'Phone number PHONE_NUMBER is blacklisted'
        Otherwise:
            Track the progress to 50%
            Log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE




8-job.js                        Contains a function named createPushNotificationsJobs:   
    It takes into argument jobs (array of objects), and queue (Kue queue)
    If jobs is not an array, it throws an Error with message: 'Jobs is not an array'
    For each job in jobs, creates a job in the queue push_notification_code_3
    When a job is created, it logs to the console Notification job created: JOB_ID
    When a job is complete, it logs to the console Notification job JOB_ID completed
    When a job is failed, it logs to the console Notification job JOB_ID failed: ERROR
    When a job is making progress, it logs to the console Notification job JOB_ID PERCENT% complete




8-job.test.js                     Tets for 8-job.js using Kue queue:
    a test suite for the createPushNotificationsJobs function:
        Uses queue.testMode to validate which jobs are inside the queue




9-stock.js                       Contains an array with the following products:
    Id: 1, name: Suitcase 250, price: 50, stock: 4
    Id: 2, name: Suitcase 450, price: 100, stock: 10
    Id: 3, name: Suitcase 650, price: 350, stock: 2
    Id: 4, name: Suitcase 1050, price: 550, stock: 5

    a function named getItemById that takes id as an argument and returns an item from listProducts with the same id.
    Has an express server listening on the port 1245.
        Contains a route GET /list_products that will return the list of every available product in a JASON format.

    Has a redis client with:
        a function reserveStockById that will take itemId and stock as arguments:
            It will set in Redis the stock for the key item.ITEM_ID
        an async function getCurrentReservedStockById, that will take itemId as an argument:
            It will return the reserved stock for a specific item

    Has a route GET /list_products/:itemId, that will return the current product and the current available stock (by using getCurrentReservedStockById) in a JSON format.

    Has a route GET /reserve_product/:itemId: 
    if the item does not exist, it returns a JSON with the error: { "status": "Product not found" }
    If it exists, it checks if atleasts there is one item available, if not it returns: {"status":"Not enough stock available","itemId":1}
    If stock is available it returns: {"status":"Reservation confirmed","itemId":1}





100-seat.js                     Redis client with the following:
    A function reserveSeat, that takes into argument number, and set the key available_seats with the number
    A function getCurrentAvailableSeats, it returns the current number of available seats (by using promisify for Redis)
    When launching the application, it sets the number of available to 50
    Initializes the boolean reservationEnabled to true - it will return to false when no seat will be available.

    An express server listening on the port 1245
        Has a route GET /available_seats that returns the number of seat available.
        Has a route GET /reserve_seat
            Returns { "status": "Reservation are blocked" } if reservationEnabled is false
            Creates and queues a job in the queue reserve_seat:
                Saves the job and return:
                    { "status": "Reservation in process" } if no error
                    Otherwise: { "status": "Reservation failed" }
                When the job is completed, prints in the console: Seat reservation job JOB_ID completed
                When the job failed, prints in the console: Seat reservation job JOB_ID failed: ERROR_MESSAGE
        Has a route GET /process
            Returns { "status": "Queue processing" } just after:
            Process the queue reserve_seat (async):
                Decrease the number of seat available by using getCurrentAvailableSeats and reserveSeat
                If the new number of available seats is equal to 0, set reservationEnabled to false
                If the new number of available seats is more or equal than 0, the job is successful
                Otherwise, fails the job with an Error with the message Not enough seats available

