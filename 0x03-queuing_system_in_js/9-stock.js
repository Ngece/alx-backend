import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

// product data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Redis client
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Reserve stock by itemId
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

// Get current reserved stock by itemId
async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  return parseInt(reservedStock) || 0;
}

// Middleware to parse JSON requests
app.use(express.json());

// Route to list all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get product details and current available stock
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = listProducts.find((p) => p.itemId === itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  res.json({
    ...product,
    currentQuantity: product.initialAvailableQuantity - currentReservedStock,
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = listProducts.find((p) => p.itemId === itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);

  if (currentReservedStock >= product.initialAvailableQuantity) {
    res.json({ status: 'Not enough stock available', itemId });
  } else {
    await reserveStockById(itemId, currentReservedStock + 1);
    res.json({ status: 'Reservation confirmed', itemId });
  }
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Close the Redis client when done
client.quit();
