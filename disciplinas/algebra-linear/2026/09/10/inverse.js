const inverse = (matrix) => {
	if (!Array.isArray(matrix) || matrix.length === 0) {
		throw new Error('A matriz deve ser quadrada e não vazia.');
	}

	const size = matrix.length;
	if (matrix.some((row) => !Array.isArray(row) || row.length !== size)) {
		throw new Error('A matriz deve ser quadrada.');
	}

	const augmented = matrix.map((row, rowIndex) => [
		...row.map(Number),
		...Array.from({ length: size }, (_, columnIndex) => (
			rowIndex === columnIndex ? 1 : 0
		)),
	]);

	if (augmented.some((row) => row.some((value) => !Number.isFinite(value)))) {
		throw new Error('Todos os elementos devem ser números finitos.');
	}

	for (let column = 0; column < size; column++) {
		let pivotRow = column;
		for (let row = column + 1; row < size; row++) {
			if (Math.abs(augmented[row][column]) > Math.abs(augmented[pivotRow][column])) {
				pivotRow = row;
			}
		}

		if (Math.abs(augmented[pivotRow][column]) < Number.EPSILON) {
			throw new Error('A matriz é singular e não possui inversa.');
		}

		[augmented[column], augmented[pivotRow]] = [augmented[pivotRow], augmented[column]];

		const pivot = augmented[column][column];
		augmented[column] = augmented[column].map((value) => value / pivot);

		for (let row = 0; row < size; row++) {
			if (row === column) continue;

			const factor = augmented[row][column];
			augmented[row] = augmented[row].map((value, index) => (
				value - factor * augmented[column][index]
			));
		}
	}

	return augmented.map((row) => row.slice(size));
};

const formatMatrix = (matrix) => matrix
	.map((row) => `[ ${row.map((value) => Number(value.toFixed(10))).join('  ')} ]`)
	.join('\n');

const main = async () => {
	const readline = require('readline');
	const rl = readline.createInterface({
		input: process.stdin,
		output: process.stdout,
	});

	const question = (query) => new Promise((resolve) => rl.question(query, resolve));

	try {
		const size = Number(await question('Digite o tamanho da matriz quadrada (n): '));
		if (!Number.isInteger(size) || size <= 0) {
			throw new Error('O tamanho deve ser um inteiro positivo.');
		}

		const matrix = [];
		for (let row = 0; row < size; row++) {
			matrix[row] = [];
			for (let column = 0; column < size; column++) {
				matrix[row][column] = Number(await question(
					`Digite o elemento da posição [${row}][${column}]: `,
				));
			}
		}

		console.log('A matriz inversa é:');
		console.log(formatMatrix(inverse(matrix)));
	} catch (error) {
		console.error(error.message);
		process.exitCode = 1;
	} finally {
		rl.close();
	}
};

module.exports = inverse;

if (require.main === module) {
	main();
}
