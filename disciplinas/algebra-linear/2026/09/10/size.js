const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const question = (query) => new Promise((resolve) => rl.question(query, resolve));

const main = async () => {
  const size = await question('Digite o tamanho da matriz quadrada (n): ')
  console.log('O tamanho da matriz quadrada é:', size);

  const arr = [];
  for (let i = 0; i < size; i++) {
    arr[i] = [];
    for (let j = 0; j < size; j++) {
      const element = await question(`Digite o elemento da posição [${i}][${j}]: `);
      console.log(`Elemento na posição [${i}][${j}] é: ${element}`);
      arr[i][j] = element;
    }
  }

  console.log('A matriz é:', arr);
  rl.close();
}

main()
  .catch(console.error);
