import { createClient } from "redis";
import { print } from "redis";
import { promisify } from "util";


const client = createClient();

const getAsync = promisify(client.get).bind(client);

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

export const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
}

export const displaySchoolValue = async (schoolName) => {
  console.log(await getAsync(schoolName));
}

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}



