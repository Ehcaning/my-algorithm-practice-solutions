var shuffle = function (nums, n) {
	let leftSide = nums.splice(0, n);
	let rightSide = nums;

	let res = [];
	for (let i = 0; i < n; i++) {
		res.push(leftSide[i]);
		res.push(rightSide[i]);
	}
	return res;
};
