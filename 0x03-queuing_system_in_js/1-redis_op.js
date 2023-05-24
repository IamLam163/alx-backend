import { print } from "redis";
import { createClient } from "redis";


const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

export const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
}

export const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (_, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
