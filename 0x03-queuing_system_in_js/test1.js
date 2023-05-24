import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const updateHash = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

function main() {
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(hashObj)) {
    updateHash('HolbertonSchools', field, value);
  }
  printHash('HolbertonSchools');
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

import { createClient, print } from "redis";

const client = createClient();


client.on('connect', () => {
  console.log('Redis client connected to the server')
  testHash();
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

export const createHash = (key, field, value) => {
  client.hset(key, field, value, print);
}

export const printHash = (key) => {
  client.hgetall(key, (err, reply) => console.log(reply));
};

function testHash() {
  const hashables = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(hashables)) {
    createHash('HolbertonSchools', field, value);
  }
  printHash('HolbertonSchools');
}
/*
createHash('HolbertonSchools', 'Portland', '50');
createHash('HolbertonSchools', 'Seattle', '80');
createHash('HolbertonSchools', 'New York', '20');
createHash('HolbertonSchools', 'Bogota', '20');
createHash('HolbertonSchools', 'Cali', '40');
createHash('HolbertonSchools', 'Paris', '2');

printHash('HolbertonSchools');
*/


